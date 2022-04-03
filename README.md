# coen446_project

## short description of entities and files

## software, libraries and tools
paho-mqtt 1.5.0 (https://pypi.org/project/paho-mqtt/)
Mosquitto 

## operating system and version

## installation steps
1. install paho-mqtt (in the terminal, type this: pip install paho-mqtt)
1. install Mosquitto broker (http://www.steves-internet-guide.com/install-mosquitto-broker/)

## information of how to compile and run the client, broker and thermostat


COMMANDS:  
[MANAGEMENT APP]  
r <name> <temp> : register <name> with preferred <temp>  
d <name> : deregister <name>  
[SMART DOOR LOCKER]  
e <name> : <name> enters room  
l <name> : <name> leaves the room  
[THERMOSTAT DISPLAY]  
p : print current temperature, registered persons, and current persons  
[CONTROLLER]  
h : help with list of commands  
exit : exit program  
