# Campus Event Manager

A simple CLI application for managing college campus events.  
Built as the shared project for a Git & GitHub hands-on seminar.

> **The application is NOT the focus.**  
> Git workflows, branching, pull requests, and collaboration are.

---

## Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/<your-org>/campus-event-manager.git
cd campus-event-manager

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # macOS / Linux
venv\Scripts\activate           # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the application
python app.py

# 5. Run the tests
pytest --tb=short -v
```

---

## Project Structure

```
campus-event-manager/
│
├── app.py               # CLI menu loop — entry point
├── events.py            # Event data and functions
├── registrations.py     # Registration data and functions
├── utils.py             # Shared print/format helpers
│
├── test_events.py       # Tests for events.py
├── test_registrations.py# Tests for registrations.py
│
├── requirements.txt     # pytest only
├── .gitignore
│
└── .github/
    └── workflows/
        └── ci.yml       # GitHub Actions: runs pytest on every push/PR
```

### File Descriptions

| File | Purpose |
|---|---|
| `app.py` | Main entry point. Runs the menu loop and calls handler functions. Easy to extend with new menu items. |
| `events.py` | In-memory list of events. Contains `list_events`, `add_event`, `search_events`, `get_event`, `delete_event`. |
| `registrations.py` | In-memory list of registrations. Contains `register_student`, `cancel_registration`, `list_registrations`, and helpers. |
| `utils.py` | Print helpers and `prompt_int`. Easy to improve or extend. |
| `test_events.py` | Pytest tests for all event functions. |
| `test_registrations.py` | Pytest tests for all registration functions. |
| `ci.yml` | GitHub Actions workflow. Runs `pytest` on every push and pull request to `main`. |

---

## Sample Session

```
========================================
       CAMPUS EVENT MANAGER
========================================
  1. List Events
  2. Add Event
  3. Search Events
  4. Register for Event
  5. Cancel Registration
  6. List Registrations
  7. Exit
========================================
  Enter choice: 1

========================================
  All Events
========================================
  [1] Python Workshop  (capacity: 30)
  [2] Git & GitHub Bootcamp  (capacity: 25)
  [3] Career Fair  (capacity: 100)
  [4] Hackathon 2026  (capacity: 50)
```

---

## Student Feature Tasks

Each task is small enough to complete in 10–20 minutes and lives on its own branch.

| # | Branch | Task |
|---|--------|------|
| 1 | `feature/search-events` | Implement keyword search in `events.py` and wire it to the menu |
| 2 | `feature/cancel-registration` | Implement cancel registration and wire it to the menu |
| 3 | `feature/capacity-validation` | In `register_student()`, check if the event is at capacity |
| 4 | `feature/duplicate-check` | In `register_student()`, prevent a student from registering twice |
| 5 | `feature/student-name-validation` | In `register_student()`, reject empty or whitespace-only names |
| 6 | `feature/event-exists-check` | In `register_student()`, reject registrations for non-existent events |
| 7 | `feature/delete-event` | Implement `delete_event()` and add menu option 8 |
| 8 | `feature/list-my-registrations` | Add a menu option to show all events a specific student is registered for |
| 9 | `feature/event-validation` | In `add_event()`, reject empty names and capacity ≤ 0 |
| 10 | `feature/duplicate-event-name` | In `add_event()`, reject duplicate event names |
| 11 | `feature/improve-cli` | Improve menu formatting, add colour, or show event count in header |
| 12 | `feature/event-date` | Add a `date` field to events and update all related functions |
| 13 | `feature/registration-count` | Show how many students are registered when listing events |
| 14 | `feature/add-tests` | Write additional tests for edge cases in `test_registrations.py` |
| 15 | `feature/error-handling` | Improve error messages throughout `app.py` |
| 16 | `feature/confirm-cancel` | Ask for confirmation before cancelling a registration |
| 17 | `feature/sort-events` | List events sorted alphabetically by name |
| 18 | `feature/export-csv` | Export registrations to a CSV file using Python's `csv` module |
| 19 | `feature/paginate-list` | Show events 5 at a time with a "next page" option |
| 20 | `feature/utils-table` | Add a `print_table()` helper to `utils.py` and use it for listings |

## CI / GitHub Actions

The workflow in `.github/workflows/ci.yml` runs automatically on every push and pull request to `main`.

It does four things:
1. Checks out the code
2. Sets up Python 3.12
3. Installs `pytest` from `requirements.txt`
4. Runs `pytest --tb=short -v`

A green checkmark means all tests pass. A red ✗ means something broke — investigate the log.
