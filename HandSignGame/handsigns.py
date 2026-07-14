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