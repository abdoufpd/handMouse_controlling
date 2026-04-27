# handMouse_controlling
this project is a python-ydotool  that u can control ur screen using hand gestures
<br>
**🖐️ Real-Time Hand Tracking & Gesture-Based Mouse Control** <br>

This project implements a real-time hand tracking system using OpenCV and MediaPipe to control the mouse cursor through natural hand gestures. <br>

By leveraging advanced computer vision techniques, the system detects hand landmarks from a webcam feed and translates finger movements into precise cursor control, enabling a touchless human-computer  <br>interaction experience.
 <br>
**🚀 Features** <br>
Real-time hand detection with high accuracy <br>
Multi-hand tracking (supports up to 2 hands) <br>
Landmark visualization with custom skeletal connections <br>
Gesture-based mouse control: <br>
Move cursor using thumb position <br>
Perform click actions by detecting thumb–index pinch <br>
Distance-based gesture recognition using Euclidean geometry <br>
FPS monitoring for performance tracking <br>
**🧠 How It Works**<br>
Uses MediaPipe’s Hand Landmarker model to extract 21 key hand landmarks per frame <br>
Computes the distance between the thumb tip and index finger tip <br>
Maps hand coordinates to screen coordinates for cursor movement <br>
Triggers mouse clicks when fingers are close (pinch gesture) <br>
Executes system-level mouse commands via ydotool <br>
**🛠️ Tech Stack** <br>
Python <br>
OpenCV <br>
MediaPipe Tasks API
NumPy / Math
Subprocess (for OS-level control) <br>
**💡 Use Cases** <br>
Touchless interfaces <br>
Accessibility tools <br>
Gesture-based control systems <br>
Interactive installations <br>
Prototyping human-computer interaction (HCI) systems <br>  <br> <br>
**⚠️ Requirements**<br>
Linux environment (for ydotool) <br> <br>
Webcam access <br>
Pretrained MediaPipe hand landmark model(included in `/pretrainde_model`) <br>
**📌 Future Improvements**<br>
more accuracy <br>
Gesture recognition expansion (scroll, drag, multi-click) <br>
Smoothing & filtering for more stable cursor control <br>
Cross-platform mouse control support <br>
GUI for calibration and sensitivity adjustment <br>
