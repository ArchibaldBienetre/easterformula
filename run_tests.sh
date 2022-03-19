#!/usr/bin/env bash

python -m pytest --cov=easterformula_module  --cov-report=html tests/easterformula_tests.py
