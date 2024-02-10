import cv2
import mediapipe as mp
import pickle
import os
import numpy as np

def preprocess_image(image_path):
    # Read and resize the image
    image = cv2.imread(image_path)
    image = cv2.resize(image, (256, 256))  # Adjust size as needed
    return image

def extract_hand_pattern(image):
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands()

    # Convert BGR image to RGB
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Process the frame with MediaPipe Hands
    results = hands.process(rgb_image)

    # Extract hand landmarks
    landmarks = []
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            for landmark in hand_landmarks.landmark:
                landmarks.extend([landmark.x, landmark.y, landmark.z])

    return np.array(landmarks)

def create_hand_pattern_dataset(folder_path):
    dataset = {"patterns": [], "labels": []}

    for gesture_label in os.listdir(folder_path):
        gesture_folder = os.path.join(folder_path, gesture_label)

        if os.path.isdir(gesture_folder):
            for image_file in os.listdir(gesture_folder):
                image_path = os.path.join(gesture_folder, image_file)

                # Preprocess image
                image = preprocess_image(image_path)

                # Extract hand pattern features
                hand_pattern = extract_hand_pattern(image)

                # Add to the dataset
                dataset["patterns"].append(hand_pattern)
                dataset["labels"].append(gesture_label)

    return dataset

def save_dataset(dataset, save_path):
    with open(save_path, 'wb') as file:
        pickle.dump(dataset, file)

# Example usage:
folder_path = "path/to/your/images"
save_path = "hand_pattern_dataset.pkl"

# Create the dataset
hand_dataset = create_hand_pattern_dataset(folder_path)

# Save the dataset
save_dataset(hand_dataset, save_path)

# Load hand patterns dataset from .pkl file
dataset_file_path = "hand_pattern_dataset.pkl"  # Replace with the path to your .pkl file

with open(dataset_file_path, 'rb') as file:
    hand_patterns_dataset = pickle.load(file)

# Initialize MediaPipe Hands model
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils

def detect_hands(frame):
    # Convert BGR image to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame with MediaPipe Hands
    results = hands.process(rgb_frame)

    # If hands are detected, draw landmarks on the frame
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw hand landmarks on the frame
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            recognize_hand_pattern(hand_landmarks)  # Recognize hand pattern

    return frame

def recognize_hand_pattern(hand_landmarks):
    landmarks = []
    for landmark in hand_landmarks.landmark:
        landmarks.extend([landmark.x, landmark.y, landmark.z])

    # Calculate distances (similar to previous code)
    thumb_tip = landmarks[3:6]
    index_finger_tip = landmarks[6:9]
    middle_finger_tip = landmarks[9:12]
    ring_finger_tip = landmarks[12:15]
    pinky_finger_tip = landmarks[15:18]

    distances = [
        distance(thumb_tip, index_finger_tip),
        distance(thumb_tip, middle_finger_tip),
        distance(thumb_tip, ring_finger_tip),
        distance(thumb_tip, pinky_finger_tip)
    ]

    # Match detected hand pattern to the loaded dataset
    matched_pattern = None
    for pattern, thresholds in hand_patterns_dataset.items():
        if all(distance < threshold for distance, threshold in zip(distances, thresholds)):
            matched_pattern = pattern
            break

    if matched_pattern:
        print(f"Detected Hand Pattern: {matched_pattern}")

def distance(point1, point2):
    return (((point1[0] - point2[0]) ** 2) + ((point1[1] - point2[1]) ** 2) + ((point1[2] - point2[2]) ** 2)) ** 0.5

# Open the camera
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    frame_with_hands = detect_hands(frame)

    cv2.imshow('Hand Detection', frame_with_hands)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()