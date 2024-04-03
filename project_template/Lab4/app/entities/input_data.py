from datetime import datetime
from pydantic import BaseModel, field_validator
from app.entities.accelerometer_data import AccelerometerData
from app.entities.gps_data import GpsData
from app.entities.parking_data import ParkingData

class InputData(BaseModel):
    accelerometer: AccelerometerData
    gps: GpsData
    parking: ParkingData
    timestamp: datetime

    @classmethod
    @field_validator("timestamp", mode="before")
    def parse_timestamp(cls, value):
        if isinstance(value, datetime):
            return value
        try:
            return datetime.fromisoformat(value)
        except (TypeError, ValueError):
            raise ValueError("Invalid timestamp format. Expected ISO 8601 format (YYYY-MM-DDTHH:MM:SSZ).")
