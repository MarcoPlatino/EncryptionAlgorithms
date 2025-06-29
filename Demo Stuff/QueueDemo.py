import threading
import time
import queue

# Create a queue for output
output_queue = queue.Queue()
lock = threading.Lock

def get_input():
    while True:
        
            user_input = input()  # Wait for user input
            output_queue.put(f"You typed: {user_input}")  # Put the output in the queue

# Start the input thread
input_thread = threading.Thread(target=get_input, daemon=True)
input_thread.start()

# Main loop
while True:
    # Check for output in the queue
    while not output_queue.empty():
        print(output_queue.get())  # Print messages from the queue

    print("Main program is running...")
    time.sleep(1)  # Simulate work being done
