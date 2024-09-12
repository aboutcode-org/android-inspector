# SPDX-License-Identifier: Apache-2.0
#
# Copyright (c) nexB Inc. and others. All rights reserved.
# ScanCode is a trademark of nexB Inc.
# SPDX-License-Identifier: Apache-2.0
# See http://www.apache.org/licenses/LICENSE-2.0 for the license text.
# See https://github.com/aboutcode-org/android-inspector for support or download.
# See https://aboutcode.org for more information about nexB OSS projects.
#

import os

from os.path import abspath
from os.path import expanduser
from os.path import join

from commoncode import command
from commoncode import fileutils

_IS_JADX_INSTALLED = None


def is_jadx_installed():
    """
    Check if jadx is installed.
    """
    global _IS_JADX_INSTALLED

    if _IS_JADX_INSTALLED is None:
        _IS_JADX_INSTALLED = False
        try:
            rc, result, err = command.execute(
                cmd_loc="jadx",
                args=["--version"],
                to_files=False,
            )

            if rc != 0:
                raise Exception(err)

            if "1.5.0" in result:
                _IS_JADX_INSTALLED = True

        except FileNotFoundError:
            pass

    return _IS_JADX_INSTALLED


def run_jadx(location, jadx_output_location=None):
    """
    Run the program `jadx` on the classes.dex file at `location`

    This will decompile the classes.dex file into Java source files.

    If `jadx_output_location` is provided, then the source files from the
    decompiled .dex files will be created there.
    """
    if not is_jadx_installed():
        return

    if jadx_output_location:
        jadx_output_location = os.path.abspath(os.path.expanduser(jadx_output_location))
    else:
        jadx_output_location = f"{location}-out"

    command.execute(
        cmd_loc="jadx",
        args=[
            "-d",
            jadx_output_location,
            location,
        ],
        to_files=False,
    )


def convert_dex_to_java(project, to_only=False):
    """
    Decompile .dex files in `project` into Java source code using `jadx`. If
    `to_only` is True, then only the .dex files in the to/ codebase are
    decompiled, otherwise all .dex files in `project are decompiled.
    """
    from scanpipe.pipes.d2d import FROM

    location = project.codebase_path
    abs_location = abspath(expanduser(location))
    for top, _, files in fileutils.walk(abs_location):
        for f in files:
            if not f.endswith(".dex") or (to_only and (FROM in top)):
                continue
            loc = join(top, f)
            run_jadx(location=loc)
