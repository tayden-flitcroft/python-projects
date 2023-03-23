import time
import threading

def print_time():
      while not stop_event.is_set():
          print(f"\rElapsed time: {round(time.time() - start_time, 2)} seconds", end="")
          time.sleep(0.1)

input("Press ENTER to start the stopwatch\nPress ENTER to record a lap time\nType 'r' and press ENTER to reset the stopwatch\nand, press CTRL + C to stop")
start_time = time.time()
last_time = start_time
lap_num = 1
print("Stopwatch started...")

stop_event = threading.Event()
t = threading.Thread(target=print_time)
t.start()

while True:
    try:
        user_input = input()
        if user_input.lower() == 'r':
            start_time = time.time()
            last_time = start_time
            lap_num = 1
            print("\rStopwatch reset...")
        else:
            lap_time = round(time.time() - last_time, 2)
            total_time = round(time.time() - start_time, 2)
            print(f"\rLap #{lap_num}: {total_time} ({lap_time})")
            lap_num += 1
            last_time = time.time()
    except KeyboardInterrupt:
        stop_event.set()
        t.join()
        print("\nStopwatch stopped...")
        end_time = time.time()
        print("The total time: ", round(end_time - start_time, 2), "seconds")
        break