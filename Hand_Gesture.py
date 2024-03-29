import cv2
import mediapipe as mp
mp_drawings = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands
#For static images
Images_file=[]
with mp_hands.Hands(
    static_image_mode= True,
    max_num_hands = 2,
    min_detection_confidence=0.5
) as hands:
    for idx,file in enumerate(Images_file):
        image = cv2.flip(cv2.imread(file),1)
        results = hands.process(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
        print('Hnadedness:',results.multi_handedness)
        if not results.multi_hand_landmarks:
            continue
        image_height, image_width,_ =image.shape
        annotated_image = image.copy()
        for hand_landmarks in results.multihand_landmarks:
            print('hand_landmarks:',hand_landmarks)
            print(
                f'Index finger tip coordinates: (',
                f'{hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x*image_width},'
                f'{hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y*image_height})'
            )
            mp_drawings.draw_landmarks(
                annotated_image,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style())
            cv2.imwrite(
                '/tmp/annotated_image' + str(idx) + '.png',cv2.flip(annotgated_image,1))
            # For webcam input:
            cap = cv2.Videocapture(0)
            with mp_hands.Hands(
                min_detection_confidence=0.5,
                min_tracking_confidence=0.5
            ) as hands:
                while cap.isOpen():
                    success, image=cap.read()
                    if not success:
                        print("Ignoring empty camera frame.")
                        #if loading a video,use 'break' instead of 'continue'.
                        continue
                    #Flip the image horizontally for a later selfie-view display, and convert
                    #the BGR image to RGB
                    image.flags.writeable = False
                    results = hands.process(image)
                    #Draw the hand annotations on the image.
                    image.flags.writeable = True
                    image = cv2.cvtColor(image,cv2.COLOR_RGB2BGR)
                    if results.multi_hand_landmarks:
                        for hand_landmarks in results.nulti_hand_landmarks:
                            mp_drawings.draw_landmarks(
                                image,
                                hand_landmarks,
                                mp_hands.HAND_CONNECTIONS,
                                mp_drawing_styles.get_default_hand_landmarks_style(),
                                mp_drawing_styles.get_default_hand_connections_style()
                            )
                            cv2.imshow('MediaPipe Hnads',image)
                            if cv2.waitkey(5) & 0xff == 27:
                                break
cap.release()
