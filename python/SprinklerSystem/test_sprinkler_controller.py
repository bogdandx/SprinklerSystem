
from unittest import TestCase
from unittest import mock
from unittest.mock import MagicMock
from unittest.mock import call

from humidity_sensor import HumiditySensor
from sprinkler_controller import SprinklerController
from sprinkler_system import SprinklerSystem

class SprinklerController_test(TestCase):
    def setUp(self):
        pass

    def test_shouldWaterOnScheduleIfHumidityBelow25Percent(self):
        sprinklerSystem = MagicMock()
        humiditySensor = MagicMock()
        humiditySensor.measureHumidity.return_value = 23

        sprinklerController = SprinklerController(sprinklerSystem, humiditySensor)
        sprinklerController.runSchedule();

        sprinklerSystem.turnOn.assert_called()
        
    @mock.patch('humidity_sensor.HumiditySensor.measureHumidity')
    def test_shouldWaterOnScheduleIfHumidityBelow25Percent_using_patch(self, measureHumidityCallback):
        measureHumidityCallback.return_value = 23
        sprinklerSystem = MagicMock()

        # sensor_2 = HumiditySensor()
        # humidity_2 = sensor_2.measureHumidity()
        
        sprinklerController = SprinklerController(sprinklerSystem, HumiditySensor())
        sprinklerController.runSchedule()

        sprinklerSystem.turnOn.assert_called()
        # self.assertEqual(23, humidity_2)

    def test_shouldSkipWateringIfHumidityAbove25Percent(self):
        sprinklerSystem = MagicMock()
        humiditySensor = MagicMock()
        humiditySensor.measureHumidity.return_value = 25

        sprinklerController = SprinklerController(sprinklerSystem, humiditySensor)
        sprinklerController.runSchedule();

        sprinklerSystem.turnOn.assert_not_called()
        
    def test_canSetSensor_checks_Instance(self):
        sprinklerSystem = MagicMock()         
        humiditySensor = MagicMock()
        
        sprinklerController = SprinklerController(sprinklerSystem, humiditySensor)
        sprinklerController.setSensor(humiditySensor)
        
        sprinklerSystem.setSensor.assert_called_with(humiditySensor)
        
    def test_canSetSensors_checks_each_instance(self):
        sprinklerSystem = MagicMock()         
        humiditySensor_1 = MagicMock()
        humiditySensor_2 = MagicMock()
        
        sprinklerController = SprinklerController(sprinklerSystem, HumiditySensor())
        sprinklerController.setSensors([humiditySensor_1, humiditySensor_2])
        
        calls = [call(humiditySensor_1), call(humiditySensor_2)]
        sprinklerSystem.setSensor.assert_has_calls(calls, any_order=True)
        # calls_reverse = [call(humiditySensor_2), call(humiditySensor_1)]
        # sprinklerSystem.setSensor.assert_has_calls(calls_reverse)