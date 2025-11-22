import json
from time import sleep

# Task:
# Create a dictionary of:
# your robot name
# battery voltage
# motor count
# a list of sensors
# whether logging is enabled (True/False)
# Then save it as device.json.

robot_data = {
    "robot_name" : "Botxora",
    "battery_voltage" : 24.5,
    "motor_count" : 3,
    "sensor_list" : ["LiDAR 23", "MQ22", "DHT11", "PIR"],
    "logging" : True
    }

with open("device.json", "w") as file:
    json.dump(robot_data, file, indent=4)

with open("device.json", "r") as file:
    data = json.load(file)
    print(data)

print("New Robot Data Created!")


sleep(10) # pauses the code execution for 10 secs

# Task:
# Load your device.json
# Add a new key: "firmware_version": "1.0.0"
# Add "GPS" to your sensor list
# Update motor count to 4
# Save the updated file
# Print the final dictionary
# When you're done, paste the output here.

# load
with open("device.json", "r") as file:
    loaded = json.load(file)
# update   
loaded.update({"firmware_version": 1.0})
loaded["sensor_list"].append("GPS")
loaded["motor_count"] = 4
# save
with open("device.json", "w") as file:
    json.dump(loaded, file, indent=10)

print("New Robot Data Updated!!")
