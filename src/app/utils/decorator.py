def do_not_modify(func):
    """
    Decorator to mark a function as critical and not to be modified.
    """
    def wrapper(*args, **kwargs):
        print(f"Warning: {func.__name__} is marked as 'do-not-modify'.")
        return func(*args, **kwargs)
    return wrapper


def should_modify(func):
    """
    Decorator to mark a function as subject to modification.
    """
    def wrapper(*args, **kwargs):
        print(f"Notice: {func.__name__} should be modified.")
        return func(*args, **kwargs)
    return wrapper