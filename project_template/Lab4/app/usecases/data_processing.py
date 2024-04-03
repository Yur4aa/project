from app.entities.input_data import InputData
from app.entities.agent_data import AgentData
from app.entities.processed_agent_data import ProcessedAgentData
import time


def process_agent_data(input_data: InputData) -> ProcessedAgentData:
    state = ""
    if input_data.parking.empty_count <= 21:
        state = "good"
    else:
        state = "bad"
    time.sleep(1)
    return ProcessedAgentData(road_state=state, agent_data=AgentData(
        accelerometer=input_data.accelerometer, gps=input_data.gps, timestamp=input_data.timestamp))
