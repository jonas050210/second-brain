"""Playwright browser tests for the Second Brain frontend.

These run against the live app server. They exercise the core Chat → Memory →
Graph workflow plus navigation, search, and settings.

Skip gracefully if Playwright/Chromium isn't available (documented limitation).
"""
import os
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

pytest.importorskip("playwright.sync_api", reason="Playwright not installed")

from playwright.sync_api import sync_playwright  # noqa: E402

BASE_URL = os.environ.get("SECOND_BRAIN_URL", "http://127.0.0.1:8000")


@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        try:
            b = p.chromium.launch(headless=True)
        except Exception as e:
            pytest.skip(f"Chromium unavailable: {e}")
        yield b
        b.close()


@pytest.fixture()
def page(browser):
    ctx = browser.new_context()
    pg = ctx.new_page()
    yield pg
    ctx.close()


def _seed_empty(page):
    """Reset the database so tests start from a clean slate."""
    page.request.post(BASE_URL + "/api/reset", data='{"confirm": true}',
                      headers={"Content-Type": "application/json"})


def _wait_boot(page):
    """Wait for the async boot() to finish (dashboard becomes active/populated)."""
    page.wait_for_selector("#view-dashboard.active .stat-card", timeout=15000)


def test_dashboard_loads(page):
    page.goto(BASE_URL + "/")
    # Wait for the async boot() to populate the dashboard stats.
    page.wait_for_selector("#view-dashboard.active .stat-card", timeout=10000)
    assert page.locator("#stats-grid .stat-card").count() >= 1


def test_chat_sends_message_and_memory_update(page):
    _seed_empty(page)
    page.goto(BASE_URL + "/")
    _wait_boot(page)
    page.click('[data-view="chat"]')
    page.fill("#chat-input", "I am learning Rust and I want to build a game engine")
    page.click("#chat-send")
    # Memory update box appears.
    page.wait_for_selector(".remembered-box", timeout=8000)
    assert "Rust" in page.locator(".remembered-box").inner_text()


def test_entity_can_be_opened(page):
    _seed_empty(page)
    page.goto(BASE_URL + "/")
    _wait_boot(page)
    page.click('[data-view="chat"]')
    page.fill("#chat-input", "I am learning Python")
    page.click("#chat-send")
    page.wait_for_selector(".remembered-chip", timeout=8000)
    page.locator(".remembered-chip").first.click()
    page.wait_for_selector("#entity-panel.open")
    assert "Python" in page.locator(".entity-title").inner_text()


def test_graph_updates(page):
    _seed_empty(page)
    page.goto(BASE_URL + "/")
    _wait_boot(page)
    page.click('[data-view="chat"]')
    page.fill("#chat-input", "My project Nebula uses Next.js")
    page.click("#chat-send")
    page.wait_for_selector(".remembered-box", timeout=8000)
    page.click('[data-view="graph"]')
    page.wait_for_selector("#cy")
    # The graph should render nodes (canvas-based, so check the sub line updates).
    page.wait_for_timeout(1500)
    sub = page.locator("#graph-sub").inner_text()
    assert "entities" in sub


def test_search_works(page):
    _seed_empty(page)
    page.goto(BASE_URL + "/")
    _wait_boot(page)
    page.click('[data-view="chat"]')
    page.fill("#chat-input", "I am learning Rust")
    page.click("#chat-send")
    page.wait_for_selector(".remembered-box", timeout=8000)
    page.click('[data-view="search"]')
    page.fill("#search-input", "What am I learning?")
    page.click("#search-btn")
    page.wait_for_selector("#search-answer", timeout=8000)
    assert "Rust" in page.locator("#search-answer").inner_text()


def test_entity_browser_and_palette_markup():
    html = open(os.path.join(os.path.dirname(__file__), "..", "frontend", "index.html"), encoding="utf-8").read()
    js = open(os.path.join(os.path.dirname(__file__), "..", "frontend", "app.js"), encoding="utf-8").read()
    assert 'id="view-browse"' in html
    assert 'aria-label="Dashboard"' in html
    assert 'role="status"' in html
    assert 'id="palette"' in html
    assert 'id="privacy-info"' in html
    assert 'id="backup-list"' in html
    assert 'id="gf-layout"' in html
    assert 'id="set-auto-backup"' in html
    assert 'id="conv-search"' in html
    assert 'id="gf-around-me"' in html
    assert 'id="graph-to-me"' in html
    assert 'id="browse-sort"' in html
    assert 'id="chat-undo"' in html
    assert "conv-sum" in js
    assert 'id="import-file"' in html
    assert 'id="browse-orphans"' in html
    assert 'id="mem-q"' in html
    assert 'id="conv-archived"' in html
    assert "function loadBrowse" in js
    assert "function formatImportReport" in js
    assert "/graph?focus=" in js
    assert "function openPalette" in js
    assert "function runGraphLayout" in js
    assert "function applyRoute" in js
    assert "function sourceChips" in js
    assert "opts.created_at" in js
    assert "data-mid" in js
    assert "Open source message" in js
    assert "runViewLoad(loadBrowse, \"entities\")" in js
    assert "if (ev.target.closest(\".rel-del\")) return;" in js
    assert "let paletteRequest = 0;" in js
    assert "if (request !== conversationRequest) return;" in js
    assert "Looks similar" in js
    assert "sources: m.sources" in js
    assert "function restore" not in js or "/backup/restore" in js


def test_settings_load(page):
    page.goto(BASE_URL + "/")
    _wait_boot(page)
    page.click('[data-view="settings"]')
    page.wait_for_selector("#view-settings.active #set-llm", timeout=10000)
    # Wait until boot() has loaded settings into the input.
    page.wait_for_function("document.querySelector('#set-llm').value.length > 0", timeout=10000)
    assert page.locator("#set-llm").input_value()


def test_reset_confirmation(page):
    page.goto(BASE_URL + "/")
    _wait_boot(page)
    page.click('[data-view="settings"]')
    page.wait_for_selector("#view-settings.active #reset-btn", timeout=10000)
    page.on("dialog", lambda d: d.dismiss())  # cancel the confirm
    page.click("#reset-btn")
    # Should not navigate away; still on settings.
    assert page.locator("#reset-btn").count() == 1
