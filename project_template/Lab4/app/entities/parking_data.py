from pydantic import BaseModel
from app.entities.gps_data import GpsData

class ParkingData(BaseModel):
    empty_count: float
    gps: GpsData