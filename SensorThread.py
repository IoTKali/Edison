import threading
import ZoneBase
import sensors
import paho.mqtt.client as mqtt

class SensorThread(threading.Thread):
    def __init__(self, client, sensor, topic, msg, display, avSpaces, regSpaces, lock):
        threading.Thread.__init__(self)
        self.client = client
        self.sensor = sensor
        self.topic = topic
        self.msg = msg
        self.lock = lock
        self.display = display
        self.avSpaces = avSpaces
        self.regSpaces = regSpaces
        
    def main(self):
        self.lock.acquire()
        if sensors.doubleTouchPulse(self.sensor):
            self.client.publish(self.topic, self.msg)
            print self.topic + "-" + self.msg
        sensors.updateDisplay(self.display, self.avSpaces, self.regSpaces)
        self.lock.release()
        
    def run(self):
        self.main()