from datetime import datetime, date
from typing import Union, List

def american_date(date_str: Union[str, List[str]]) -> Union[date, List[date]]:
    """
    Convert American date string (mm-dd-yy) to date object.

    Args:
        date_str (Union[str, List[str]]): A single date string or a list of date strings

    Returns:
        Single date object or list of date objects.
    """

    def single_date(date_str: str) -> date:
        try:
            return datetime.strptime(date_str, '%m-%d-%y').date()
        except ValueError:
            raise ValueError(f'Invalid date format: {date_str}')

    if isinstance(date_str, list):
        return [single_date(d) for d in date_str]
    return single_date(date_str)