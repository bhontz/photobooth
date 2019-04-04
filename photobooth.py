"""
   Raspberry Pi Jam GSOC Photo Booth, code for Raspberry Pi

"""
import pygame, base64, os, sys, time
from pygame import camera
from pygame.locals import KEYDOWN, K_ESCAPE, K_SPACE
from GoogleCloudVision import GoogleCloudVision
from OverlayImages import *
from TwitterPost import TwitterPost
import Adafruit_MPR121.MPR121 as MPR121
from captouch import CapTouchHandler

class BreakIt(Exception): pass  # use this to break out of nested loops

strSaveImagePath = "/home/pi/photobooth/"  # this should be the script running point as well
strTwitterMessage = "Thank you for visiting the GSOC Photobooth! @GirlScoutsOC @OCFair #WomenInSTEM #Imaginology"
list_functions = [Landmarks, FlowerCrown, BrownieCap, EyeMask, FoxFace, DogFace, Mustache, Zorro, Alps, Cowboy, Emo]
list_overlay = [[], [flower_crown], [brownie_cap], [eye_mask], [fox_left_ear, fox_right_ear, fox_nose],\
    [dog_left_ear, dog_right_ear, dog_nose, dog_tongue], [mustache], [zorrohat, zorromask], [alps], [cowboy], [emo]]

pygame.init()
screen_size = (640, 480)
screen = pygame.display.set_mode(screen_size, 0)

pygame.camera.init()
camera = pygame.camera.Camera('/dev/video0', screen_size)
camera.start()
time.sleep(0.5)
snapshot = pygame.surface.Surface(screen_size, 0, screen)
# snapshot = pygame.image.load('/users/brad/my projects/girlscout-STEM/raspberry pi/picture.png')
dLandmarks = dict()
overlay_flag = False
twitter_flag = False

cap = MPR121.MPR121()
nbr_of_buttons = 3  # 0 = camera, 1 = overlay toggle, 2 = twitter
if not cap.begin():
    print("Error initializing MRP121, check your wiring!!.  Terminating.")
    sys.exit(-1)
last_touched = cap.touched()

try:
    while True:  # outer loop, come back from camera to here
        while True:
            events = pygame.event.get()
            for e in events:
                if (e.type == KEYDOWN and e.key == K_SPACE):
                    print("Exiting Photobooth!")
                    raise BreakIt
            
            e, last_touched = CapTouchHandler(cap, last_touched, 3)
            if e == 0:
                overlay_flag = True
                break
                
            snapshot = camera.get_image(snapshot)
            screen.blit(snapshot, (0,0))
            pygame.display.update()
            time.sleep(0.1)

        #### Out of Camera Loop
        if overlay_flag == True:
            pygame.image.save(snapshot, os.path.join(strSaveImagePath, 'picture.png'))
            pygame.draw.rect(snapshot, (0,255,0), (0,0,640,480), 8)  # use a frame to visually verify picture was taken ..
            screen.blit(snapshot, (0,0))
            pygame.display.update()

            #### Google Cloud Vision
            fp = open(os.path.join(strSaveImagePath, 'picture.png'), 'rb')
            dResponse = GoogleCloudVision(dLandmarks, fp)
            fp.close()
            del fp

            ### Overlay Process
            if any(dResponse):
                screen_overlay = screen.copy()
                ii = 0
                jj = -1
                while True:
                    if jj != ii:
                        list_functions[ii](dResponse, screen, list_overlay[ii])  # loop over the overlay functions ...
                        jj = ii

                    e, last_touched = CapTouchHandler(cap, last_touched, 3)
                    if e == 1:
                        ii += 1
                        if ii == len(list_functions):
                            ii = 0
                            jj = -1
                        screen.blit(screen_overlay, (0,0))
                        pygame.display.update()
                    elif e == 2:
                        screen.blit(pygame.image.load("overlays/twitter_logo.png"), (0,0))
                        pygame.display.update()
                        #TwitterPost(strTwitterMessage)
                        time.sleep(3)
                        break
                            

            time.sleep(5)
            overlay_flag = False
            pygame.event.clear()

except BreakIt:
    pass

camera.stop()
del camera
del snapshot
del screen
pygame.display.quit()
pygame.quit()