import helperMethods
import math
import numpy as np
import helperMethods

def fist(hand_landmarks):
    """
    Determines if the hand is making a fist gesture.
    
    Args:
        hand_landmarks: A list of hand landmarks.  
    """
    for i in range(1, 21, 4):
        if(helperMethods.is_finger_straight(hand_landmarks, i, i+1, i+2, i+3)):
            return False
    return True

def index_point(hand_landmarks):
    """
    Determines if the hand is making an index point gesture.
    
    Args:
        hand_landmarks: A list of hand landmarks.  
    """
    if(helperMethods.is_finger_straight(hand_landmarks, 5, 6, 7, 8) and
       not helperMethods.is_finger_straight(hand_landmarks, 9, 10, 11, 12) and
       not helperMethods.is_finger_straight(hand_landmarks, 13, 14, 15, 16) and
       not helperMethods.is_finger_straight(hand_landmarks, 17, 18, 19, 20)):
        return True
    return False

def thumb_up(hand_landmarks):
    """
    Determines if the hand is making a thumb up gesture.
    
    Args:
        hand_landmarks: A list of hand landmarks.  
    """
    if(helperMethods.is_finger_straight(hand_landmarks, 1, 2, 3, 4) and
       not helperMethods.is_finger_straight(hand_landmarks, 5, 6, 7, 8) and
       not helperMethods.is_finger_straight(hand_landmarks, 9, 10, 11, 12) and
       not helperMethods.is_finger_straight(hand_landmarks, 13, 14, 15, 16) and
       not helperMethods.is_finger_straight(hand_landmarks, 17, 18, 19, 20)):
        return True
    return False

def peace(hand_landmarks):
    """
    Determines if the hand is making a peace gesture.
    
    Args:
        hand_landmarks: A list of hand landmarks.  
    """
    if(helperMethods.is_finger_straight(hand_landmarks, 5, 6, 7, 8) and
       helperMethods.is_finger_straight(hand_landmarks, 9, 10, 11, 12) and
       not helperMethods.is_finger_straight(hand_landmarks, 13, 14, 15, 16) and
       not helperMethods.is_finger_straight(hand_landmarks, 17, 18, 19, 20)):
        return True
    return False

def open(hand_landmarks):
    """
    Determines if the hand is making an open gesture.
    
    Args:
        hand_landmarks: A list of hand landmarks.  
    """
    for i in range(1, 21, 4):
        if(not helperMethods.is_finger_straight(hand_landmarks, i, i+1, i+2, i+3)):
            return False
    return True

def rock(hand_landmarks):
    """
    Determines if the hand is making a rock gesture.
    
    Args:
        hand_landmarks: A list of hand landmarks.  
    """
    if(helperMethods.is_finger_straight(hand_landmarks, 1, 2, 3, 4) and
       helperMethods.is_finger_straight(hand_landmarks, 5, 6, 7, 8) and
       not helperMethods.is_finger_straight(hand_landmarks, 9, 10, 11, 12) and
       not helperMethods.is_finger_straight(hand_landmarks, 13, 14, 15, 16) and
       helperMethods.is_finger_straight(hand_landmarks, 17, 18, 19, 20)):
        return True
    return False

def three(hand_landmarks):
    """
    Determines if the hand is making a three gesture.
    
    Args:
        hand_landmarks: A list of hand landmarks.  
    """
    if(not helperMethods.is_finger_straight(hand_landmarks, 1, 2, 3, 4) and
       helperMethods.is_finger_straight(hand_landmarks, 5, 6, 7, 8) and
       helperMethods.is_finger_straight(hand_landmarks, 9, 10, 11, 12) and
       helperMethods.is_finger_straight(hand_landmarks, 13, 14, 15, 16) and
       not helperMethods.is_finger_straight(hand_landmarks, 17, 18, 19, 20)):
        return True
    return False

def angle(a, b):
    return math.degrees(math.atan2(b.y - a.y, b.x - a.x))

def angle_diff(a1, a2):
    """Returns the smallest angle between two angles."""
    diff = abs(a1 - a2) % 360
    return min(diff, 360 - diff)

def angle_between_knuckles(hand_landmarks):
    """
    Calculates the angle between adjacent knuckles.

    Args:
        hand_landmarks: A list of hand landmarks.

    Returns:
        A list of angles (in degrees) between each pair of fingers.
    """
    finger_angles = [
        angle(hand_landmarks[2], hand_landmarks[3]),    # thumb
        angle(hand_landmarks[5], hand_landmarks[6]),    # index
        angle(hand_landmarks[9], hand_landmarks[10]),   # middle
        angle(hand_landmarks[13], hand_landmarks[14]),  # ring
        angle(hand_landmarks[17], hand_landmarks[18])   # pinky
    ]

    return [
        angle_diff(finger_angles[i], finger_angles[i + 1])
        for i in range(4)
    ]
    
def angle_between_tips(hand_landmarks):
    """
    Calculates the angle between adjacent fingertips.

    Args:
        hand_landmarks: A list of hand landmarks.

    Returns:
        A list of angles (in degrees) between each pair of fingertips.
    """
    finger_angles = [
        angle(hand_landmarks[2], hand_landmarks[4]),    # thumb
        angle(hand_landmarks[5], hand_landmarks[8]),    # index
        angle(hand_landmarks[9], hand_landmarks[12]),   # middle
        angle(hand_landmarks[13], hand_landmarks[16]),  # ring
        angle(hand_landmarks[17], hand_landmarks[20])   # pinky
    ]

    return [
        angle_diff(finger_angles[i], finger_angles[i + 1])
        for i in range(4)
    ]