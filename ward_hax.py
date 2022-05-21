import time
import pyautogui
import json


def pretty_print(mydict):
    # return mydict
    return json.dumps(mydict, indent=4)


def main():
    counter = 0
    flag = 0
    prev = ''

    locs = {}
    print()

    while 1:
        team = input('What team are you [green] or [red]? : ')
        if team.upper() == 'GREEN':
            flag = 0
            break
        elif team.upper() == 'RED':
            flag = 1
            break
        else:
            continue
    print()
    while 1:

        if flag:
            a = pyautogui.locateOnScreen('red_obs.png', confidence=0.75)
            b = pyautogui.locateOnScreen('red_antiward.png', confidence=0.75)
            c = pyautogui.locateOnScreen('red_obs_antiward_combo.png', confidence=0.75)

            if a:
                temp = ['observer']
                if a in locs.values():
                    continue

                else:
                    temp.append(str(a))

                    locs[counter] = temp
                    print('Observer on map : ',a)
                # pyautogui.click(a)
                counter += 1

            if b:
                temp = ['anti-ward']
                if b in locs.values():
                    continue

                else:
                    temp.append(str(b))
                    locs[counter] = temp
                    print('Anti-ward on map : ',b)
                # pyautogui.click(b)
                counter += 1

            if c:
                temp = ['observer anti-ward combination']
                if c in locs.values():
                    continue
                else:
                    temp.append(str(c))
                    locs[counter] = temp
                    print('Observer Anti-ward combonation on map : ',c)
                # pyautogui.click(c)
                counter += 1

            if prev == locs:
                print('\nNo new wards')
            else:
                print('\n',pretty_print(locs), '\n')

            prev = locs
            time.sleep(5)

        else:
            d = pyautogui.locateOnScreen('green_obs.png', confidence=0.75)
            e = pyautogui.locateOnScreen('green_antiward.png', confidence=0.75)
            f = pyautogui.locateOnScreen('green_opbs_antiward_combo.png', confidence=0.75)


main()