class TestHumiditySensor :
    humidity : int

    def setHumidity(self, humidity : int):
        self.humidity = humidity
    
    def measureHumidity(self):
        return self.humidity