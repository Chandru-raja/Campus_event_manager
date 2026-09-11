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

---

## Git Scenarios for the Seminar

### 1 — Basic workflow
```bash
git clone ...
git switch -c feature/search-events
# make changes
git status
git diff
git add events.py
git commit -m "Add keyword search for events"
git push origin feature/search-events
# open Pull Request on GitHub
# merge after review
```

### 2 — Parallel development
Two students work on separate branches simultaneously:
- Student A: `feature/capacity-validation`
- Student B: `feature/duplicate-check`

Both branches touch `register_student()` — when merged one after the other, the second merge produces a conflict.

### 3 — Merge conflict (the main demo)
**Setup:**
```bash
# Student A's branch
git switch -c feature/student-name-validation
# adds: if not student_name: return False
git commit -m "Validate student name"

# Student B's branch (from main, before A is merged)
git switch -c feature/event-exists-check
# adds: if not get_event(event_id): return False
git commit -m "Check event exists before registering"
```
**Conflict:** When B's branch is merged after A's, Git cannot auto-merge `register_student()`.  
**Resolution:** The instructor shows how to read the conflict markers and combine both validations.

### 4 — Wrong commit / soft reset
```bash
# Accidentally committed debug print statements
git show                    # inspect the bad commit
git reset --soft HEAD~1     # undo commit, keep changes staged
# remove the debug lines
git commit -m "Add capacity validation (clean)"
```

### 5 — Lost commit / reflog
```bash
git reset --hard HEAD~1     # "lose" a commit
git reflog                  # find the lost commit hash
git checkout <hash>         # inspect it
git switch -c recovery      # or restore it on a new branch
```

### 6 — Stash
```bash
# Student is mid-way through a feature
git stash                           # save unfinished work
git switch main                     # switch to help a teammate
git switch feature/my-feature       # come back
git stash pop                       # restore work
```

### 7 — Wrong branch
```bash
# Student made changes on main by mistake
git diff                            # confirm the changes
git stash                           # or: git switch -c fix/oops
git switch -c feature/correct-branch
git stash pop
```

### 8 — Revert (safe undo on shared history)
```bash
# Bad commit is already on main and pushed
git log --oneline                   # find the bad commit hash
git revert <hash>                   # creates a new "undo" commit
git push                            # safe — history is preserved
```
Contrast with `reset --hard`, which rewrites history and is dangerous on shared branches.

### 9 — Deliberate CI failure
```python
# In events.py, break a function:
def list_events():
    return None          # was: return events
```
Push to a branch, open a PR — the CI badge goes red.  
Students paste the GitHub Actions log into an AI assistant:

```
Analyze this CI failure.
Identify:
1. Which test failed
2. What the root cause is
3. Which code is responsible
4. What the minimal fix is
Do not modify unrelated code.
```

Then verify and apply the fix, push again, and watch CI go green.

---

## CI / GitHub Actions

The workflow in `.github/workflows/ci.yml` runs automatically on every push and pull request to `main`.

It does four things:
1. Checks out the code
2. Sets up Python 3.12
3. Installs `pytest` from `requirements.txt`
4. Runs `pytest --tb=short -v`

A green checkmark means all tests pass. A red ✗ means something broke — investigate the log.
