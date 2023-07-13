import datetime
import random
from datetime import date

current_date = date.today()

# Store the last shuffled date
last_shuffled_date = None

def shuffle_logic():

    global last_shuffled_date
    # Your list
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Get the current date
    current_date = date.today()

    # Compare current date with last shuffled date
    if last_shuffled_date == None or last_shuffled_date != current_date:
        # Shuffle the list
        random.shuffle(my_list)

        # The number of list items to display
        random_list = my_list[:3]

        # Update the last shuffled date
        last_shuffled_date = current_date

        # Store the last shuffled list
        # last_shuffled_list = random_list

    # Print the shuffled or unshuffled list
        print("Current date: ", current_date)
        print("Shuffle date: ", last_shuffled_date)
        print(random_list)

    else:
        print("Same list, no shuffle")

shuffle_logic()