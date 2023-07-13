import time
from typing import Any


def timer(func: Any) -> Any:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time

        seconds = int(elapsed_time + 0.5)
        hours = seconds // 3_600
        minutes = (seconds - hours * 3_600) // 60
        seconds = seconds - hours * 3_600 - minutes * 60

        print(f"Elapsed time: {hours:02}:{minutes:02}:{seconds:02}")
        return result

    return wrapper
