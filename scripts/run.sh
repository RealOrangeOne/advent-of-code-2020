#!/usr/bin/env bash


TIMEFORMAT="time %3R"

for task_dir in [0-9]*; do
    for py_file in $task_dir/*.py; do
        echo -e "\n> $py_file"
        time python3 "$py_file"
    done

    if [ -d "$task_dir/rust" ]; then
        echo -e "\n> $task_dir/rust"
        cd $task_dir/rust && time cargo run --release -q && cd - > /dev/null
    fi
done
