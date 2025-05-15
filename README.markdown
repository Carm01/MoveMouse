# Installation Instructions for MouseMover

To set up and build the `MouseMover` application, follow the steps below.

## Prerequisites

1. **Install Python**  
   Download and install Python from the official website: [python.org](https://www.python.org/downloads/){target=_blank}.
   - **Recommendation**: Install Python to `C:\Python` for simplicity.  
   - Ensure Python and pip are added to your system PATH during installation.

2. **Prepare an Icon File**  
   You will need an `.ico` file for the application icon. The path to this icon file is referenced in:
   - Line 35 of the `MouseMover.py` script.
   - Line 37 in the script (for the system tray icon).
   - The `pyinstaller` command (see below).  
   Replace `C:\path\to\your\icon\Proycontec-Robots-Robot-screen-settings.ico` with the actual path to your `.ico` file.

## Setup Instructions

### 1. Open a Command Prompt
- **First Command**: Navigate to the Python Scripts directory:  
  ```cmd
  cd C:\Python\Scripts
  ```
- **Second Command**: If you right-click and select "Open Terminal Here" in Windows, it may open PowerShell. To switch to the Command Prompt, type:  
  ```cmd
  CMD
  ```

### 2. Install Required Python Packages
- **Third Command**: Install `pyinstaller` using pip:  
  ```cmd
  pip install pyinstaller
  ```
- Install additional required packages:  
  ```cmd
  pip install pyautogui pystray pillow screeninfo
  ```

### 3. Build the Application
Use the following `pyinstaller` command to compile the script into a standalone executable:  
```cmd
pyinstaller --noconfirm --onefile --windowed --name NoSleep60 --icon "C:\path\to\your\icon\Proycontec-Robots-Robot-screen-settings.ico" --add-data "C:\path\to\your\icon\Proycontec-Robots-Robot-screen-settings.ico;." "C:\path\to\your\script\MouseMover.py"
```

- **Options Explained**:
  - `--noconfirm`: Overwrites previous builds without prompting.
  - `--onefile`: Packages the app into a single `.exe` file.
  - `--windowed`: Runs the app without a console window.
  - `--name NoSleep60`: Sets the output executable name to `NoSleep60.exe`.
  - `--icon`: Specifies the path to the icon file.
  - `--add-data`: Includes the icon file in the build.
  - The final argument is the path to your `MouseMover.py` script.

- **Important**: Replace `C:\path\to\your\icon\Proycontec-Robots-Robot-screen-settings.ico` and `C:\path\to\your\script\MouseMover.py` with the actual paths to your icon and script files.

## Troubleshooting
- Ensure Python is added to your system PATH. You can verify by running `python --version` in the Command Prompt.
- If you encounter errors with `pip`, ensure you’re in the correct directory (`C:\Python\Scripts`) or try upgrading pip:  
  ```cmd
  python -m pip install --upgrade pip
  ```
- If the icon file is not found, double-check the file path and ensure the `.ico` file exists.

## Notes
- The resulting executable (`NoSleep60.exe`) will be located in the `dist` folder created by `pyinstaller`.
- This application uses `pyautogui`, `pystray`, `pillow`, and `screeninfo` to simulate mouse movement and manage the system tray icon.
