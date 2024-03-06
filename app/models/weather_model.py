# In app/models/weather_model.py
from sqlalchemy import Column, Integer, String, Float, DateTime
from database import Base

class WeatherData(Base):
    __tablename__ = 'weather_data'

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
