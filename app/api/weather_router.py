import logging
from typing import List, Optional
from datetime import datetime, timedelta

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.models.weather_model import WeatherData, WeatherDataSchema, TemperatureForecastSchema
from app.models.utils import kelvin_to_fahrenheit, convert_dt_iso_str
from app.database import get_db

logger = logging.getLogger(__name__)

router = APIRouter()

@router.get("/weather/", response_model=List[WeatherDataSchema])
async def read_weather_data(
    days: int = 10,
    start_date: Optional[str] = None,
    db: Session = Depends(get_db)):
    """
    Fetches weather data starting from 'start_date' or the last 'days' days if start_date is not provided.
    """
    # If start_date is provided, use it; otherwise, calculate the start date as today minus 'days'
    if start_date:
        try:
            start_point = datetime.strptime(start_date, '%Y-%m-%d')
        except ValueError:
            raise HTTPException(status_code=400, detail="start_date must be in format YYYY-MM-DD")
    else:
        start_point = datetime.now() - timedelta(days=days)

    logger.debug(f"starting date is {start_point}")

    weather_data = db.query(WeatherData).filter(
        WeatherData.dt_iso >= start_point.strftime('%Y-%m-%d')
    ).all()

    converted_weather_data = []

    for record in weather_data:
        # Apply the temperature conversion to each record
        record.temp = round(kelvin_to_fahrenheit(record.temp), 1) if record.temp is not None else None
        record.feels_like = round(kelvin_to_fahrenheit(record.feels_like), 1) if record.feels_like is not None else None
        record.temp_min = round(kelvin_to_fahrenheit(record.temp_min), 1) if record.temp_min is not None else None
        record.temp_max = round(kelvin_to_fahrenheit(record.temp_max), 1) if record.temp_max is not None else None

        converted_weather_data.append(record)

    # Return the converted data
    return converted_weather_data

@router.get("/weather/forecast/", response_model=TemperatureForecastSchema)
async def read_temperature_forecast(date: Optional[str] = None, db: Session = Depends(get_db)):
    """
    Fetches average temperature for a given date across the last ten years.
    """
    if date:
        try:
            target_date = datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            raise HTTPException(status_code=400, detail="date must be in format YYYY-MM-DD")
    else:
        # Default to today's date if not provided
        target_date = datetime.now()

    # Calculate the start and end range for the day/month across ten years
    start_date = target_date.replace(year=target_date.year - 10)
    end_date = target_date.replace(year=target_date.year - 1)  # Last year

    weather_data_query = db.query(
        func.avg(WeatherData.temp).label('avg_temp')
    ).filter(
        WeatherData.dt_iso >= start_date,
        WeatherData.dt_iso <= end_date,
        WeatherData.temp.isnot(None)  # Ensure you're only considering non-NULL temperatures
    )

    avg_temp_result = weather_data_query.first()

    if avg_temp_result and avg_temp_result.avg_temp is not None:
    # Convert and round the temperature
        converted_temp = round(kelvin_to_fahrenheit(avg_temp_result.avg_temp), 1)
        forecast_response = TemperatureForecastSchema(avg_temp=converted_temp)
    else:
        forecast_response = TemperatureForecastSchema()

    return forecast_response

@router.get("/weather/icon/")
async def get_weather_icon(date: str, db: Session = Depends(get_db)):
    """
    Fetches the URL for the weather icon for a given date.
    """
    try:
        # Convert string date to datetime object
        target_date = datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        raise HTTPException(status_code=400, detail="date must be in format YYYY-MM-DD")

    # Format target_date back to string for comparison
    target_date_str = convert_dt_iso_str(date)

    weather_record = db.query(WeatherData).filter(
        WeatherData.dt_iso.startswith(target_date_str)
    ).first()

    if not weather_record or not weather_record.weather_icon:
        raise HTTPException(status_code=404, detail="Weather data not found for the specified date")

    icon_url = f"https://openweathermap.org/img/w/{weather_record.weather_icon}.png"

    return {"weather_icon": weather_record.weather_icon, "icon_url": icon_url}