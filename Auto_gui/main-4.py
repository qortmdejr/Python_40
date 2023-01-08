import pyautogui
import time
import pyperclip
from PIL import Image

All_Weather = ["서울 날씨", "시흥 날씨", "청주 날씨", "부산 날씨"," 강원도 날씨"];

addr_X = 1420;
addr_Y = 300;
start_X = 1013;
start_Y = 452;
end_X = 1820;
end_Y = 822;

for Weather in All_Weather:
    pyautogui.moveTo(addr_X, addr_Y, 0.2);

    pyautogui.click();

    pyautogui.moveTo(addr_X, addr_Y, 0.2);
    pyperclip.copy(Weather);
    pyautogui.hotkey("ctrl", "v");

    pyautogui.write(["enter"]);

    저장경로 = Weather + '.png';
    pyautogui.screenshot(저장경로, region = (start_X, start_Y, end_X-start_X, end_Y-start_Y));
