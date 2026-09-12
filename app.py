#!/usr/bin/env python3
# app.py
# Entry point. Runs the CLI menu loop.
#
# CONFLICT ZONE: The menu and its handlers are easy for multiple
# developers to extend. Adding a new menu option always touches
# the same block of if/elif code, making conflicts likely and realistic.

import events as ev
import registrations as reg
from utils import print_header, print_event, print_registration, prompt_int


def show_menu():
    print()
    print("=" * 40)
    print("       CAMPUS EVENT MANAGER")
    print("=" * 40)
    print("  1. List Events")
    print("  2. Add Event")
    print("  3. Search Events")
    print("  4. Register for Event")
    print("  5. Cancel Registration")
    print("  6. List Registrations")
    print("  7. Exit")
    print("=" * 40)


def handle_list_events():
    print_header("All Events")
    all_events = ev.list_events()
    if not all_events:
        print("  No events found.")
        return
    for event in all_events:
        print_event(event)


def handle_add_event():
    print_header("Add Event")
    name = input("  Event name: ").strip()
    capacity = prompt_int("  Capacity: ")
    if not name or capacity is None:
        print("  Invalid input. Event not added.")
        return
    event = ev.add_event(name, capacity)
    print(f"  Event added: [{event['id']}] {event['name']}")


def handle_search_events():
    print_header("Search Events")
    keyword = input("  Enter keyword: ").strip()
    results = ev.search_events(keyword)
    if not results:
        print("  No matching events.")
        return
    for event in results:
        print_event(event)


def handle_register():
    print_header("Register for Event")
    student = input("  Your name: ").strip()
    event_id = prompt_int("  Event ID: ")
    if not student or event_id is None:
        print("  Invalid input.")
        return
    success = reg.register_student(student, event_id)
    if success:
        print(f"  {student} registered for event {event_id}.")
    else:
        print("  Registration failed.")


def handle_cancel():
    print_header("Cancel Registration")
    student = input("  Your name: ").strip()
    event_id = prompt_int("  Event ID: ")
    if not student or event_id is None:
        print("  Invalid input.")
        return
    success = reg.cancel_registration(student, event_id)
    if success:
        print(f"  Registration cancelled.")
    else:
        print("  No matching registration found.")#no registrstion
        


def handle_list_registrations():
    print_header("All Registrations")
    all_regs = reg.list_registrations()
    if not all_regs:
        print("  No registrations yet.")
        return
    for r in all_regs:
        print_registration(r)


def main():
    while True:
        show_menu()
        choice = input("  Enter choice: ").strip()

        if choice == "1":
            handle_list_events()
        elif choice == "2":
            handle_add_event()
        elif choice == "3":
            handle_search_events()
        elif choice == "4":
            handle_register()
        elif choice == "5":
            handle_cancel()
        elif choice == "6":
            handle_list_registrations()
        elif choice == "7":
            print("\n  Goodbye!\n")
            break
        else:
            print("  Invalid choice. Please enter 1–7.")


if __name__ == "__main__":
    main()
