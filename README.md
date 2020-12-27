# <img src="https://raw.githack.com/FortAwesome/Font-Awesome/master/svgs/solid/tachometer-alt.svg" card_color="#D81159" width="50" height="50" style="vertical-align:bottom"/> Wiolink Wionode Voice
The skill allows for voice commands to retrieve sensor data from and send commands to grove devices that are connect to wifi enabled wiolink and wionode modules.

## About
Wio link, from seeedstudios, is "an esp8266 based open-source wi-fi development board meant to greatly simplify the creation of iot applications by virtualizing plug-n-play modules to restful apis with mobile apps."

seeedstudios has defined a new way to create iot applications. no hardware programming. no breadboard. no jumper wires. no soldering. 3 steps. 5 minutes. build your own iot applications. the wifi connected wiolink boards, described here, https://www.seeedstudio.com/wio-link.html,  provided 6 grove connectors, 3 are digital ports and the other 3 are an analog, uart, and i2c port. seeedstudios and other vendor sell a wide variety of grove devices such as sensors, displays, relays, leds. servos, etc that can be plugged into one of the compatible grove connectors on the wio link board.  you download the wio app to your phone open it and create an account. then drag and drop your choice of grove devices to the connector on on board. the app will only allow connection of a device to a compatible port. the you plug the devices into the selected connectors on board, power up the board, and enter your wifi ssdi and password and the app will flash the drivers to the board. now your board is connected to a server. a sample project demostarting that proceess is availbale at this link, http://iot.seeed.cc/. the phone app allows simple interaction such  get sensor data with a push of a button. the devices are now also accescible with http curl command get and put as well as a wio client app running in python. for this skill i will provide the python coded to read and send data and commands to/from sensors uisng mycroft voice and terminal inputs.

## Examples
* "What is the humidity"
* "What is the temperature"
* "What is the barometric pressure"
* "What is the altitude"
* "What is the air quality"
* "Read all sensors"

## Credits
Gary J. Wozniak

## Category
**IoT**
Wiolink voice control

## Tags
#Iot
#Home automation
#Environmetal monitoring

