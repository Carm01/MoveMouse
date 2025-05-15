import pyautogui
import time
import pystray
from PIL import Image
import threading
import sys
import random
import os

# Set pyautogui to not pause between actions
pyautogui.PAUSE = 0

# Get screen dimensions using pyautogui
screen_width, screen_height = pyautogui.size()
x_limit = screen_width * 0.8
y_limit = screen_height * 0.8

def move_mouse_if_idle():
    while True:
        initial_pos = pyautogui.position()
        time.sleep(60)
        current_pos = pyautogui.position()
        if initial_pos == current_pos:
            new_x = random.randint(1, int(x_limit))
            new_y = random.randint(1, int(y_limit))
            pyautogui.moveTo(new_x, new_y, duration=0.25)

def on_exit(icon, item):
    icon.stop()
    sys.exit()

def create_tray_icon():
    # Load the .ico file
    icon_path = (
        os.path.join(sys._MEIPASS, "Proycontec-Robots-Robot-screen-settings.ico")
        if hasattr(sys, '_MEIPASS')
        else r"P:\Apps\Python\Proycontec-Robots-Robot-screen-settings.ico"
    )
    try:
        image = Image.open(icon_path)
        # Resize to 16x16 for system tray compatibility
        image = image.resize((16, 16), Image.LANCZOS)
    except Exception as e:
        print(f"Error loading icon: {e}")
        # Fallback to a generic icon
        image = Image.new('RGB', (16, 16), color='white')
    
    menu = pystray.Menu(
        pystray.MenuItem("Exit", on_exit)
    )
    icon = pystray.Icon("Mouse Mover", image, "Mouse Mover", menu)
    icon.run()

def main():
    mouse_thread = threading.Thread(target=move_mouse_if_idle, daemon=True)
    mouse_thread.start()
    create_tray_icon()

if __name__ == "__main__":
    main()