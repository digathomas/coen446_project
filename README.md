# coen446_project

## Plan

Follow MQTT protocol through
paho mqtt client
mosquito broker

simulate arrivals and departures

input functions:
- e <name> <prefered_temperature>: <name> enters the house with <prefered_temperature>
- l <name>: <name> leaves the house
- p: print the temperature of the house
	if house empty: 15 deg C
	if 1 person: prefered_temperature of that person
	if +1 person: avg_prefered_temperature

*run "t" on each function