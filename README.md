# Face ID Door

This project implements a Face ID-based door lock system using OpenCV and DeepFace for face recognition and GPIO for controlling the door lock mechanism. If you have any questions feel free to contact me (as well as if you want any new features) 

This is a relatively simple program so feel free to modify it as you wish!

## Overview

The Face ID Door system captures video input from a camera, detects faces in the frames, and verifies them against a set of approved faces. If a match is found, the door is unlocked. The door control logic is handled through GPIO pins, suitable for use with hardware like the Raspberry Pi.

## Features

- Real-time face detection and recognition using OpenCV and DeepFace
- Multi-threaded processing for efficient performance
- Hardware control for door locking and unlocking
- Configurable via a Python script

## Requirements

- Python 3.7+
- OpenCV
- DeepFace
- Hardware with GPIO pins (e.g., Raspberry Pi)
- Modify the door.py file as needed. (Your door mechanism probably wont be the same as mine)

## Setup

1. **Clone the Repository:**

    ```sh
    git clone https://github.com/Ali-Vali-007/face-id-door.git
    cd face-id-door
    ```

2. **Install Dependencies:**

    ```sh
    pip install opencv-python-headless
    pip install deepface
    ```

3. **Prepare Approved Faces:**

    - Place images of approved faces in the `Face ID/APPROVEDFACES/` directory.
    - Ensure the images are named as `0.jpg`, `1.jpg`, etc.

4. **Set Up Hardware:**

    - Connect your door lock mechanism to the appropriate GPIO pins as defined in `door.py`.

## Usage

1. **Run the Face ID Door System:**

    ```sh
    python camerainput.py
    ```

    This script will start capturing video from the default camera, process each frame for face detection, and control the door lock based on recognition results.

2. **Exiting the Program:**

    - Press the `\`` key to exit the video loop and terminate t
