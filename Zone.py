import threading
import paho.mqtt.client as mqtt
import pyupm_grove as button
import pyupm_i2clcd as lcd
import pyupm_ttp223 as touch

import SensorThread
from sensors import displayUpdate

class Zone:
    def __init__(self, zoneID, regSpaces, spSpaces, outputZones, outsideInput, outsideOutput, display, host):
        self.zoneID = zoneID
        self.regSpaces = regSpaces
        self.spSpaces = spSpaces
        self.avSpaces = regSpaces
        self.display = display
        self.client = mqtt.Client(client_id=zoneID)
        self.client.connect(host)
        self.threadArr = []
        lock = threading.Lock()
        
        for e in outputZones:
            self.threadArr.append(SensorThread(self.client, e[0], e[1] + "/i", self.getID(), self.display, self.avSpaces, self.regSpaces, lock))
            
        for e in outsideInput: 
            self.threadArr.append(SensorThread(self.client, e[0], self.getID() + "/i", "add", "none", lock))
                                  
        for e in outsideOutput:
            self.threadArr.append(SensorThread(self.client, e[0], e[1], self.getID(), "add", lock))
        
    def on_connect(client, userdata, flags, rc):
        client.subscribe(self.zone  ID + "/i")
        client.subscribe(self.zoneID + "/o")
        
    def on_message(client, userdata, msg):
        if message.topic == self.zoneID + "/i":
            self.avSpaces -= 1
        else:
            self.avSpaces += 1
        self.displayUpdate()
            
    def getAvSpaces(self):
        return self.avSpaces
        
    def getRegSpaces(self):
        return self.regSpaces
    
    def getSpSpaces(self):
       return self.spSpaces

    def getID(self):
        return self.zoneID
        
    def main(self):
        sensors.updateDisplay(self.display, self.avSpaces, regSpaces)
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        for t in self.threadArr:
            t.start()
    