from commoncode import command

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

            if result.startswith("jadx"):
                _IS_JADX_INSTALLED = True

        except FileNotFoundError:
            pass

    return _IS_JADX_INSTALLED
