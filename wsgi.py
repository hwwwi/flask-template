#! /usr/bin/env python3
""" wsgi entrypoint """

import logging
from dotenv import load_dotenv
from app import create_app

load_dotenv()  # Read config from .env
app = create_app()

if __name__ == '__main__':
    # When running wsgi.py directly for debug
    app.run()
else:
    # When running through gunicorn
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
