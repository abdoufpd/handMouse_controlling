# handMouse_controlling
this project is a python-ydotool  that u can control ur screen using hand gestures
<br>
**🖐️ Real-Time Hand Tracking & Gesture-Based Mouse Control**

This project implements a real-time hand tracking system using OpenCV and MediaPipe to control the mouse cursor through natural hand gestures.

By leveraging advanced computer vision techniques, the system detects hand landmarks from a webcam feed and translates finger movements into precise cursor control, enabling a touchless human-computer interaction experience.

**🚀 Features** <br>
Real-time hand detection with high accuracy
Multi-hand tracking (supports up to 2 hands)
Landmark visualization with custom skeletal connections
Gesture-based mouse control:
Move cursor using thumb position
Perform click actions by detecting thumb–index pinch
Distance-based gesture recognition using Euclidean geometry
FPS monitoring for performance tracking
**🧠 How It Works**<br>
Uses MediaPipe’s Hand Landmarker model to extract 21 key hand landmarks per frame
Computes the distance between the thumb tip and index finger tip
Maps hand coordinates to screen coordinates for cursor movement
Triggers mouse clicks when fingers are close (pinch gesture)
Executes system-level mouse commands via ydotool
🛠️ Tech Stack
Python
OpenCV
MediaPipe Tasks API
NumPy / Math
Subprocess (for OS-level control)
**💡 Use Cases<br>**
Touchless interfaces
Accessibility tools
Gesture-based control systems
Interactive installations
Prototyping human-computer interaction (HCI) systems
**⚠️ Requirements**<br>
Linux environment (for ydotool)
Webcam access
Pretrained MediaPipe hand landmark model(included in `/pretrainde_model`)
**📌 Future Improvements**<br>
more accuracy
Gesture recognition expansion (scroll, drag, multi-click)
Smoothing & filtering for more stable cursor control
Cross-platform mouse control support
GUI for calibration and sensitivity adjustment
