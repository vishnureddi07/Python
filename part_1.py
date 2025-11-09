import time 

def india():
    for i in range(11,21):
        time.sleep(0.5)
        print(f'India : {i}')


def usa():
    for j in range(21,31):
        time.sleep(0.5)
        print(f'USA : {j}')


india()
usa()