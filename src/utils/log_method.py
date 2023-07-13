from typing import Any, Dict


def log_method(starting: str = None, completed: str = None) -> Any:
    def decorator(func: Any) -> Any:
        def wrapper(self: Any, *args: Any, **kwargs: Dict[str, Any]) -> Any:
            method_name = func.__name__
            starting_message = (
                "Starting {method_name} process" if starting is None else starting
            )
            completed_message = (
                "Completed {method_name} process" if completed is None else completed
            )

            self.logger.info(starting_message.format(method_name=method_name))
            result = func(self, *args, **kwargs)
            self.logger.info(completed_message.format(method_name=method_name))
            return result

        return wrapper

    return decorator
