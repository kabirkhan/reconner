#!/usr/bin/env bash

set -e
set -x

mypy reconer --disallow-untyped-defs
black reconer tests --check
isort --multi-line=3 --trailing-comma --force-grid-wrap=0 --combine-as --line-width 88 --recursive --check-only --thirdparty reconer
