import sys
import time


class TrafficLight:
    __color = ""

    def running(self):
        print("Светофор включился")

        while True:
            __color = "red"
            sys.stdout.write("\r" + __color)
            sys.stdout.flush()
            time.sleep(7)

            __color = "yellow"
            sys.stdout.write("\r" + __color)
            sys.stdout.flush()
            time.sleep(2)

            __color = "green"
            sys.stdout.write("\r" + __color)
            sys.stdout.flush()
            time.sleep(10)


a = TrafficLight()
print(a.running())
