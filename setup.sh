#!/bin/bash

aoc_install_deps () {
    python -m pip install -r requirements.txt
}

aoc_new_day() {
    cp -R template day$1
    cd day$1
    python -m venv .venv
    . .venv/bin/activate
    aoc_install_deps
}
