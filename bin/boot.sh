#!/usr/bin/env sh

alembic upgrade head

uvicorn --host=0.0.0.0 application:app --reload
