"""
   Raspberry Pi Jam GSOC Photo Booth, code for Raspberry Pi

"""
import pygame, base64, os, sys, time, pickle
from math import atan, cos, sin, sqrt, degrees, pow
from pygame import camera
from pygame.locals import KEYDOWN
from GoogleCloudVision import GoogleCloudVision
from OverlayImages import OverlayProcess
from TwitterPost import TwitterPost

strSaveImagePath = "/home/pi/photobooth/"  # this should be the script running point as well
strTwitterMessage = "Thank you for visiting the GSOC Photobooth! @GirlScoutsOC @OCFair #WomenInSTEM #Imaginology"

pygame.init()
screen_size = (640, 480)
screen = pygame.display.set_mode(screen_size, 0)

###### Comment out next 5 lines if you're not using the camera
pygame.camera.init()
camera = pygame.camera.Camera('/dev/video0', screen_size)
camera.start()
time.sleep(0.5)
snapshot = pygame.surface.Surface(screen_size, 0, screen)
# snapshot = pygame.image.load('/users/brad/my projects/girlscout-STEM/raspberry pi/picture.png')

dLandmarks = dict()
overlay_flag = False
twitter_flag = False

while True:  # outer loop, come back from camera to here
	if overlay_flag == True:
		camera.start()

	while True:
		events = pygame.event.get()
		for e in events:
			if (e.type == KEYDOWN and e.key == 274):
				print("GOT DOWN ARROW!")
				overlay_flag = True
				break

		if overlay_flag == True:
			pygame.event.clear()
			break

	snapshot = camera.get_image(snapshot)   # Comment this line out if you're not using the camera
	screen.blit(snapshot, (0,0))
	pygame.display.update()
	time.sleep(0.5)
    
	#### Out of Camera Loop
    camera.stop()   # Comment this line out if you're not using the camera
    pygame.image.save(snapshot, os.path.join(strSaveImagePath, 'picture.png'))
    pygame.draw.rect(snapshot, (0,255,0), (0,0,640,480), 6)  # use a frame to visually verify picture was taken ..
    screen.blit(snapshot, (0,0))
    pygame.display.update()
    
    #### Google Cloud Vision
    fp = open(os.path.join(strSaveImagePath, 'picture.png'), 'rb')
    dResponse = GoogleCloudVision(dLandmarks, fp)
    fp.close()
    del fp
    
    ### Overlay Process
    i = OverlayProcess(dResponse, screen)
    time.sleep(5)
    
    if (i == 18):
		print("Twitter process started.")
		TwitterPost(strTwitterMessage)
		overlay_flag = False
	
    # if (i == 17):
	# 	print("Camera button pressed.")
	# 	overlay_flag = False

camera.stop()
del camera
pygame.display.quit()
del display
pygame.quit()
del snapshot
del screen
