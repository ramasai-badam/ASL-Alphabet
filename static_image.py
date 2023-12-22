import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

# For static images:
mp_model = mp_hands.Hands(
    static_image_mode=True, # only static images
    max_num_hands=2, # max 2 hands detection
    min_detection_confidence=0.5) # detection confidence

# we are not using tracking confidence as static_image_mode is true.


# image_height, image_width, c = image.shape # get image shape
# # iterate on all detected hand landmarks
# for hand_landmarks in results.multi_hand_landmarks:
#       # we can get points using mp_hands
#       print(f'Ring finger tip coordinates: (',
#           f'{hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].x * image_width}, '
#           f'{hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y * image_height})'
    #   )

def processImage(image_path, output_dir):
    """ Process input image and save output image to given directory. """
    image = cv2.flip(cv2.imread(image_path), 1)
    if image is None: return
    # Convert the BGR image to RGB before processing.
    results = mp_model.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    

    if not results.multi_hand_landmarks:
        return # if there are no detections, we can skip the rest of the code in this function

    for hand_landmarks in results.multi_hand_landmarks:
        mp_drawing.draw_landmarks(
            image,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS,
            mp_drawing_styles.get_default_hand_landmarks_style(),
            mp_drawing_styles.get_default_hand_connections_style())
    # flip and write output image to disk
    cv2.imwrite(f"{output_dir}/{image_path.split('/')[-1]}", cv2.flip(image, 1))


import os
for image in os.listdir("images\A"):
    processImage(f"images\A\{image}", "output\A")