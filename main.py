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

import Zone
import pyupm_grove as grove
import pyupm_i2clcd as lcd
import pyupm_ttp223 as touch

zoneID = "zone_1"
outputZones = [(touch.TTP22(4), "zone_2")] #Arrays of tuples: first element in touple is a sensor, second one the topic address
outsideInput = [(touch.TTP(5), zoneID)]    #
outsideOutput = []                         #
display = lcd.Jhd1313m1(0, 0x3E, 0x62)
host = "10.43.28.194"

myZone = Zone(zoneID, 17, 5, outputZones, outsideInput, outsideOutput, display, host) #Default constructor
myZone.main() #Runs infinitely until manually stopped
