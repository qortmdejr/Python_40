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

start_x = 777;
start_y = 153;
end_x = 1382;
end_y = 702;

pyautogui.screenshot(region = (start_x, start_y, end_x-start_x, end_y-start_y));

