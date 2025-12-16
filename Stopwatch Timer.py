import time

def stopwatch():
    print("----- STOPWATCH -----")
    print("Commands:")
    print("start - Start stopwatch")
    print("stop  - Stop stopwatch")
    print("reset - Reset stopwatch")
    print("exit  - Exit program\n")

    start_time = None
    elapsed_time = 0
    running = False

    while True:
        command = input("Enter command: ").lower()

        if command == "start":
            if not running:
                start_time = time.time()
                running = True
                print("⏱ Stopwatch started")
            else:
                print("Stopwatch already running")

        elif command == "stop":
            if running:
                elapsed_time += time.time() - start_time
                running = False
                print(f"⏸ Stopwatch stopped at {elapsed_time:.2f} seconds")
            else:
                print("Stopwatch not running")

        elif command == "reset":
            start_time = None
            elapsed_time = 0
            running = False
            print("🔄 Stopwatch reset")

        elif command == "exit":
            print("Goodbye! 👋")
            break

        else:
            print("Invalid command")

stopwatch()
