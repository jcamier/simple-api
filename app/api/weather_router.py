import logging
from typing import List, Optional
from datetime import datetime, timedelta

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from models.weather_model import WeatherData, WeatherDataSchema
from database import get_db

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
    # Assuming dt_iso stores dates as strings in YYYY-MM-DD format
    # Adjust your query to filter based on the calculated start_point
    weather_data = db.query(WeatherData).filter(
        WeatherData.dt_iso >= start_point.strftime('%Y-%m-%d')
    ).all()

    return weather_data