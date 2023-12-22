import cv2
import os
import glob
import mediapipe as mp
from csv import writer
import pandas as pd
import gc
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

def processlandmarks(image_path):
    # print(image_path'{}'.format(1))
    mp_model = mp_hands.Hands(
        static_image_mode=True, # only static images
        max_num_hands=2, # max 2 hands detection
        min_detection_confidence=0.5) # detection confidence
    """ Process input image and save output image to given directory. """
    image = cv2.flip(cv2.imread(image_path), 1)
    # if image is None: return
    # Convert the BGR image to RGB before processing.
    results = mp_model.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    if not results.multi_hand_landmarks:
        return # if there are no detections, we can skip the rest of the code in this function

    keypoint = []
    for hand_landmarks in results.multi_hand_landmarks:
        for ids, landmrk in enumerate(hand_landmarks.landmark):
            # print(ids, landmrk)
            cx, cy = landmrk.x, landmrk.y
            # print(cx, cy)
            keypoint.append(cx)
            keypoint.append(cy)

    # print(keypoint)
    # print(len(keypoint))

    num = [2,0,0]
    keypoint = num + keypoint
    print(keypoint)
    # final_df = final_df.append(pd.DataFrame(keypoint))
    # print(final_df)


    with open('custom_keypoint.csv', 'a') as f_object:
 
        # Pass this file object to csv.writer()
        # and get a writer object
        writer_object = writer(f_object)
    
        # Pass the list as an argument into
        # the writerow()
        writer_object.writerow(keypoint)
    
        # Close the file object
        f_object.close()
        del f_object
        
    # return final_df
    del keypoint
    del image
    del results
    gc.collect()

def df_to_csv(dataframe):

    dataframe.to_csv('custom_keypoint.csv')

import sys
if __name__ == "__main__":
    processlandmarks(sys.argv[1])
