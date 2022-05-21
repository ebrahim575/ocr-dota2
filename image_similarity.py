import time
import pyautogui
from playsound import playsound

def box_checker(loc):
    if 1110 <= loc[0] <= 1120 and 935 <= loc[1] <= 945:
        return 'box1'
    elif 1175 <= loc[0] <= 1185 and 935 <= loc[1] <= 945:
        return 'box2'
    elif 1242 <= loc[0] <= 1252 and 935 <= loc[1] <= 945:
        return 'box3'
    elif 1110 <= loc[0] <= 1120 and 983 <= loc[1] <= 992:
        return 'box4'
    elif 1175 <= loc[0] <= 1185 and 983 <= loc[1] <= 992:
        return 'box5'
    elif 1242 <= loc[0] <= 1252 and 983 <= loc[1] <= 992:
        return 'box6'
    else:
        return None

def main():
    counter = 0

    # boxes = {
    #     'box1': [1115, 940],
    #     'box2': [1180, 940],
    #     'box3': [1247, 940],
    #     'box4': [1115, 988],
    #     'box5': [1180, 988],
    #     'box6': [1247, 988]  # variable +-5 is what i want
    # }

    while 1:
        counter+=1

        prev_inventory = {}
        curr_inventory = {}

        a = pyautogui.locateOnScreen('observer.PNG',confidence = 0.75)
        b = pyautogui.locateOnScreen('antiward.PNG',confidence = 0.75)
        c = pyautogui.locateOnScreen('observer_antiward.PNG',confidence = 0.75)

        if a:
            prev_inventory[box_checker(a)] = 'obs'
        if b:
            prev_inventory[box_checker(b)] = 'anti'
        if c:
            prev_inventory[box_checker(c)] = 'obs+anti'


        print('--------------------------------------------------------------------')

        print('Previous inventory : ',prev_inventory)

        time.sleep(5)

        a = pyautogui.locateOnScreen('observer.PNG', confidence=0.75)
        b = pyautogui.locateOnScreen('antiward.PNG', confidence=0.75)
        c = pyautogui.locateOnScreen('observer_antiward.PNG', confidence=0.75)

        if a:
            curr_inventory[box_checker(a)] = 'obs'
        if b:
            curr_inventory[box_checker(b)] = 'anti'
        if c:
            curr_inventory[box_checker(c)] = 'obs+anti'
        print('Current inventory : ',curr_inventory)

        set1 = set(prev_inventory.items())
        set2 = set(curr_inventory.items())

        if prev_inventory != curr_inventory and counter != 1:
            if len(prev_inventory) < len(curr_inventory):
                print('\nA ward has been purchased!\n')
                playsound('ward_notification.mp3')
            else:
                print('\nA ward has been placed!\n')
                playsound('ward_notification.mp3')
            print('Here is the inventory change : ',set1 ^ set2)

main()


# Observer in inventory at :  Box(left=1115, top=940, width=67, height=51) box1
# Anti-ward in inventory at :  Box(left=1247, top=941, width=64, height=51) box3
# Observer and Anti-ward mix in inventory at :  Box(left=1180, top=939, width=70, height=52) box2
#
# Observer in inventory at :  Box(left=1115, top=988, width=67, height=51) box4
# Anti-ward in inventory at :  Box(left=1247, top=990, width=64, height=51) box6
# Observer and Anti-ward mix in inventory at :  Box(left=1180, top=987, width=70, height=52) box5
#
# Observer in inventory at :  Box(left=1247, top=940, width=67, height=51) box 3
# Anti-ward in inventory at :  Box(left=1181, top=941, width=64, height=51)
# Observer and Anti-ward mix in inventory at :  Box(left=1114, top=939, width=70, height=52)
