#!/bin/bash

dir_here="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
bin_python="${HOME}/venvs/python/3.8.11/wow_wtf_manager_venv/bin/python"
${bin_python} "run.py"
