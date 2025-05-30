import time

def run(args):
    if not args or not args[0].isdigit():
        print("Usage: timer <seconds>")
        return
    seconds = int(args[0])
    print(f"Timer started for {seconds} seconds...")
    time.sleep(seconds)
    print("Time's up!")