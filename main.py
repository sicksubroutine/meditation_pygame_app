import time
import pygame
from gtts import gTTS

# Initialize the pygame modules
pygame.init()
pygame.font.init()
pygame.mixer.init()

# Set constants and starting values
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
WIDTH = 400
HEIGHT = 300
BG_COLOR = BLACK
pygame.display.set_caption("Mindful Meditation App")
icon = pygame.Surface((1, 1))
pygame.display.set_icon(icon)
window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

guided_phrases = [
  "The meditation is about to begin",
  "Find yourself a comfortable place to sit down",
  "Close your eyes and take a deep breath",
  "Focus on your breath and let go of any thoughts or worries",
  "Breathe in and out slowly and deeply",
  "There is only the breath", 
  "Let everything else drop away",
  "Let your body relax and release any tension",
  "If you find your mind wandering", 
  "gently bring the focus back to the breath",
  "Imagine a light shining in your heart", 
  "spreading warmth throughout your body",
  "Slowly scan your body for senentations", 
  "and just sit with them as you breath",
  "Listen to the sounds around you", 
  "and try to focus on each one in turn.",
  "Take a deep breath", 
  "and focus on the sensation of the breath", 
  "as it moves in and out of your body",
  "If you get distracted, gently bring your attention back to the breath.",
  "Let go of any judgments or expectations and simply allow yourself to be in the present moment.",
]

class Button:
    def __init__(self, x, y, width, height, text, font_size, inactive_color, active_color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.font_size = font_size
        self.inactive_color = inactive_color
        self.active_color = active_color
        self.is_clicked = False

    def draw(self, window):
        # Draw a rectanglular button with the specified dimensions and colors
        if self.is_clicked:
            pygame.draw.rect(window, self.active_color, [self.x, self.y, self.width, self.height])
        else:
            pygame.draw.rect(window, self.inactive_color, [self.x, self.y, self.width, self.height])

        # Create a font object and draw the text on the button
        font = pygame.font.Font(None, self.font_size)
        text_surface = font.render(self.text, True, BLACK)
        text_rect = text_surface.get_rect()
        text_rect.center = ((self.x + self.width / 2), (self.y + self.height / 2))
        window.blit(text_surface, text_rect)

    def check_click(self, pos):
        # Check if the button has been clicked
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                self.is_clicked = True

beginMeditation = Button(x=100, y=100, width=200, height=50, text="Begin Meditation", font_size=24, inactive_color=WHITE, active_color=RED)

exitButton = Button(x=100, y=200, width=200, height=50, text="Exit", font_size=24, inactive_color=WHITE, active_color=RED)

def text_to_speech(text):
    # Create a gTTS object and pass it the text to speak
    tts = gTTS(text, lang="en", tld="co.uk")
    tts.save("assets/temp.mp3")
    pygame.mixer.music.load("assets/temp.mp3")
    pygame.mixer.music.play()

def text_fade_in(text):
  alpha = 0
  fade_speed = 1
  font = pygame.font.Font(None, 20)
  text_surface = font.render(text, True, WHITE)
  text_surface.set_alpha(alpha)
  text_rect = text_surface.get_rect()
  text_rect.center = (WIDTH / 2, HEIGHT / 2)
  # Fade in the text
  while alpha < 255:
    window.fill(BG_COLOR)
    alpha += fade_speed
    text_surface.set_alpha(alpha)
    window.blit(text_surface, text_rect)
    pygame.display.update()
    clock.tick(60)
  # fade out the text  
  while alpha > 0:
    
    window.fill(BG_COLOR)
    alpha -= fade_speed
    text_surface.set_alpha(alpha)
    window.blit(text_surface, text_rect)
    pygame.display.update()
    clock.tick(60)

def ding_sound():
  while pygame.mixer.get_busy():
      continue
  pygame.mixer.music.load("assets/music.wav")
  pygame.mixer.music.play()

def meditationBegin():
  txt = guided_phrases[0]
  text_to_speech(txt)
  text_fade_in(txt)

  txt = guided_phrases[1]
  text_to_speech(txt)
  text_fade_in(txt)
  ding_sound()
  time.sleep(10)
  
  txt = guided_phrases[2]
  text_to_speech(txt)
  text_fade_in(txt)
  time.sleep(60)

  txt = guided_phrases[3]
  text_to_speech(txt)
  text_fade_in(txt)
  time.sleep(60)

  txt = guided_phrases[4]
  text_to_speech(txt)
  text_fade_in(txt)
  time.sleep(60)

  txt = guided_phrases[5]
  text_to_speech(txt)
  text_fade_in(txt)
  time.sleep(60)

  txt = guided_phrases[6]
  text_to_speech(txt)
  text_fade_in(txt)
  time.sleep(60)

  txt = guided_phrases[7]
  text_to_speech(txt)
  text_fade_in(txt)

  txt = guided_phrases[8]
  text_to_speech(txt)
  text_fade_in(txt)
  time.sleep(60)

  txt = guided_phrases[9]
  text_to_speech(txt)
  text_fade_in(txt)
  time.sleep(60)

  txt = guided_phrases[10]
  text_to_speech(txt)
  text_fade_in(txt)
  time.sleep(60)

  txt = guided_phrases[11]
  text_to_speech(txt)
  text_fade_in(txt)
  time.sleep(60)

while running:
  # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if beginMeditation.check_click(pos):
                pass
            if exitButton.check_click(pos):
                pass
        if event.type == pygame.MOUSEBUTTONUP:
          beginMeditation.is_clicked = False
          exitButton.is_clicked = False
    # game loop
    window.fill(BG_COLOR)
    beginMeditation.draw(window)
    exitButton.draw(window)
    pygame.display.update()
    if beginMeditation.is_clicked == True:
       meditationBegin()
    elif exitButton.is_clicked == True:
      running = False
      break
    clock.tick(60)
      
# Clean up
pygame.quit()