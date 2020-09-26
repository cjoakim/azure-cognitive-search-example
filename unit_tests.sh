#!/bin/bash

# Execute the unit tests in this project with the pytest library.
# Chris Joakim, Microsoft, 2020/09/26

source bin/activate

echo 'executing unit tests ...'
pytest --ignore=lib/
