def time_execution(seconds):
    """Time the execution of a function.

    Parameters
    ----------
    seconds : int
        Number of seconds to wait.
    """
    h = int(seconds / 3600)
    m = int((seconds - h * 3600) / 60)
    s = seconds % 60
    return f"{h}:{m}:{round(s,1)}"
