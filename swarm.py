import 'firefly'
import random
import sched, time

class Swarm:

    def __init__(self, n):
        self.fireflies = []
        self.scheduler = sched.scheduler(time.time, time.sleep)
        for i in range(n):
            for j in range(n):
                self.fireflies.append(Firefly(i, j))

    def begin_flashing(runtime, flash_interval, flash_chance):
        for i in range(runtime / flash_interval):
            for f in fireflies:
                if random.random() < flash_chance:
                    self.scheduler.enter(flash_interval * i, 1, lambda: self.flash_firefly(f))

        self.scheduler.run()

    def flash_firefly(f):
        f.flash(1, 3)
        self.emit_signal(f)

    def emit_signal(f):

        for fly in self.fireflies:
            flash_chance = get_flash_chance(f.coords, fly.coords)
            if random.random() < flash_chance:
                self.scheduler.enter(random.randrange(0.1, 0.2), 1, lambda: fly.flash(1, 3))

    def get_flash_chance(origin_coords, fly_coords):

        x1 = origin_coords[0]
        y1 = origin_coords[1]
        x2 = fly_coords[0]
        y2 = fly_coords[1]
        dist = self.distance(x1, y1, x2, y2)
        return 1 / (dist + (1/9))

    def distance(x1, y1, x2, y2):
        return (((x2 - x1) ** 2) + (y2 - y1) ** 2) ** (1/2)
