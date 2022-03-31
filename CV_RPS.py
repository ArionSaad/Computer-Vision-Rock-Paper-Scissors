import cv2
from keras.models import load_model
import numpy as np
import random
import time
model = load_model("keras_model.h5")
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
it_takes = 3
player_wins = 0
computer_wins = 0

#function that defines the game
def game(player_choice):
    #computer making a choice
    rps = ["rock", "paper", "scissors"]
    comp_choice = random.choice(rps)
    print(f'Computer chose {comp_choice}')
    global player_wins
    global computer_wins
    #determining who the winner is
    if player_choice == "rock" and comp_choice == "rock":
        print("Draw")
    elif player_choice == "paper" and comp_choice == "rock":
        print("Win")
        player_wins += 1
    elif player_choice == "scissors" and comp_choice == "rock":
        print("Lose")
        computer_wins += 1
    elif player_choice == "rock" and comp_choice == "paper":
        print("Lose")
        computer_wins += 1
    elif player_choice == "paper" and comp_choice == "paper":
        print("Draw")
    elif player_choice == "scissors" and comp_choice == "paper":
        print("Win")
        player_wins += 1
    elif player_choice == "rock" and comp_choice == "scissors":
        print("Win")
        player_wins += 1
    elif player_choice == "paper" and comp_choice == "scissors":
        print("Lose")
        computer_wins += 1
    elif player_choice == "scissors" and comp_choice == "scissors":
        print("Draw")
    else:
        print("Not Valid input")
    print(f'{player_wins} - {computer_wins}')
    game_while()



def game_while ():
    begin_time = time.time()
    while True: 
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        cv2.imshow('frame', frame)

        

        #ending the game after set number of player wins
        global player_wins
        global computer_wins
        if player_wins == 3 or computer_wins == 3:
            break

        # creating a timer
        
        current_time = time.time()
        elapsed_time = current_time - begin_time

        if elapsed_time > it_takes:
            # finds the index of the maximum value in the prediction array and based on that determines the player choice
            max = np.argmax(prediction)
            if max == 0:
                player_choice = "rock"
            elif max == 1:
                player_choice = "paper"
            elif max == 2: 
                player_choice = "scissors"
            else:
                player_choice = "None"
            print(f"You chose {player_choice}")
            #calls the game function with the player choice
            game(player_choice)
            break

        #set a timer for this while loop to end and whatever the player input is at the end is the player input
        #take the final prediction and find the index of the max value to decide what the player input is
        #in a different method make a random choice for the computer and compare with the player choice

        
        

        # Press q to close the window
        #print(prediction)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            
            break


game_while()

if player_wins == 3:
    print("Good job beating the machine")
elif computer_wins == 3:
    print("Tough luck, try next time")
else:
    print("Qutting already?!")

# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()






