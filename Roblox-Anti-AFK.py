import tkinter as tk
import threading
import time
import pyautogui
import random

running = False
keys = ['w', 'a', 's', 'd']

def afk_loop():
    global running
    while running:
        time.sleep(900)  # Wait 15 minutes
        pyautogui.moveRel(0, 10, duration=0.2)
        pyautogui.moveRel(0, -10, duration=0.2)
        pyautogui.click()
        pyautogui.press('space')
        rand_key = random.choice(keys)
        pyautogui.press(rand_key)
        log(f"Did anti-AFK actions (space + click + key: {rand_key})")

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

# Modern GUI Setup
root = tk.Tk()
root.title("Roblox Anti-AFK")
root.geometry("350x300")
root.config(bg="#1c1c1c")  # Dark background color

# Fonts and Styling
font_style = ("Segoe UI", 12)
button_font = ("Segoe UI", 14)
button_bg = "#4caf50"  # Green for active state
button_fg = "#fff"  # White text
text_bg = "#333"  # Darker background for text
text_fg = "#ccc"  # Light grey text

# Start and Stop Buttons
start_button = tk.Button(root, text="Start Anti-AFK", command=start_afk, font=button_font, bg=button_bg, fg=button_fg, relief="flat", width=20, height=2)
start_button.pack(pady=15)

stop_button = tk.Button(root, text="Stop Anti-AFK", command=stop_afk, font=button_font, bg="#f44336", fg=button_fg, relief="flat", width=20, height=2)
stop_button.pack(pady=5)

# Output Text Area
output_text = tk.Text(root, height=8, width=35, font=font_style, bg=text_bg, fg=text_fg, relief="flat", bd=0)
output_text.pack(pady=10)

log("Ready. Click Start to begin.")

root.mainloop()
