# OctoFit Tracker — Backend (minimal developer notes)

This README contains minimal steps to set up and run the backend for the OctoFit Tracker app.

Paths used in this repo (root-relative):

- Backend folder: `octofit-tracker/backend`
- Django project: `octofit-tracker/backend/octofit_tracker`

Prerequisites
- Python 3 (python3)
- Git and network access to PyPI

Quick setup (recommended)

1. Create a virtual environment (this project uses a venv inside the backend directory):

```bash
python3 -m venv octofit-tracker/backend/venv
```

2. Activate the venv (bash):

```bash
source octofit-tracker/backend/venv/bin/activate
```

3. Install Python dependencies:

```bash
pip install -r octofit-tracker/backend/requirements.txt
```

4. Run Django migrations and start the development server:

```bash
python octofit-tracker/backend/octofit_tracker/manage.py migrate
python octofit-tracker/backend/octofit_tracker/manage.py createsuperuser  # optional
python octofit-tracker/backend/octofit_tracker/manage.py runserver 0.0.0.0:8000
```

Notes
- If you prefer not to `cd` into directories, use absolute paths or the venv python directly. Example (no venv activation):

```bash
/workspaces/skills-build-applications-w-copilot-agent-mode/octofit-tracker/backend/venv/bin/python \
  /workspaces/skills-build-applications-w-copilot-agent-mode/octofit-tracker/backend/octofit_tracker/manage.py runserver 0.0.0.0:8000
```

- Forwarded ports in this environment: 8000 (public) is used for the Django dev server.
- The project `requirements.txt` is at `octofit-tracker/backend/requirements.txt` and was added earlier.

Next steps
- Initialize apps (e.g., `activities`, `users`) with `python manage.py startapp <appname>` and register them in `settings.py`.
- If you plan to use MongoDB/djongo in development, add DB settings to `octofit-tracker/backend/octofit_tracker/octofit_tracker/settings.py` (note: `djongo` has compatibility caveats).

If you want, I can add a short `Makefile` or root-level run scripts to simplify these steps.
