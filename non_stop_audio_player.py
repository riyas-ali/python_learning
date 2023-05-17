from playsound import playsound
import os, time


def play():
    playsound("https://file-examples.com/storage/fea9880a616463cab9f1575/2017/11/file_example_WAV_1MG.wav")
    while True:
        # Start taking user input and doing something with it
        stop_playback = int(input("Press 2 anytime to stop playback and go back to the menu: "))
        if stop_playback == 2:
            return
        else:
            continue


while True:
    # clear the screen
    os.system("clear")
    print("MyPOD Music Player")
    time.sleep(1)
    # Show the menu
    print("Press 1 to Play")
    time.sleep(1)
    print("Press 2 to Exit")
    time.sleep(1)
    print("Press anything else to see the meny again")
    # take user's input
    user_input = int(input())
    # check whether you should call the play() subroutine depending on user's input
    if user_input == 1:
        print("Playing some proper tunes!")
        play()
    elif user_input == 2:
        exit()
    else:
        continue
