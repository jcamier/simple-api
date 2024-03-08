# In app/models/weather_model.py
from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Float, DateTime

from app.database import Base


class WeatherData(Base):
    __tablename__ = 'historical_weather_data'

    dt = Column(Integer, primary_key=True)
    dt_iso = Column(String)
    timezone = Column(Integer)
    city_name = Column(String)
    lat = Column(Float)
    lon = Column(Float)
    temp = Column(Float)
    visibility = Column(Integer)
    dew_point = Column(Float)
    feels_like = Column(Float)
    temp_min = Column(Float)
    temp_max = Column(Float)
    pressure = Column(Integer)
    sea_level = Column(Integer, nullable=True)
    grnd_level = Column(Integer, nullable=True)
    humidity = Column(Integer)
    wind_speed = Column(Float)
    wind_deg = Column(Integer)
    wind_gust = Column(Float, nullable=True)
    rain_1h = Column(Float, nullable=True)
    rain_3h = Column(Float, nullable=True)
    snow_1h = Column(Float, nullable=True)
    snow_3h = Column(Float, nullable=True)
    clouds_all = Column(Integer)
    weather_id = Column(Integer)
    weather_main = Column(String)
    weather_description = Column(String)
    weather_icon = Column(String)


class WeatherDataSchema(BaseModel):
    dt: int
    dt_iso: str
    timezone: int
    city_name: str
    lat: float
    lon: float
    temp: float
    visibility: Optional[int] = None
    dew_point: float
    feels_like: float
    temp_min: float
    temp_max: float
    pressure: int
    sea_level: Optional[int] = None
    grnd_level: Optional[int] = None
    humidity: int
    wind_speed: float
    wind_deg: int
    wind_gust: Optional[float] = None
    rain_1h: Optional[float] = None
    rain_3h: Optional[float] = None
    snow_1h: Optional[float] = None
    snow_3h: Optional[float] = None
    clouds_all: int
    weather_id: int
    weather_main: str
    weather_description: str
    weather_icon: str

    class Config:
        from_attributes = True


class TemperatureForecastSchema(BaseModel):
    avg_temp: Optional[float] = None  # Allow None if there's no data