import pyautogui
import pyperclip
import time

pyautogui.moveTo(1420, 300);
pyautogui.click();

pyperclip.copy("서울날씨");
pyautogui.hotkey("ctrl", "v");

pyautogui.write(["enter"]);

