from os.path import abspath
from os.path import expanduser
from os.path import join

from commoncode import command
from commoncode import fileutils
from scanpipe.pipes.d2d import FROM


def convert_dex_to_java(project, to_only=False):
    """
    Decompile .dex files in `project` into Java source code using `jadx`. If
    `to_only` is True, then only the .dex files in the to/ codebase are
    decompiled, otherwise all .dex files in `project are decompiled.
    """
    location = project.codebase_path
    abs_location = abspath(expanduser(location))
    for top, _, files in fileutils.walk(abs_location):
        for f in files:
            if not f.endswith(".dex") or (to_only and (FROM in top)):
                continue
            loc = join(top, f)
            run_jadx(location=loc)


def run_jadx(location):
    """
    Run the program `jadx` on the classes.dex file at `location`

    This will decompile the classes.dex file into Java source files.
    """
    command.execute(
        cmd_loc="jadx",
        args=[
            "-d",
            f"{location}-out",
            location,
        ],
        to_files=False,
    )
