public class HumiditySensorTestDouble extends HumiditySensor {
    private int reading;

    @Override
    public int measureHumidity() {
        return this.reading;
    }

    public void setNextHumidityReading(int reading) {
        this.reading = reading;
    }
}
