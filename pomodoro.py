
from os import system
from pygame import mixer
import time

MINIMAL = {"work_time": 10, "pause_time": 1,
           "long_pause_time": 10, "cycles": 4}
STANDARD = {"work_time": 25, "pause_time": 5,
            "long_pause_time": 15, "cycles": 4}
MAXIMUM = {"work_time": 45, "pause_time": 15,
           "long_pause_time": 30, "cycles": 4}
METOTHOD5217 = {"work_time": 52, "pause_time": 17,
                "long_pause_time": 17, "cycles": 4}


def clear():
    system("cls")


def pause():
    system("pause")


def choice_method():
    clear()

    choices = ["1. Minimal", "2. Standard",
               "3. Maximum", "4. 5217 Method", "5. Custom", "0. Exit"]
    print("Choose your pomodoro:")
    for i in choices:
        print(i)
    try:
        choice = int(input("Your choice: "))
        if choice == 1:
            return MINIMAL
        elif choice == 2:
            return STANDARD
        elif choice == 3:
            return MAXIMUM
        elif choice == 4:
            return METOTHOD5217
        elif choice == len(choices)-1:
            clear()
            work_time = int(input("Work time (minutes): "))
            pause_time = int(input("Pause time (minutes): "))
            long_pause_time = int(input("Long pause time (minutes): "))
            cycles = int(input("Number of cycles: "))
            return {"work_time": work_time, "pause_time": pause_time, "long_pause_time": long_pause_time, "cycles": cycles}
        elif choice == 0:
            exit()
        else:
            raise ValueError
    except ValueError:
        clear()
        print("Wrong choice")
        pause()
        return choice_method()
    except KeyboardInterrupt:
        exit()
    except EOFError:
        exit()


def music(song):
    mixer.init()
    mixer.music.load(f'audio/{song}.mp3')
    mixer.music.play()


def pomodoro(choice):
    for i in range(choice["cycles"]):
        print("Work for {} minutes".format(choice["work_time"]))
        music("work")
        clock(choice["work_time"], "Work")
        if i == choice["cycles"] - 1:
            print("Long pause for {} minutes".format(
                choice["long_pause_time"]))
            music("long")
            clock(choice["long_pause_time"], "Long pause")
        else:
            print("Pause for {} minutes".format(choice["pause_time"]))
            music("short")
            clock(choice["pause_time"], "Pause")


def clock(minutes, stage):
    now = time.time()
    after = now + (minutes * 60)
    now = time.strftime("%H:%M:%S", time.localtime(now))
    after = time.strftime("%H:%M:%S", time.localtime(after))
    print(f"{stage} started at {now}")
    print(f"{stage} ends at {after}")
    while True:
        now = time.time()
        now = time.strftime("%H:%M:%S", time.localtime(now))
        if now == after:
            clear()
            break
    


def main():

    clear()
    choice = choice_method()
    clear()
    try:
        pomodoro(choice)
    except KeyboardInterrupt:
        return main()
    


main()
