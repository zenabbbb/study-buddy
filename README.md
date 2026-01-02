# Study Buddy — Productivity & Wellness Assistant (Backend)

Study Buddy is a Django + Django REST Framework (DRF) backend that powers a productivity + wellness assistant.
It supports user profiles, tasks, study sessions, hydration logs, and reminders—designed to plug into a web/mobile UI.

## Features
- Users (profile + preferences)
- Tasks (status updates + completion tracking)
- Study sessions (start/end + counters)
- Hydration logs
- Reminders (with optional scheduling/recurrence)

## Tech Stack
Python • Django • Django REST Framework • SQLite (dev)

## Run Locally (Windows)
```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
