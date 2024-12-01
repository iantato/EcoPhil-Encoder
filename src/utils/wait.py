import random

def uniform_delay(delay_range: str) -> float:
    """
    Generate a random delay between two values.

    Args:
        delay_range (str): A preset string ('short', 'medium', 'long') to determine the range of the delay

    Returns:
        float: The actual delay time.
    """
    PRESET_DELAYS = {
        'short': (0.5, 1),
        'medium': (1, 2),
        'long': (2, 3)
    }

    return random.uniform(*PRESET_DELAYS[delay_range])