# 🖐️ Gesture-Based Presentation Controller  

A **Python-based presentation controller** using **OpenCV, Mediapipe, and PyAutoGUI** that allows you to control slides and use a **laser pointer** with **hand gestures**.  

No need for a clicker or remote – just use your webcam and your hand! 🎥  

---

## 🚀 Features  

- 👉 **Index Finger Up** → Next Slide  
- ✊ **Closed Hand** → Previous Slide  
- 🖐 **Open Hand** → Start/Stop Presentation  
- ✌ **Index + Middle Up** → Laser Pointer (moves mouse cursor with your finger)  


---

## ⚙️ Tech Stack  

- **Python 3.8+**  
- **OpenCV** – Webcam access & frame processing  
- **Mediapipe** – Hand tracking & landmark detection  
- **PyAutoGUI** – Keyboard/mouse automation  
- **NumPy** – Coordinate mapping  

---

## 📂 Project Structure  

📁 gesture-presentation-controller
│── app.py              # Main script (gesture detection + actions)
│── requirements.txt    # Dependencies
│── README.md           # Documentation

---


## 📦 Installation

Clone the repository
git clone https://github.com/your-username/gesture-presentation-controller.git
cd gesture-presentation-controller


Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows


Install dependencies
pip install -r requirements.txt

---

## ▶️ Usage

Run the app:
python app.py
Perform gestures in front of your webcam:
👉 Index Finger Up → Next Slide (Right Arrow)
✊ Closed Hand → Previous Slide (Left Arrow)
🖐 Open Hand → Start (F5) / Stop (ESC) Presentation
✌ Laser Pointer → Move mouse with your index finger
Press q to exit the program.

---

## 🙌 Acknowledgements
Mediapipe – Hand Tracking
OpenCV – Computer Vision
PyAutoGUI – Automation

---

## 🔮 Future Enhancements
🎤 Voice commands for hybrid control
🖱️ Add custom gestures (e.g., thumbs up → start presentation)
📊 GUI for selecting gestures & actions
🌐 Convert into a web-based gesture controller


