# events.py
# Manages the list of campus events.
# This file is a natural conflict zone:
# multiple developers can add validation to add_event().

events = [
    {"id": 1, "name": "Python Workshop",     "capacity": 30},
    {"id": 2, "name": "Git & GitHub Bootcamp","capacity": 25},
    {"id": 3, "name": "Career Fair",          "capacity": 100},
    {"id": 4, "name": "Hackathon 2026-2027",       "capacity": 50},
]

_next_id = 5   # simple auto-increment; no database needed


def list_events():
    """Return all events."""
    return events


def get_event(event_id):
    """Return a single event by id, or None if not found."""
    for event in events:
        if event["id"] == event_id:
            return event
    return None


def add_event(name, capacity):
    """
    Add a new event.

    Intentionally minimal — students will later add:
      - name length validation
      - capacity > 0 check
      - duplicate name check
    """
    global _next_id
    event = {"id": _next_id, "name": name, "capacity": capacity}
    events.append(event)
    _next_id += 1
    return event


def search_events(keyword):
    """Return events whose name contains keyword (case-insensitive)."""
    keyword = keyword.lower()
    return [e for e in events if keyword in e["name"].lower()]


def delete_event(event_id):
    """
    Remove an event by id.
    Returns True if deleted, False if not found.
    Students can add this feature on a branch.
    """
    global events
    original_len = len(events)
    events = [e for e in events if e["id"] != event_id]
    return len(events) < original_len
