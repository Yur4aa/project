from csv import reader
from datetime import datetime

from domain.parking import Parking
from domain.aggregated_data import AggregatedData
from domain.accelerometer import Accelerometer
from domain.gps import Gps

class FileDatasource:
    def __init__(self, accelerometer_filename: str, gps_filename: str, parking_filename: str) -> None:
        self.accelerometer_filename = accelerometer_filename
        self.gps_filename = gps_filename
        self.parking_filename = parking_filename
        self.cache_data = {}

    def read(self) -> AggregatedData:
        data_points = ((self.cache_data["accelerometer"], "accelerometer"),
                       (self.cache_data["gps"], "gps"),
                       (self.cache_data["parking"], "parking"))
        processed_data = {}
        for values, data_type in data_points:
            processed_data[data_type] = next(reader(values))

        x, y, z = map(int, processed_data["accelerometer"])
        longitude, latitude = map(float, processed_data["gps"])

        accelerometer_obj = Accelerometer(x=x, y=y, z=z)
        gps_obj = Gps(longitude=longitude, latitude=latitude)
        parking_obj = Parking(int(processed_data["parking"][0]), gps_obj)  # Share GPS instance

        return AggregatedData(
            accelerometer=accelerometer_obj,
            gps=gps_obj,
            parking=parking_obj,
            timestamp=datetime.now()
        )

    def startReading(self, *args, **kwargs):
        self.cache_data["accelerometer"] = open(self.accelerometer_filename, 'r')
        self.cache_data["gps"] = open(self.gps_filename, 'r')
        self.cache_data["parking"] = open(self.parking_filename, 'r')

    def stopReading(self, *args, **kwargs):
        """Метод повинен викликатись для закінчення читання даних"""
        # This one is redundant for now as the reading is infinite
        pass