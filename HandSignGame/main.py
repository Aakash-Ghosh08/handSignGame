import cv2
import mediapipe as mp
import helperMethods
import pygame
import handsigns
import player
from constants import WIDTH, HEIGHT

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
player1 = player.player(WIDTH // 4, HEIGHT // 2, (0, 0, 255), "Player 1")
player2 = player.player(3 * WIDTH // 4, HEIGHT // 2, (0, 255, 0), "Player 2")

mp_hands = mp.solutions.hands

hands = mp_hands.Hands(
    max_num_hands=2,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.5
)

mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    success, frame = cap.read()
    if not success:
        break
    
    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)
    if results.multi_hand_landmarks:
        for hand in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(
                frame,
                hand,
                mp_hands.HAND_CONNECTIONS
            )
            if(hand.landmark[0].x < 0.5):
                player1.deactivate_shield()
                if(handsigns.fist(hand.landmark)):
                    player1.activate_shield()
                    if(not player1.handSigns or player1.handSigns[-1] != "fist"):
                        player1.handSigns.append("fist")
                elif(handsigns.open(hand.landmark)):
                    if(not player1.handSigns or player1.handSigns[-1] != "open"):
                        player1.handSigns.append("open")
                elif(handsigns.peace(hand.landmark)):
                    player1.attack(helperMethods.angle(hand.landmark[5], hand.landmark[6], hand.landmark[7], hand.landmark[8]))
                elif(handsigns.index_point(hand.landmark)):
                    player1.move(helperMethods.angle(hand.landmark[5], hand.landmark[6], hand.landmark[7], hand.landmark[8]))
                elif(handsigns.rock(hand.landmark)):
                    player1.heal(1)
            else:
                player2.deactivate_shield()
                if(handsigns.fist(hand.landmark)):
                    player2.activate_shield()
                    if(not player2.handSigns or player2.handSigns[-1] != "fist"):
                        player2.handSigns.append("fist")
                elif(handsigns.open(hand.landmark)):
                    if(not player2.handSigns or player2.handSigns[-1] != "open"):
                        player2.handSigns.append("open")
                elif(handsigns.peace(hand.landmark)):
                    player2.attack(helperMethods.angle(hand.landmark[5], hand.landmark[6], hand.landmark[7], hand.landmark[8]))
                elif(handsigns.index_point(hand.landmark)):
                    player2.move(helperMethods.angle(hand.landmark[5], hand.landmark[6], hand.landmark[7], hand.landmark[8]))
                elif(handsigns.rock(hand.landmark)):
                    player2.heal(1)
    screen.fill((255, 255, 255))
    player1.update(player2)
    player2.update(player1)
    player1.draw(screen)
    player2.draw(screen)
    if(player1.isDead):
        font = pygame.font.Font(None, 74)
        text = font.render("Player 2 Wins!", True, (0, 0, 0))
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
    elif(player2.isDead):
        font = pygame.font.Font(None, 74)
        text = font.render("Player 1 Wins!", True, (0, 0, 0))
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
    pygame.display.flip()
    cv2.imshow("Hand Tracker", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
hands.close()
pygame.quit()
cv2.destroyAllWindows()