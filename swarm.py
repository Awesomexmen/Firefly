from firefly import Firefly
import random
import sched, time

class Swarm:

    def __init__(self, n, scheduler):
        self.fireflies = []
        self.scheduler = scheduler
        for i in range(n):
            for j in range(n):
                self.fireflies.append(Firefly(i, j, self.scheduler))

    def begin_flashing(self, runtime, flash_interval, flash_chance):
        for i in range(int(runtime / flash_interval)):
            for f in self.fireflies:
                if random.random() < flash_chance:
                    self.scheduler.enter(flash_interval * i, 1, self.flash_firefly, argument=[f])

    def flash_firefly(self, f):
        if not f.can_flash: return
        f.flash(random.uniform(0.2, 0.6), 1.2)
        self.emit_signal(f)

    def emit_signal(self, f):

        for fly in self.fireflies:
            flash_chance = self.get_flash_chance(f.coords, fly.coords)
            if random.random() < flash_chance:
                self.scheduler.enter(random.uniform(0.05, 0.08), 1, self.flash_firefly, argument=[fly])

    def get_flash_chance(self, origin_coords, fly_coords):

        x1 = origin_coords[0]
        y1 = origin_coords[1]
        x2 = fly_coords[0]
        y2 = fly_coords[1]
        dist = self.distance(x1, y1, x2, y2)
        return 0.85 / (1 + 2.7182818 ** (5 * (dist - 1.6)))

    def distance(self, x1, y1, x2, y2):
        return (((y2 - y1) ** 2) + ((x2 - x1) ** 2)) ** (1/2)

    def print_status(self):
        print("\n" * 50)
        n = int(len(self.fireflies) ** (1/2))
        for i in range(n):
            row = ""
            for j in range(n):
                if self.fireflies[i*n + j].flashing:
                    row += "*"
                else:
                    row += "-"
                row += "   "

            print(row + "\n" * 1)
