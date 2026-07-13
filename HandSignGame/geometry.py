import math
import numpy as np
from constants import STRAIGHTNESS_THRESHOLD

def distance(a, b):
    return math.hypot(a.x - b.x, a.y - b.y)

def is_finger_straight(hand, mcp, pip, dip, tip):
    return (
        distance(hand[tip], hand[mcp]) /
        (
            distance(hand[mcp], hand[pip]) +
            distance(hand[pip], hand[dip]) +
            distance(hand[dip], hand[tip])
        )
    ) > STRAIGHTNESS_THRESHOLD

def angle(*landmarks):
    points = np.array([[lm.x, lm.y] for lm in landmarks])

    center = points.mean(axis=0)
    centered = points - center

    _, _, vt = np.linalg.svd(centered)
    return vt[0]