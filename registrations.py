# registrations.py
# Manages student registrations for events.
#
# KEY CONFLICT ZONE: register_student() is intentionally minimal.
# Multiple developers will add different validations on separate branches,
# making it the perfect function for demonstrating merge conflicts.
#
# Developer A might add:  if not student_name: ...
# Developer B might add:  if not get_event(event_id): ...
# Developer C might add:  capacity check
# Developer D might add:  duplicate registration check
# demooooooovdoishuwdhiqeuyiewqqfewgh

from events import get_event

registrations = []


def list_registrations():
    """Return all registrations."""
    return registrations


def register_student(student_name, event_id):
    """
    Register a student for an event.

    Returns True on success, False on failure.

    Intentionally minimal — students will later add:
      - student_name validation          (Developer A)
      - event existence check            (Developer B)
      - capacity validation              (Developer C)
      - duplicate registration check     (Developer D)
    """
    registration = {"student": student_name, "event_id": event_id}
    registrations.append(registration)
    return True


def cancel_registration(student_name, event_id):
    """
    Cancel a student's registration.

    Returns True if cancelled, False if registration not found.
    Students can extend this on a branch.
    """
    global registrations
    original_len = len(registrations)
    registrations = [
        r for r in registrations
        if not (r["student"] == student_name and r["event_id"] == event_id)
    ]
    return len(registrations) < original_len


def get_registrations_for_event(event_id):
    """Return all registrations for a given event id."""
    return [r for r in registrations if r["event_id"] == event_id]


def get_registrations_for_student(student_name):
    """Return all registrations for a given student."""
    return [r for r in registrations if r["student"] == student_name]
