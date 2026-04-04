# Screen Size
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
CENTER_X = SCREEN_WIDTH // 2
CENTER_Y = SCREEN_HEIGHT // 2

#Car specs
CAR_SPEED = 0
BLINK_SPEED = 20

#Signal specs
SIGNAL_WIDTH = 128
SIGNAL_GAP = 10 #pixels between the two signals
LEFT_X = CENTER_X - SIGNAL_WIDTH - SIGNAL_GAP // 2
RIGHT_X = CENTER_X + SIGNAL_GAP // 2
SIGNAL_Y = CENTER_Y - SIGNAL_WIDTH // 2 # Vertically centered

#Hazard signal specs
HAZARD_WIDTH = 65
HAZARD_X = CENTER_X - HAZARD_WIDTH // 2
HAZARD_Y = SIGNAL_Y + SIGNAL_WIDTH + 25 # Positioned below the turn signals