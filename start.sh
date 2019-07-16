#!/usr/bin/env bash
# For development use (simple logging, etc):
# python3 app.py

# For production use:
gunicorn app:app -w 1 --log-file -