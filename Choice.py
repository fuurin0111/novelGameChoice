import keyboard
import time

def choice(text_list):
    global flag,button
    while flag:
        text_list = list(map(str, text_list))
        a = ""
        if len(text_list)%2 > 0:
            for i in range(len(text_list)%2): 
                text_list.append(" ")
        for i in range(int(len(text_list)/2)):
            if b == i*2:
                a = "▶︎" + text_list[i*2] + " " + text_list[i*2+1]
            elif b == i*2+1:
                a = " " + text_list[i*2] + "▶︎" + text_list[i*2+1]
            else:
                a = " " + text_list[i*2] + " " + text_list[i*2+1]
            print()
            print(a)
            print()
        keyboarder(len(text_list),int(len(text_list)/2))
    print(text_list[b])

def keyboarder(textlen,maxlen):
    global b,flag
    while True: 
        time.sleep(0.1)
        if keyboard.is_pressed("right"):
            if b >= 0 and b <= textlen-2:
                b += 1
                break
        elif keyboard.is_pressed("left"):
            if b >= 1 and b <= textlen-1:
                b -= 1
                break
        elif keyboard.is_pressed("up"):
            if b//2 >= 1 and b//2 <= maxlen-1:
                b -= 2
                break
        elif keyboard.is_pressed("down"):
            if b//2 >= 0 and b//2 <= maxlen-2:
                b += 2
                break
        elif keyboard.is_pressed("Space"):
            flag = False
            break

text_list_d = ["こんにちは","こんばんわ","おはよう","おやすみ"]
b = 0
flag  = True
choice(text_list_d)