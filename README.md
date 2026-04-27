# Computer-Vision-Automation-Bot-for-Chrome-Dino
A Python-based automation bot designed for the Chrome Dino game, using real-time screen capture and computer vision techniques to detect obstacles and trigger jumps automatically. The project combines image processing, template matching, and input simulation to achieve fast reaction times and continuous gameplay without manual control.



This project is a real-time automation bot for the Chrome Dino game. It uses computer vision to detect obstacles on the screen and simulates keyboard input to make the dinosaur jump automatically.



The bot captures a selected area of the screen, processes the image using edge detection, and reacts within milliseconds when an obstacle is identified.



How It Works:
  1. Searches for the dinosaur position on the screen using template matching.
  2. Defines a monitoring area in front of the dinosaur.
  3. Continuously captures frames from that area.
  4. Applies grayscale conversion and edge detection.
  5. Calculates pixel intensity changes to identify obstacles.
  6. Simulates a jump action when a threshold is exceeded.



Installation:

pip install opencv-python mss numpy pyautogui



Usage
  1. Open the Chrome Dino game.
  2. Ensure the dino.png template image is in the project folder.
  3. Run the script:
    python main.py
  4. Press q to stop execution.
