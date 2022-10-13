public class SprinklersController {
    private SprinklerSystem sprinklerSystem;
    private HumiditySensor sensor;

    public SprinklersController(SprinklerSystem sprinklerSystem, HumiditySensor sensor) {
        this.sprinklerSystem = sprinklerSystem;
        this.sensor = sensor;
    }

    public void runSchedule() {
        int humidity = sensor.measureHumidity();

        if (humidity < 25) {
            this.sprinklerSystem.turnOn();
        }
    }
}
