import pyautogui
import time

def create_arr(locs):
    arr = []
    for pos in locs:
        arr.append((pos[0],pos[1]))
    return arr

def remove_similar(arr):
    res = []
    res2 = []
    res3 = []

    for i in arr:
        if i[0] not in res and i[0] + 1 not in res and i[0] - 1 not in res:
            res.append(i[0] + 10)
            res2.append(i[1] + 7)

    for i in range(len(res)):
        res3.append((res[i],res2[i]))

    return res3


def main():
    prev = []

    while 1:
        team = input('What team are you [green] or [red]? : ')
        if team.upper() == 'GREEN':
            ward = 'green_obs.png'
            break
        elif team.upper() == 'RED':
            ward = 'red_obs.png'
            break
        else:
            print('Invalid choice.')

    while 1:

        locs = pyautogui.locateAllOnScreen(ward,grayscale = False,confidence=.7)

        arr = create_arr(locs)
        arr = remove_similar(arr)

        print(arr)

        for i in range(len(arr)):
            pyautogui.click(arr[i])
            pyautogui.click(arr[i])
            time.sleep(5)

        time.sleep(5)

        if len(prev) < len(arr):
            print('New ward has been placed!')

        if len(prev) > len(arr):
            print('Nice job dewarding!')

        prev = arr

main()
