from humidity_sensor import HumiditySensor
from sprinkler_system import SprinklerSystem

class SprinklerController:

    def __init__(self, sprinklerSystem : SprinklerSystem, humiditySensor : HumiditySensor) -> None:
        self.sprinklerSystem = sprinklerSystem
        self.humiditySensor = humiditySensor

    def runSchedule(self):
        humidity = self.humiditySensor.measureHumidity()

        if humidity <25:
            self.sprinklerSystem.turnOn()
            
    def setSensor(self, sensor : HumiditySensor):
      self.sprinklerSystem.setSensor(sensor)
      
    def setSensors(self, sensors : list):
    #   self.sprinklerSystem.setSensor(sensors[0])
    #   self.sprinklerSystem.setSensor(sensors[1])
      
      for sensor in sensors:
          self.sprinklerSystem.setSensor(sensor)
