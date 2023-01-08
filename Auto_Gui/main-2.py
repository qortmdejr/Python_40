import pyautogui
import time
import pyperclip

pyautogui.moveTo(850,270,0.2);
pyautogui.click();
time.sleep(0.5);

pyperclip.copy("서울 날씨");
pyautogui.hotkey("command", "v");
time.sleep(0.5);

pyautogui.write(["enter"]);
time.sleep(1);