from PIL import Image
import pyautogui
import json

myScreenshot = pyautogui.screenshot()
myScreenshot.save(r'C:\\Users\\ezulq\\Desktop\\Coding\Python\\ocr\\screenshot.png')


filename = "screenshot.png"
img = Image.open(filename)
#img.show()

slots = {}


slots['first'] = img.getpixel((1150,965))
slots['second'] = img.getpixel((1215,965))
slots['third'] = img.getpixel((1280,965))

slots['fourth'] = img.getpixel((1150,1015))
slots['fifth'] = img.getpixel((1215,1015))
slots['sixth'] = img.getpixel((1270,1015))

key_list = list(slots.keys())
val_list = list(slots.values())

# position = val_list.index(100)
# print(key_list[position])
# print(slots)
prettydictionary = json.dumps(slots, sort_keys=False, indent=4)
print(prettydictionary)
for i in range(len(slots)):
    key = key_list[val_list.index(val_list[i])]

    if 164 <= val_list[i][0] <= 191 and 72 <= val_list[i][1] <= 99 and 8 <= val_list[i][2] <= 37:
        print('observer and anti-ward mix in slot : ', key)
        continue
    if 66 <= val_list[i][0] <= 185 and 44 <= val_list[i][1] <= 160 and 7 <= val_list[i][2] <= 63:
        print('observer in slot : ',key)
        continue
    if val_list[i][0] <= 20 and 52 <= val_list[i][1] <= 77 and 47 <= val_list[i][2] <= 74:
        print('anti-ward in slot : ',key)
        continue

