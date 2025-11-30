# Utils – Flask Upload System

This directory contains the utility modules that power the Flask-based file
upload system used in the programming assignment rounds (Rodada 1 and Rodada 2).
These files define configuration, routing, templates, and server behavior for
the web application.

## Files overview

### `config.py`
Application configuration module.  
Defines upload directories, allowed extensions, round control flags, timeout
settings, and general environment variables.

### `gunicorn_config.py`
Configuration file for running the application with **Gunicorn**.  
Optimized for a single worker using `gevent` to avoid concurrency conflicts
related to shared state.

### `routes.py`
All Flask routes are registered here.  
Handles:
- Upload endpoints for Rodada 1 and Rodada 2  
- Status and toggle APIs for administrators  
- Dashboard endpoint  
- Automatic directory creation and file name conflict resolution

### `server.py`
Main application entry point.  
Initializes Flask, loads configuration, registers routes, and can run either
with Flask’s development server or via Gunicorn in production.

### `templates.py`
Contains inline page templates rendered via `render_template_string()`,
including:
- Home page  
- Upload pages for both rounds  
- Locked round page  
- Admin dashboard  
Templates include UI logic, QR code display, and live status checking.

## Purpose

These utilities enable a controlled environment for student submissions during
the TDD/AI programming study. They support:
- Managed upload windows  
- Logging of interactions  
- Secure ZIP uploads  
- Instructor dashboard and monitoring  
- Clear feedback to participants  

## Notes

- All uploads are stored inside the folders defined in `config.py`.  
- Round release/bock logic uses in-memory state and is designed for
single-worker deployment.  
- For production usage, run with:

```bash
gunicorn -c gunicorn_config.py server:app
