#! /usr/bin/env bash

set -o errexit
set -o nounset
set -o pipefail

export FLASK_DEBUG=1
python -m nxcontact
