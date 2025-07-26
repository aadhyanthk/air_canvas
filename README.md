# Air Canvas: Hand Gesture Drawing & AR Toolkit

Air Canvas is a Python application that lets you draw, annotate, and manipulate graphics in real-time using only your hands and webcam—no mouse or touchscreen required. It leverages [MediaPipe](https://mediapipe.dev/) for hand tracking, supports shape and color controls, drawing grid alignment, freehand/straight lines, shape rotation, and even voice commands for a seamless, interactive experience.

## Features

- **Draw in Mid-Air:** Use hand gestures to draw lines, shapes, or erase on a digital "air canvas."
- **Shape Support:** Draw straight lines, rectangles, circles, or freehand curves.
- **Grid Snapping:** Toggle grid alignment for precise, straight lines.
- **Shape Manipulation:** Rotate drawn shapes using keyboard controls.
- **Color & Thickness Selection:** Switch between colors (blue, pink, green) and line thickness with voice commands.
- **Erase & Clear:** Erase selectively or clear the entire canvas.
- **Voice Recognition:** Issue drawing or tool-change commands simply by speaking.
- **Live Camera Feed:** View yourself in a corner of the canvas for spatial reference.


## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/air-canvas.git
   cd air-canvas
   ```

2. **(Optional but recommended) Create a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   Or, manually:
   ```bash
   pip install opencv-python mediapipe numpy pyttsx3 SpeechRecognition keyboard
   ```

## Usage

### Air Canvas AR Toolkit

- **To start the main canvas with hand gesture controls & voice:**
  ```bash
  python AR_Canvas.py
  ```

- **To use the classic version with manual/keyboard shape control:**
  ```bash
  python main.py
  ```

- **To experiment with shape rotation features:**
  ```bash
  python rotation.py
  ```

Follow on-screen prompts or voice feedback. Use gestures and supported voice commands to switch modes, colors, and thickness.

## Controls

### Hand Gestures
- **Index Finger Tip** is used for drawing and specifying shape positions.

### Voice Commands (in AR_Canvas.py)
Say any of the following to change modes or settings:
- `"paint"` – Freehand draw  
- `"straight"` – Draw straight lines  
- `"rectangle"` or `"circle"` – Draw the shape  
- `"erase"` – Switch to eraser  
- `"clear"` – Clear entire canvas  
- `"pink"`, `"green"`, `"blue"` – Change color  
- `"thicker"`, `"thinner"` – Adjust stroke width  

### Keyboard Shortcuts (main.py, rotation.py)
- **r** – Reset/clear drawing
- **u/y** – Undo last line (two modes)
- **s** – Toggle straight/grid snap mode
- **l, j, k, i** – Move drawing right, left, down, up
- **g** – Rotate drawing (rotation.py)
- **q** – Quit

## File Overview

- **AR_Canvas.py**: Advanced canvas with hand, shape, and voice control.
- **main.py**: Classic grid/curve air drawing with keyboard toggles.
- **rotation.py**: Drawing + rotate shapes feature demonstration.
- **requirements.txt**: All necessary Python dependencies.

## Requirements

- Python 3.7+
- Webcam
- [MediaPipe](https://google.github.io/mediapipe/) (for hand tracking)
- [OpenCV](https://opencv.org/)
- `pyttsx3`, `SpeechRecognition`, `keyboard`, `numpy`

## Notes

- No virtual environments (`venv/`, `.venv/`) or temporary files should be committed to the repository—add them to your `.gitignore`.
- This tool is intended for educational, prototyping, and demo purposes.

## Acknowledgements

- [MediaPipe by Google](https://mediapipe.dev/)
- [OpenCV](https://opencv.org/)
- The Python open-source community

**Enjoy drawing in mid-air! For questions or ideas, [open an issue](https://github.com/yourusername/air-canvas/issues).**

*Tip: Replace `yourusername` with your actual GitHub username and add a real demo screenshot for best effect.*

[1] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/62972974/68a7a85c-bd64-4cdd-a7b1-f36af88c506a/AR_Canvas.py
[2] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/62972974/d30b7834-ab3e-4cca-a8ef-936cdc5b5402/main.py
[3] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/62972974/763a14cf-3c89-43a2-bb86-7acdea6a5a7c/rotation.py
