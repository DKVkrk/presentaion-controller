import cv2
import mediapipe as mp
import pyautogui
import time
import numpy as np

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

presentation_started = False
last_gesture_time = 0
gesture_delay = 1  # seconds

def detect_gesture(hand_landmarks):
    thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    thumb_ip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP]
    index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    index_mcp = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP]
    middle_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
    ring_tip = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]
    pinky_tip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]

    thumb_y = thumb_tip.y
    thumb_ip_y = thumb_ip.y
    index_y = index_tip.y
    index_mcp_y = index_mcp.y
    middle_y = middle_tip.y
    ring_y = ring_tip.y
    pinky_y = pinky_tip.y

    # Laser pointer: index and middle up, ring and pinky down
    if (index_y < index_mcp_y and middle_y < index_mcp_y and
        ring_y > thumb_ip_y and pinky_y > thumb_ip_y):
        return 'laser_pointer'
    # Index up
    elif index_y < index_mcp_y < middle_y and all(finger.y > thumb_ip_y for finger in [middle_tip, ring_tip, pinky_tip]):
        return 'index_up'
    # Closed hand
    elif all(finger.y > thumb_ip_y for finger in [thumb_tip, index_tip, middle_tip, ring_tip, pinky_tip]):
        return 'closed_hand'
    # Open hand
    elif all(finger.y < thumb_ip_y for finger in [index_tip, middle_tip, ring_tip, pinky_tip]):
        return 'open_hand'
    return None

def perform_gesture_action(gesture, hand_landmarks=None, frame_shape=None):
    global presentation_started
    global last_gesture_time

    current_time = time.time()
    if gesture != 'laser_pointer' and current_time - last_gesture_time < gesture_delay:
        return  

    if gesture != 'laser_pointer':
        last_gesture_time = current_time

    print(f"Performing action for gesture: {gesture}")
    if gesture == 'index_up':
        print("Going to next slide...")
        pyautogui.press('right')  
    elif gesture == 'closed_hand':
        print("Going to previous slide...")
        pyautogui.press('left')   
    elif gesture == 'open_hand':
        if not presentation_started:
            print("Starting presentation...")
            pyautogui.press('f5') 
            presentation_started = True
        else:
            print("Stopping presentation...")
            pyautogui.press('esc')  
            presentation_started = False
    elif gesture == 'laser_pointer' and hand_landmarks is not None and frame_shape is not None:
        # Move mouse to index finger tip position
        index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
        h, w, _ = frame_shape
        x = int(index_tip.x * w)
        y = int(index_tip.y * h)
        screen_w, screen_h = pyautogui.size()
        # Map camera coordinates to screen coordinates
        screen_x = np.interp(x, [0, w], [0, screen_w])
        screen_y = np.interp(y, [0, h], [0, screen_h])
        pyautogui.moveTo(screen_x, screen_y)
        print(f"Laser pointer at: {int(screen_x)}, {int(screen_y)}")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    gesture = None
    hand_landmarks = None

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            gesture = detect_gesture(hand_landmarks)
            if gesture:
                print(f"Detected Gesture: {gesture}")
                perform_gesture_action(gesture, hand_landmarks, frame.shape)

    cv2.imshow('Gesture-based Presentation Controller', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
