# importing pyinputplus libarary as co for easy of calling
import pyinputplus as co 
import time
def moving():
    while True:
        direction = co.inputChoice(["UP","DOWN"])
        # print(direction)

        print("Choose a floor: up or down")
        desired_floor = co.inputCustom()
        if desired_floor in [1, 16]:
            print(f"selected floor {desired_floor}")
        print("Invalid choice, try again.")

    time_taken = desired_floor* 0.5
    print(f"life is moving {moving_direction}")
    time.sleep(time_taken)
    print(f"Current floor is {desired_floor} gates are open")
    time.sleep(0.5)
    print("Gates closing")


# max_floor = 15
# lowest_floor = 0 
moving()






