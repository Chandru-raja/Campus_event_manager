# test_events.py
# Unit tests for events.py.
# Kept simple so juniors can read and extend them easily.

import pytest
import events


@pytest.fixture(autouse=True)
def reset_events():
    """Restore the events list to its original state before each test."""
    original = events.events[:]
    original_id = events._next_id
    yield
    events.events = original
    events._next_id = original_id


def test_list_events_returns_list():
    result = events.list_events()
    assert isinstance(result, list)


def test_list_events_not_empty():
    result = events.list_events()
    assert len(result) > 0


def test_add_event():
    before = len(events.list_events())
    event = events.add_event("Test Event", 20)
    assert len(events.list_events()) == before + 1
    assert event["name"] == "Test Event"
    assert event["capacity"] == 20
    assert "id" in event


def test_add_event_assigns_unique_id():
    e1 = events.add_event("Event One", 10)
    e2 = events.add_event("Event Two", 10)
    assert e1["id"] != e2["id"]


def test_get_event_found():
    event = events.get_event(1)
    assert event is not None
    assert event["id"] == 1


def test_get_event_not_found():
    event = events.get_event(9999)
    assert event is None


def test_search_events_match():
    results = events.search_events("python")
    assert len(results) >= 1
    assert all("python" in r["name"].lower() for r in results)


def test_search_events_no_match():
    results = events.search_events("xyznonexistent")
    assert results == []


def test_search_events_case_insensitive():
    results_lower = events.search_events("git")
    results_upper = events.search_events("GIT")
    assert len(results_lower) == len(results_upper)


def test_delete_event_existing():
    events.add_event("To Delete", 5)
    all_ids = [e["id"] for e in events.list_events()]
    target_id = all_ids[-1]
    deleted = events.delete_event(target_id)
    assert deleted is True
    assert events.get_event(target_id) is None


def test_delete_event_not_found():
    deleted = events.delete_event(9999)
    assert deleted is False
