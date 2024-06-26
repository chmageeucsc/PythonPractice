''' https://www.fesliyanstudios.com/royalty-free-sound-effects-download/spells-and-power-ups-217
    (Video Game Secret Sound C1 Slowest Sound Effect)
'''

from playsound import playsound
import time

CLEAR = "\033[23"
CLEAR_AND_RETURN = "\033[H"

def alarm(seconds):
    time_elapsed = 0

    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        print(f"{CLEAR_AND_RETURN}Alarm will sound in: \n{minutes_left:02d}:{seconds_left:02d}")

    playsound("guitar.mp3")

minutes = int(input("How many minutes: "))
seconds = int(input("How many seconds: "))
total_seconds = minutes * 60 + seconds

alarm(total_seconds)
