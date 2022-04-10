# coen446_project

## Short description of entities and files
* file main.py -> contains the entire simulated house smart heating/cooling system, including the management app, the smart door locker, the MQTT broker, and the thermostat.  

1. Management App: Keeps track of users that have been registered/unregistered from the system by storing the name and preferred temperature of them. Publishes new and updated information to the MQTT broker.  
1. Smart Door Locker: Keeps track of registered users that are currently in the house (entered/left). Publishes new and updated information to the MQTT broker.  
1. MQTT Broker: Manages MQTT protocol publish and subscribe on different topics for each separate entity.  
1. Thermostat: Calculates the preferred house temperature based on the status in the house. After running the algorithm, displays the house temperature on the terminal. Is subscribed to the broker on topics related to new information varying the variables to calculate the temperature of the house.  

* class Person -> represents a person which has a unique name and an associated preferred temperature.  
* infinite loop -> represents a controller unit where each separate entity can be controlled from the terminal.  

## Software, libraries and tools
* Python 3.7.9 Anaconda 3 (https://www.anaconda.com/products/distribution)  
* Pycharm 2020.1.5 Professional Edition (https://www.jetbrains.com/pycharm/download/#section=windows)  
* Paho-mqtt 1.5.0 (https://pypi.org/project/paho-mqtt/)  
* Mosquitto V2 (http://www.steves-internet-guide.com/download/6-bit-mosquitto-v2/)  

## Operating system and version
* Microsoft Windows 10 Pro 10.0.19044 Build 19044

## Installation steps
1. Install Pycharm (https://www.jetbrains.com/pycharm/download/#section=windows)  
1. Install Python (https://www.anaconda.com/products/distribution)  
1. Open the project with Pycharm and set run configuration with Python interpreter (https://github.com/digathomas/coen446_project)  
1. Install Paho-mqtt (in the terminal, type this: pip install paho-mqtt)
1. Install Mosquitto broker (http://www.steves-internet-guide.com/install-mosquitto-broker/)

## Information of how to compile and run the client, broker and thermostat
Compilation happens at runtime due to the project being a python project.  
1. Set run configuration with the installed Python interpreter.
1. Run main.py, all entities will run with this file.  

## User guide
1. See all available commands with 'h'.  
1. Register users to the management app beforehand with 'r'.  
1. Deregister users from the management app with 'd'.
1. Check for the thermostat current temperature with 'p'. Additionally, the current list of registered and persons in the house will be printed.  
1. Simulate users entering and leaving the house with 'e' and 'l'.  
1. Recheck for the new thermostat current temperature with 'p'.  
1. Exit the program with 'exit'.  

### Run commands through the terminal:  
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

## Uninstallation steps
Since pip installs globally, uninstall packages after running the program.  
1. Uninstall Paho-mqtt (in the terminal, type: pip uninstall paho-mqtt)  
1. Uninstall Mosquitto broker (run uninstall.exe ![image](https://user-images.githubusercontent.com/77941062/162345588-695fb34e-0ddc-4948-a0ea-1e8a2afd9331.png))  