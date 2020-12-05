#!/usr/bin/env bash


TIMEFORMAT="time %3R"

for task_dir in [0-9]*; do
    for py_file in $task_dir/*.py; do
        echo "> $py_file"
        time python3 "$py_file"
    done
done
