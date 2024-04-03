from datetime import datetime
from pydantic import BaseModel
from app.entities.accelerometer_data import AccelerometerData
from app.entities.gps_data import GpsData

class AgentData(BaseModel):
    accelerometer: AccelerometerData
    gps: GpsData
    timestamp: datetime
