#! /usr/bin/env bash

set -o errexit
set -o nounset
set -o pipefail

(py-deactivate-env || /usr/bin/true) > /dev/null 2>&1
(deactivate || /usr/bin/true) > /dev/null 2>&1

rm -Rf \
        ./.virtualenv \
        ./.tox \
        ./node_modules \
        tags

find . -name __pycache__ -print -exec rm -Rf \{\} \;
find . -name '*.pyc' -delete
find ./ -name "*~" -exec rm -f \{\} \;

