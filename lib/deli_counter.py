#!/usr/bin/env python3

katz_deli = []

def line(queue):
    if len(queue) == 0:  # Check if the queue is empty
        print("The line is currently empty.")
    else:
        # Create a string showing each person's position and name
        current_line = "The line is currently: " + " ".join([f"{i+1}. {name}" for i, name in enumerate(queue)])
        print(current_line)

def take_a_number(queue, name):
    # Add the new customer to the end of the line
    queue.append(name)
    # Call out their name and position in line
    print(f"Welcome, {name}. You are number {len(queue)} in line.")

def now_serving(queue):
    if len(queue) == 0:  # Check if the queue is empty
        print("There is nobody waiting to be served!")
    else:
        # Call out the next person in line and remove them
        print(f"Currently serving {queue.pop(0)}.")