import sched, time

class Firefly:

    def __init__(self, x, y):
        self.coords = (x, y)
        self.flashing = False
        self.can_flash = True
        self.scheduler = sched.scheduler(time.time, time.sleep)

    def flash(self, timeout, cooldown):
        if not self.can_flash: return
        self.can_flash = False
        self.flashing = True
        self.scheduler.enter(timeout, 1, lambda: self.flashing = False)
        self.scheduler.enter(cooldown, 1, lambda: self.can_flash = True)
        self.scheduler.run()

# def print_time():
#     print(int(time.time()))
#
# s = sched.scheduler(time.time, time.sleep)
# print(int(time.time()))
# for i in range(1, 10):
#     s.enter(i * 2, 1, print_time)
#
# s.run()
