import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

import static org.mockito.Mockito.*;

public class SprinklersControllerTests {

    private HumiditySensorTestDouble sensor;
    private SprinklerSystemTestDouble sprinklerSystem;
    private SprinklersController sprinklersController;

    @Before
    public void setUp(){
      //  sensor = mock(HumiditySensor.class);
        sensor = new HumiditySensorTestDouble();
      //  sprinklerSystem = mock(SprinklerSystem.class);
        sprinklerSystem = new SprinklerSystemTestDouble();
        sprinklersController = new SprinklersController(sprinklerSystem, sensor);
    }

    @Test
    public void shouldWaterOnScheduleIfHumidityBelow25Percent(){
      //  when(sensor.measureHumidity()).thenReturn(23);
        sensor.setNextHumidityReading(23);

        sprinklersController.runSchedule();

        sprinklerSystem.wasWaterTurnedOn();
        //verify(sprinklerSystem).turnOn();
    }

    @Test
    public void shouldSkipWateringIfHumidityAbove25Percent(){
        sensor.setNextHumidityReading(26);
        //when(sensor.measureHumidity()).thenReturn(26);

        sprinklersController.runSchedule();

        Assert.assertFalse(sprinklerSystem.waterTurnedOn);
       // verify(sprinklerSystem, never()).turnOn();
    }
}
