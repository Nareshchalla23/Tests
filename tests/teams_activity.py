import pyautogui
import time
import random
import win32gui
import win32con

def minimize_all_windows():
    pyautogui.hotkey('win', 'd')
    time.sleep(1)

def get_desktop_area():
    screen_width, screen_height = pyautogui.size()
    taskbar_height = 40
    desktop_area = (0, 0, screen_width, screen_height - taskbar_height)
    return desktop_area

def is_icon_position(x, y):
    return (x % 80 < 60) and (y % 80 < 60)

def simulate_visible_activity(desktop_area):
    x1, y1, x2, y2 = desktop_area
    
    while True:
        x = random.randint(x1, x2)
        y = random.randint(y1, y2)
        
        if not is_icon_position(x, y):
            break
    
    pyautogui.moveTo(x, y, duration=0.5)
    pyautogui.click(duration=0.2)
    pyautogui.moveRel(50, 0, duration=0.2)
    pyautogui.moveRel(0, 50, duration=0.2)
    pyautogui.moveRel(-50, 0, duration=0.2)
    pyautogui.moveRel(0, -50, duration=0.2)
    pyautogui.rightClick(duration=0.2)
    pyautogui.press('shift')

    print(f"Clicked at ({x}, {y}) at {time.strftime('%H:%M:%S')}")

def main():
    duration = 5 * 60 * 60
    interval = 5

    end_time = time.time() + duration

    print("Starting desktop activity simulation. Press Ctrl+C to stop.")
    time.sleep(5)

    minimize_all_windows()
    desktop_area = get_desktop_area()

    try:
        while time.time() < end_time:
            simulate_visible_activity(desktop_area)
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\nSimulation stopped by user.")

if __name__ == "__main__":
    main()
