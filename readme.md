
# Roblox Anti-AFK

A simple tool to prevent going AFK in Roblox by simulating mouse movements, clicks, and keyboard inputs at regular intervals.

## Features
- Simulates mouse movement to prevent AFK timeout.
- Clicks and presses random keys (W, A, S, D) to keep the game active.
- Easy-to-use graphical interface with a Start and Stop button.

## How to Get Started

You can use this tool in two ways:

### Option 1: Download the Standalone Executable (Windows Only)
If you don't have Python installed, you can download the precompiled executable for Windows and run it directly.

1. Download the `.exe` file from the [Releases](#) section
2. Run the executable, and you'll see the graphical interface.
3. Click **Start Anti-AFK** to begin the anti-AFK actions.
4. Click **Stop Anti-AFK** to stop.

### Option 2: Run the Script Using Python
If you have Python installed, you can run the script directly from your computer.

#### Requirements:
- **Python 3.x** installed on your system.
- **`pyautogui`** and **`tkinter`** libraries installed.

#### Steps to Run the Script:
1. Install the necessary Python libraries by running:
   ```bash
   pip install pyautogui
   ```

2. Download or clone this repository to your local machine.

3. Open a terminal/command prompt and navigate to the folder where the script is located.

4. Run the script using Python:
   ```bash
   python Roblox-Anti-AFK.py
   ```

5. The GUI window will appear, and you can start and stop the anti-AFK actions by clicking the respective buttons.

## How It Works
- The tool automatically simulates mouse movement, clicking, and random keypresses (W, A, S, D) every 15 minutes.
- This prevents Roblox from detecting inactivity and kicking you out for being AFK.

## License
This project is open-source and available under the MIT License.
