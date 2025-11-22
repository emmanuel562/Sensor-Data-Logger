from random import uniform
from time import sleep, strftime


with open("demo.txt", "a") as file:
    file.write("===================================================================\n")
    start_time = strftime("%Y - %m - %d / %I:%M:%S %p") #stamp the start time of experiment
    file.write(f"New Temperature Logging(Celcius) | {start_time}\n")
    file.write("===================================================================\n")
    file.write("\n")

    for plot in range(10):
        temp = round(uniform(23, 35), 2) # rounds a randomly generated reading to 2 dec places
        time_stamp = strftime("%I:%M:%S %p") #reads time of generation
        file.write(f"{time_stamp}  | {temp} *Celcius\n") # writes time of reading and temp. reading
        sleep(1)
    file.write("\n") 


print("🤖 10 seconds timeframe complete ✅")
