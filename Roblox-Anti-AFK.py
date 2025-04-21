import tkinter as tk
import threading
import time
import pyautogui
import random
import pygetwindow as gw

running = False
keys = ['w', 'a', 's', 'd']
afk_enabled = False

def afk_loop():
    global running, afk_enabled
    while running:
        time.sleep(900)  # Wait 15 minutes
        active_window = gw.getActiveWindow()
        if active_window and "Roblox" in active_window.title:  # Check if Roblox is the active window
            if not afk_enabled:
                afk_enabled = True
                log("Roblox selected, starting Anti-AFK actions.")
            pyautogui.moveRel(0, 10, duration=0.2)
            pyautogui.moveRel(0, -10, duration=0.2)
            pyautogui.click()
            pyautogui.press('space')
            rand_key = random.choice(keys)
            pyautogui.press(rand_key)
            log(f"Did anti-AFK actions (space + click + key: {rand_key})")
        else:
            if afk_enabled:
                afk_enabled = False
                log("Roblox deselected, stopping Anti-AFK actions.")
                stop_afk()

def start_afk():
    global running
    if not running:
        running = True
        log("Anti-AFK started.")
        threading.Thread(target=afk_loop, daemon=True).start()

def stop_afk():
    global running
    running = False
    log("Anti-AFK stopped.")

def log(msg):
    output_text.insert(tk.END, msg + "\n")
    output_text.see(tk.END)

# GUI Setup
root = tk.Tk()
root.title("Roblox Anti-AFK")
root.geometry("300x250")

start_button = tk.Button(root, text="Start Anti-AFK", command=start_afk)
start_button.pack(pady=10)

stop_button = tk.Button(root, text="Stop Anti-AFK", command=stop_afk)
stop_button.pack(pady=5)

output_text = tk.Text(root, height=10, width=35)
output_text.pack(pady=10)

log("Ready. Click Start to begin.")

root.mainloop()
