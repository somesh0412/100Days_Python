# Function to turn the robot right by turning left three times
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Main loop to navigate through the maze
while not at_goal():
    # Check if the path to the right is clear
    if right_is_clear():
        # Turn right and move forward
        turn_right()
        move()
        # If the path to the right is not clear, check if the path in front is clear
    elif front_is_clear():
        # Move forward if the path is clear
        move()
    else:
        turn_left()
      