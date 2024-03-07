from datetime import datetime

from fastapi import HTTPException


def kelvin_to_fahrenheit(kelvin: float) -> float:
    return (kelvin - 273.15) * 9/5 + 32

def convert_dt_iso_str(date_str: str, fmt: str = '%Y-%m-%d') -> str:
    """
    Validates a date string and returns it in the specified format.

    Args:
        date_str (str): The date string to validate and convert.
        fmt (str, optional): The format to return the date string in. Defaults to '%Y-%m-%d'.

    Returns:
        str: The date string in the specified format.

    Raises:
        HTTPException: If the date string is invalid or cannot be parsed.
    """
    try:
        # Convert string date to datetime object to ensure valid date format
        date_obj = datetime.strptime(date_str, fmt)
    except ValueError:
        raise HTTPException(status_code=400, detail=f"date must be in format {fmt}")

    # Format the date object back to string for comparison or use
    formatted_date_str = date_obj.strftime(fmt)

    return formatted_date_str