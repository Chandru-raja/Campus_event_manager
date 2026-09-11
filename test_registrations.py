# test_registrations.py
# Unit tests for registrations.py.
# Kept simple — students will add more tests as a feature task.

import pytest
import registrations


@pytest.fixture(autouse=True)
def reset_registrations():
    """Clear registrations before each test so tests don't interfere."""
    registrations.registrations.clear()
    yield
    registrations.registrations.clear()


def test_list_registrations_initially_empty():
    result = registrations.list_registrations()
    assert result == []


def test_register_student_success():
    success = registrations.register_student("Alice", 1)
    assert success is True


def test_register_student_appears_in_list():
    registrations.register_student("Alice", 1)
    all_regs = registrations.list_registrations()
    assert len(all_regs) == 1
    assert all_regs[0]["student"] == "Alice"
    assert all_regs[0]["event_id"] == 1


def test_register_multiple_students():
    registrations.register_student("Alice", 1)
    registrations.register_student("Bob", 1)
    registrations.register_student("Charlie", 2)
    assert len(registrations.list_registrations()) == 3


def test_cancel_registration_success():
    registrations.register_student("Alice", 1)
    cancelled = registrations.cancel_registration("Alice", 1)
    assert cancelled is True
    assert len(registrations.list_registrations()) == 0


def test_cancel_registration_not_found():
    cancelled = registrations.cancel_registration("Nobody", 99)
    assert cancelled is False


def test_cancel_only_removes_matching():
    registrations.register_student("Alice", 1)
    registrations.register_student("Alice", 2)
    registrations.cancel_registration("Alice", 1)
    remaining = registrations.list_registrations()
    assert len(remaining) == 1
    assert remaining[0]["event_id"] == 2


def test_get_registrations_for_event():
    registrations.register_student("Alice", 1)
    registrations.register_student("Bob", 1)
    registrations.register_student("Charlie", 2)
    result = registrations.get_registrations_for_event(1)
    assert len(result) == 2


def test_get_registrations_for_student():
    registrations.register_student("Alice", 1)
    registrations.register_student("Alice", 3)
    registrations.register_student("Bob", 1)
    result = registrations.get_registrations_for_student("Alice")
    assert len(result) == 2
