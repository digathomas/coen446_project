import shlex


class Person:
    def __init__(self, name, temp):
        self.name = name
        self.temperature_preference = temp


# global variables
current_persons = []
current_temperature = 15

while 1:
    # user input command
    command = input("type command...\n")
    print("command: " + command)
    args = shlex.split(command)

    # simulate person entering room
    if args[0] == "e":
        current_persons.append(Person(args[1], args[2]))
        avg_sum = 0
        for p in current_persons:
            avg_sum += int(p.temperature_preference)
        current_temperature = avg_sum / len(current_persons)
        print("temperature: " + str(current_temperature))
    # simulate person leaving room
    elif args[0] == "l":
        current_persons.remove(Person(args[1], args[2]))
        if len(current_persons) == 0:
            current_temperature = 15
        elif len(current_persons) > 0:
            avg_sum = 0
            for p in current_persons:
                avg_sum += int(p.temperature_preference)
            current_temperature = avg_sum / len(current_persons)
        print("temperature: " + str(current_temperature))
    # print room temperature
    elif args[0] == "p":
        print("temperature: " + str(current_temperature))
    else:
        print("invalid command\n")


"""
Follow MQTT protocol through
paho mqtt client
mosquito broker
"""