public class SprinklerSystemTestDouble extends SprinklerSystem {
    boolean waterTurnedOn = false;

    @Override
    public void turnOn() {
        waterTurnedOn = true;
    }

    public boolean wasWaterTurnedOn() {
        return waterTurnedOn;
    }
}
