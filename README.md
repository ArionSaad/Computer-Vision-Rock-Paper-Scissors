# Computer-Vision-Rock-Paper-Scissors

> This project is about creating the game Rock Paper Scissors which can be played against the computer using a webcam.

## Milestone 1

- Using Teachable Machine a model was created that recognizes the player holding a rock, paper or scissors shape with their hand. This involved taking 50 - 100 pictures of holding those shapes.
- This model will be used to detect the player input using a webcam. 

![Screenshot from 2022-03-30 19-23-19](https://user-images.githubusercontent.com/101988764/160904921-a8f230a0-e709-4d0c-b2fa-2c4a2fe5c13a.png)

## Mileston 2

- Created a new conda environment and installed the following libraries; opencv-python, tensorflow and ipykernel. This environment is using Python 3.8 and is called RPS_env.

- The following code is used to run the code on the local machine: 

```python
import cv2
from keras.models import load_model
import numpy as np
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
    # Press q to close the window
    print(prediction)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
            
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()
```

## Milestone 3

- The user is asked to input one of the three options and the computer makes a random choice. Based on these two choices, if-else conditions are used to determine who won. This is wrapped up in a function.

```python
def game():
    while True:
        #computer making a choice
        rps = ["rock", "paper", "scissors"]
        comp_choice = random.choice(rps)
        #asking player for input
        player_choice = input("Make a choice")
        #determining who the winner is
        if player_choice == "rock" and comp_choice == "rock":
            print("Draw")
        elif player_choice == "paper" and comp_choice == "rock":
            print("Win")
        elif player_choice == "scissors" and comp_choice == "rock":
            print("Lose")
        elif player_choice == "rock" and comp_choice == "paper":
            print("Lose")
        elif player_choice == "paper" and comp_choice == "paper":
            print("Draw")
        elif player_choice == "scissors" and comp_choice == "paper":
            print("Win")
        elif player_choice == "rock" and comp_choice == "scissors":
            print("Win")
        elif player_choice == "paper" and comp_choice == "scissors":
            print("Lose")
        elif player_choice == "scissors" and comp_choice == "scissors":
            print("Draw")
        else:
            print("Not Valid input")
```
![Screenshot from 2022-03-30 21-10-27](https://user-images.githubusercontent.com/101988764/160922301-13a2c539-aeb0-44f3-bb9e-eff3da97c372.png)

## Milestone 4

- The code used in milestone 2 produced a prediction based on what the camera is picking up. The prediction variable is an array of 4 numbers indicating the possibility of the camera input corresponding to either rock, paper, scissors or nothing. 
- By taking the index of the highest number in the array, it can be determined wether the camera input is one of the 4 options listed above. This is the code used:
```python
max = np.argmax(prediction)
    if max == 0:
        player_choice = "rock"
    elif max == 1:
        player_choice = "paper"
    elif max == 2: 
        player_choice = "scissors"
    else:
        player_choice = "None"
```

- The game method is modified to take the player_choice input and is called directly from the while loop. This produces a list of player choices and win/loss/draw conditions.

![Screenshot from 2022-03-31 19-08-00](https://user-images.githubusercontent.com/101988764/161121558-4a02d0a9-5df1-44cd-967d-fdef68cba5be.png)

- Timer is created using the time.time() method. After an established period of time the while loop takes the camera input and runs the game method. A counter is set up to count the number of wins between the player and the computer and the game ends on either gets 3 wins.

![Screenshot from 2022-03-31 20-33-10](https://user-images.githubusercontent.com/101988764/161134888-a33336a0-b978-47c0-b688-b9ee059a5a1a.png)

- Added a feature where the programme keeps track of what the player chose previously and based on that will make future choices. This increases the difficulty of the game as the player will now need to varry their inputs or they will lose to the computer. 

```python
def ego(player_choice):
    list_player_choice.append(player_choice)
    rps = ["rock", "paper", "scissors"]
    comp_choice = random.choice(rps)
    if len(list_player_choice) >= 2:
        player_bias = max(list_player_choice, key=list_player_choice.count)
        if player_bias == "rock":
            comp_choice = "paper"
        elif player_bias == "paper":
            comp_choice = "scissors"
        elif player_bias == "scissors":
            comp_choice = "rock"
        elif player_bias == "none":
            rps = ["rock", "paper", "scissors"]
            comp_choice = random.choice(rps)
    game(player_choice, comp_choice)
```

![Screenshot from 2022-04-04 19-00-35](https://user-images.githubusercontent.com/101988764/161603923-3caceb76-956c-4849-a190-ab4f4e1f45b4.png)


## Conclusion

- UI is one area where the game is lacking. Easier visibility of the timer and the wins or losses would make the game more readable. 
- Could be possible to build an entire database of player inputs from multiple games and based on that the computer tries to predict what the player will choose next.






