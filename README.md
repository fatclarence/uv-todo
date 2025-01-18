A todo app based on https://dev.to/rodbv/creating-a-to-do-app-with-django-and-htmx-part-1-583p

Learning how to use uv and Django.

# Setup process:

1. Install uv
2. Ran `uv init`
3. Ran `uv venv` & `source .venv/bin/activate` - Create virtual environment
4. Ran `uv add django`
5. Ran `uv run django-admin startproject todo_django .` - Create Django project in current directory:

- The settings.py contains your project-wide configurations
- urls.py handles top-level URL routing
- manage.py is the command-line utility you'll use to interact with your project

6. Ran `uv run python manage.py runserver`
7. Override Django's default user model, which is a best-practice for new projects.
8. Ran: `uv run python manage.py startapp core` - `startapp` creates a new application within your Django project.

- An app is a self-contained module that handles a specific functionality of your website.
