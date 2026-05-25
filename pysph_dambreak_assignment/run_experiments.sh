#!/bin/bash

echo "Running baseline experiment..."
python dam_break_baseline.py

echo "Running dx modified experiment..."
python dam_break_dx_modified.py

echo "Running gravity modified experiment..."
python dam_break_gravity_modified.py