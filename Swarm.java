import java.util.ArrayList;
import java.util.Timer;

public class Swarm
{
    ArrayList<Firefly> fireflies;
    public Swarm(int n) {
        for (int i = 0; i < n; i++) {
            fireflies.add(new Firefly(/*some x*/, /*some y*/));
        }
    }

    public emit() {

    }
}
