import org.example.Main;
import org.junit.Assert;
import org.junit.Test;

public class WebLoginTest {



    @Test
    public void testAddition() {
        Main main = new Main();
        int result  = main.add(10,20);
        Assert.assertNotNull(result);
        Assert.assertEquals(30, result);
    }
}
