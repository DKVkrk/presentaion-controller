# Presentation Controller

A gesture-based presentation controller using Python, MediaPipe, and PyAutoGUI that allows you to control your presentations using hand gestures captured through your webcam.

## 🎯 Features

- **Gesture Recognition**: Real-time hand gesture detection using MediaPipe
- **Slide Navigation**: Control presentation slides with intuitive hand gestures
- **Laser Pointer**: Use your index finger as a virtual laser pointer
- **Cross-Platform**: Works on Windows, macOS, and Linux
- **Real-time Feedback**: Visual feedback with hand landmark tracking
- **Easy Setup**: Simple installation and configuration

## 🎮 Supported Gestures

| Gesture | Action | Description |
|---------|--------|-------------|
| 👆 **Index Up** | Next Slide | Point with index finger only |
| ✊ **Closed Hand** | Previous Slide | Make a fist |
| ✋ **Open Hand** | Start/Stop Presentation | Open palm facing camera |
| 👉 **Laser Pointer** | Mouse Control | Index and middle finger up, others down |

## 📋 Prerequisites

- Python 3.7 or higher
- Webcam
- Presentation software (PowerPoint, Google Slides, etc.)

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/presentation-controller.git
cd presentation-controller
```

### 2. Create Virtual Environment (Recommended)

```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install opencv-python mediapipe pyautogui numpy
```

Or install from requirements.txt (if available):
```bash
pip install -r requirements.txt
```

## 🎯 Usage

### 1. Start the Application

```bash
python app.py
```

### 2. Prepare Your Presentation

1. Open your presentation in your preferred software (PowerPoint, Google Slides, etc.)
2. Make sure your presentation is ready to start

### 3. Use Gestures

- **Start Presentation**: Show an open hand (✋) to start the presentation
- **Next Slide**: Point with your index finger (👆)
- **Previous Slide**: Make a fist (✊)
- **Laser Pointer**: Use index and middle finger up, others down (👉)
- **Stop Presentation**: Show an open hand (✋) again

### 4. Exit the Application

Press `q` in the camera window to quit the application.

## ⚙️ Configuration

You can modify the following parameters in `app.py`:

- `min_detection_confidence`: Hand detection confidence threshold (default: 0.7)
- `min_tracking_confidence`: Hand tracking confidence threshold (default: 0.7)
- `gesture_delay`: Delay between gesture actions in seconds (default: 1)

## 🔧 Troubleshooting

### Common Issues

**Camera not detected:**
- Ensure your webcam is connected and not being used by another application
- Check camera permissions in your operating system

**Gestures not recognized:**
- Ensure good lighting conditions
- Keep your hand clearly visible in the camera frame
- Try adjusting the detection confidence thresholds

**PyAutoGUI not working:**
- On macOS, grant accessibility permissions to Terminal/IDE
- On Linux, install `python3-tk` and `python3-dev`

### Performance Tips

- Use a well-lit environment
- Keep your hand at a reasonable distance from the camera
- Close unnecessary applications to free up system resources

## 🛠️ Technical Details

### Dependencies

- **OpenCV**: Computer vision library for camera capture and image processing
- **MediaPipe**: Google's framework for building multimodal ML pipelines
- **PyAutoGUI**: Cross-platform GUI automation for controlling presentations
- **NumPy**: Numerical computing library for coordinate mapping

### Architecture

The application uses a real-time video processing pipeline:
1. **Camera Capture**: Continuous video feed from webcam
2. **Hand Detection**: MediaPipe hand landmark detection
3. **Gesture Classification**: Custom gesture recognition algorithm
4. **Action Execution**: PyAutoGUI commands for presentation control

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Setup

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run tests (if available)
python -m pytest

# Format code
black app.py
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **MediaPipe**: Google's framework for building multimodal ML pipelines
- **PyAutoGUI**: Cross-platform GUI automation Python module
- **OpenCV**: Open source computer vision library
- **NumPy**: Fundamental package for scientific computing with Python

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/your-username/presentation-controller/issues) page
2. Create a new issue with detailed information about your problem
3. Include your operating system, Python version, and error messages

## 🔄 Version History

- **v1.0.0**: Initial release with basic gesture controls
- Basic slide navigation (next/previous)
- Presentation start/stop functionality
- Laser pointer mode

---

**Made with ❤️ for seamless presentations**







