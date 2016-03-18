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

import pyupm_ttp223 as ttp223
import pyupm_grove as grove

def checkTouchPulse(touch):
    if touch.isPressed():
        while True:
            if not touch.isPressed():
                return True
    return False

def checkButtonPulse(button):
    if button.value() != 0:
        while True:
            if button.value() == 0:
                return True
    return False

def doubleTouchPulse(touch):
    while True:
        if checkTouchPulse(touch):
            while True:
                if checkTouchPulse(touch):
                    return True
                
def displayUpdate(display, avSpaces, regSpaces):
        display.clear()
        if avSpaces > 0:
            if avSpaces >= regSpaces / 2:
                display.setColor(0, 255, 0)
            elif avSpaces >= regSpaces / 4:
                display.setColor(255, 255, 0)
            else:
                display.setColor(255, 127, 0)
                
            display.setCursor(0, 0)
            display.write("Available places:")
            display.setCursor(1, 0)
            display.write(str(avSpaces))
        else:
            display.setColor(255, 0, 0)
            display.setCursor(0, 0)
            display.write("No available")
            display.setCursor(1, 0)
            display.write("places")
