import cv2
from keras.models import load_model
import numpy as np
import random
model = load_model("keras_model.h5")
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

while True: 
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    cv2.imshow('frame', frame)

    # finds the index of the maximum value in the prediction array and based on that determines the player choice
    max = np.argmax(prediction)
    if max == 0:
        player_choice = "Rock"
    elif max == 1:
        player_choice = "Paper"
    elif max == 2: 
        player_choice = "Scissors"
    else:
        player_choice = "None"
    print(player_choice)

    #set a timer for this while loop to end and whatever the player input is at the end is the player input
    #take the final prediction and find the index of the max value to decide what the player input is
    #in a different method make a random choice for the computer and compare with the player choice

    #if
    # #computer makes a random choice
    # rps = ["rock", "paper", "scissors"]
    # comp_choice = random.choice(rps)

    # #asking player for input
    # player_choice = input("Make a choice")
    

    # Press q to close the window
    #print(prediction)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
            
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()
