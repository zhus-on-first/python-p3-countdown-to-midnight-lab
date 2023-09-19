import time

def countdown(number):
    while number >=1:
        print(f"{number} SECOND(S)!")
        number -= 1
    print("HAPPY NEW YEAR!")

def countdown_with_sleep(integer):
    while integer >=1:
        print(f"{integer} SECOND(S)!")
        integer -= 1
        time.sleep(1)
    print("HAPPY NEW YEAR!")