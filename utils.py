# utils.py
# Shared helpers for printing and formatting.
# Small and easy to understand — students can improve print_event()
# or add a new helper on a feature branch.


def print_header(title):
    """Print a simple section header."""
    print()
    print("=" * 40)
    print(f"  {title}")
    print("=" * 40)


def print_event(event):
    """Print a single event in a readable format."""
    print(f"  [{event['id']}] {event['name']}  (capacity: {event['capacity']})")


def print_registration(registration):
    """Print a single registration in a readable format."""
    print(f"  {registration['student']}  →  Event ID {registration['event_id']}")


def prompt_int(message):
    """
    Ask the user to enter an integer.
    Returns None if the input is not a valid integer.
    """
    raw = input(message).strip()
    try:
        return int(raw)
    except ValueError:
        return None
#hello