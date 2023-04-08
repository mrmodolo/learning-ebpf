#!/bin/bash
#
export LD_LIBRARY_PATH=/opt/bcc/lib 
export PYTHON="$(which python)"

PRG="${1}"

sudo LD_LIBRARY_PATH="${LD_LIBRARY_PATH}" "${PYTHON}" "${PRG}"
