#!/bin/bash

# Execute the unit tests in this project with the pytest library.
# Chris Joakim, Microsoft, 2020/09/29

source bin/activate

python -m pytest tests/ 
