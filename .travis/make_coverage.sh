#!/usr/bin/env bash
rm -rf .coverage
coverage run tests/test_controllers/test_user_connexion_controller.py
coverage report
coverage xml