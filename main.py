import shlex
import paho.mqtt.client as mqtt
import time


class Person:
    def __init__(self, name, temp):
        self.name = name
        self.temperature_preference = temp


#def on_log(client, userdata, level, buf):
#    print("Log: " + buf)


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected")
    else:
        print("Connection error ", rc)


def on_disconnect(client, userdata, flags, rc=0):
    print("Disconnected")


def on_message(client, userdata, message):
    if message.topic == "house/management_app":
        if str(message.payload.decode("utf-8")) == "register":
            registered_persons.append(Person(args[1], args[2]))
            print("Registered: " + args[1])
        if str(message.payload.decode("utf-8")) == "deregister":
            for p in registered_persons:
                if p.name == args[1]:
                    registered_persons.remove(p)
                    print("Deregistered: " + args[1])
                    return
            print("Unable to find: " + args[1])
    if message.topic == "house/smart_door_locker":
        if str(message.payload.decode("utf-8")) == "enter":
            for p in registered_persons:
                if p.name == args[1]:
                    current_persons.append(p)
                    client.publish("house/thermostat", "update")
                    print("Entered house: " + args[1])
                    return
            print("Unable to find: " + args[1])
        if str(message.payload.decode("utf-8")) == "leave":
            for p in registered_persons:
                if p.name == args[1]:
                    current_persons.remove(p)
                    client.publish("house/thermostat", "update")
                    print("Left house: " + args[1])
                    return
            print("Unable to find: " + args[1])
    if message.topic == "house/thermostat":
        print_temperature()


def print_temperature():
    if len(current_persons) == 0:
        current_temperature = 15
    elif len(current_persons) > 0:
        avg_sum = 0
        for p in current_persons:
            avg_sum += int(p.temperature_preference)
        current_temperature = avg_sum / len(current_persons)
    print("TEMPERATURE: " + str(current_temperature))


def print_commands():
    print("COMMANDS: ")
    print("[MANAGEMENT APP]")
    print("r <name> <temp> : register <name> with preferred <temp>")
    print("d <name> : deregister <name>")
    print("[SMART DOOR LOCKER]")
    print("e <name> : <name> enters room")
    print("l <name> : <name> leaves the room")
    print("[THERMOSTAT DISPLAY]")
    print("p : print current temperature, registered persons, and current persons")
    print("[CONTROLLER]")
    print("h : help with list of commands")
    print("exit : exit program")


def print_registered_persons():
    print("REGISTERED PERSONS")
    for p in registered_persons:
        print("> " + p.name + ": " + p.temperature_preference)


def print_current_persons():
    print("CURRENT PERSONS")
    for p in current_persons:
        print("> " + p.name + ": " + p.temperature_preference)


# global variables
registered_persons = []
current_persons = []

# set up mqtt client
broker_url = "test.mosquitto.org"
print("Creating new instance")
client = mqtt.Client("Temperature")
client.on_connect = on_connect
#client.on_log = on_log
client.on_message = on_message

# connect to broker
print("Connecting to broker")
client.connect(broker_url)
client.loop_start()

# subscribe to topics
client.subscribe("house/management_app")
client.subscribe("house/smart_door_locker")
client.subscribe("house/thermostat")

# infinite loop
while 1:
    try:
        # delay
        time.sleep(1)

        # user input command
        print("=================")
        command = input("Type command: ")
        print("=================")
        args = shlex.split(command)
        # empty input case
        if len(args) == 0:
            print_commands()
            continue

        # simulate register person on app
        if args[0] == "r" and len(args) == 3:
            client.publish("house/management_app", "register")
        # simulate deregister person on app
        elif args[0] == "d" and len(args) == 2:
            client.publish("house/management_app", "deregister")
        # simulate person entering room
        elif args[0] == "e" and len(args) == 2:
            client.publish("house/smart_door_locker", "enter")
        # simulate person leaving room
        elif args[0] == "l" and len(args) == 2:
            client.publish("house/smart_door_locker", "leave")
        # print room temperature
        elif args[0] == "p" and len(args) == 1:
            print_temperature()
            print_registered_persons()
            print_current_persons()
        elif args[0] == "h" and len(args) == 1:
            print_commands()
        # exit loop
        elif args[0] == "exit" and len(args) == 1:
            break
        # invalid input argument
        else:
            print_commands()
    except:
        print("Error")

client.loop_stop()
client.disconnect()
