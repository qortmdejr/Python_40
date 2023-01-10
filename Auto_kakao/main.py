import pyautogui
import pyperclip
import time
import threading
import os

def send_message():
    threading.Timer(10, send_message).start();

    picPosition = pyautogui.locateOnScreen("pic1.png");
    print(picPosition);

    if picPosition is None:
        picPosition = pyautogui.locateOnScreen("pic2.png");
        print(picPosition);
    if picPosition is None:
        picPosition = pyautogui.locateOnScreen("pic3.png");
        print(picPosition);


    clickPosition = pyautogui.center(picPosition);
    pyautogui.doubleClick(clickPosition);

    pyperclip.copy("....................");
    pyautogui.hotkey("ctrl" ,"v");
    time.sleep(0.5);

    pyautogui.write(["enter"]);
    time.sleep(0.5);

    pyautogui.write(["escape"]);
    time.sleep(0.5);

send_message();