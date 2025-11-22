# Simulating sensor readings saved in binary format
senseo_reading = [23, 45, 12, 99, 18]  # pretend this is sensor data

with open("sensor_log.bin", "wb") as file:
    for r in senseo_reading:
        file.write(bytes([r]))   # store each reading as a single byte

# Read back from the end
with open("sensor_log.bin", "rb") as file:
    print("File size:", file.seek(0, 2))   # go to end, print size

    # Read the last 2 senseo_reading
    file.seek(-2, 2)   # move cursor 2 bytes back from the end
    last_two = file.read()

    print("Last 2 raw bytes:", last_two) #encoded format
    print("Last 2 senseo_reading:", list(last_two))
