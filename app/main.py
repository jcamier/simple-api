import os
from pathlib import Path
import logging

from fastapi import FastAPI

from api.weather_router import router as weather_router

# Environment and path configurations
BASE_DIR = Path(__file__).resolve().parent.parent
DEBUG = bool(int(os.environ.get('DEBUG', 0)))
VERSION = os.environ.get("VERSION")

# Logging configurations
LOG_DIR = BASE_DIR / "logs"
LOG_FILE_NAME = os.environ.get("LOG_FILE_NAME", "api.log")
LOG_FILE_PATH = LOG_DIR / LOG_FILE_NAME

# Convert log level from string to actual logging level
LOG_LEVEL = os.environ.get("LOG_LEVEL", "DEBUG").upper()
numeric_level = getattr(logging, LOG_LEVEL, None)
if not isinstance(numeric_level, int):
    raise ValueError(f'Invalid log level: {LOG_LEVEL}')

# Configure logging
logging.basicConfig(filename=LOG_FILE_PATH if not DEBUG else None,
                    format=os.environ.get("LOG_FORMAT", "%(asctime)s::%(levelname)s::%(message)s"),
                    level=numeric_level)

logger = logging.getLogger(__name__)
logger.info(f"Starting app with DEBUG={DEBUG}")

app = FastAPI()

# Include the router
app.include_router(weather_router)

@app.get("/")
async def root():
    return {"message": f"Hello World Weather API - Version: {VERSION}"}
