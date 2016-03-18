    #Copyright (C) 2016  IoT Kali

    #This program is free software; you can redistribute it and/or modify
    #it under the terms of the GNU General Public License as published by
    #the Free Software Foundation; either version 2 of the License, or
    #(at your option) any later version.

    #This program is distributed in the hope that it will be useful,
    #but WITHOUT ANY WARRANTY; without even the implied warranty of
    #MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    #GNU General Public License for more details.

    #You should have received a copy of the GNU General Public License along
    #with this program; if not, write to the Free Software Foundation, Inc.,
    #51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.


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
