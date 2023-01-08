import pyautogui
import pyperclip
import time
from PIL import Image

pyautogui.moveTo(1420, 300);
pyautogui.click();
time.sleep(0.5);

pyperclip.copy("서울날씨");
pyautogui.hotkey("ctrl", "v");
time.sleep(0.5);

pyautogui.write(["enter"]);
time.sleep(1);

start_X = 1013;
start_Y = 451;
end_X = 1818;
end_Y = 822;


pyautogui.screenshot(r"서울날씨.png", region = (start_X, start_Y, end_X-start_X, end_Y-start_Y));


image = Image.open("서울날씨.png");
image.show();