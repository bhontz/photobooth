"""
   Raspberry Pi Jam GSOC Photo Booth

    pygame.image.save(screen, "/users/brad/my projects/girlscout-STEM/raspberry pi/picture_overlay.png")

"""
import pygame, os, sys, time
from pygame.locals import *
from math import atan, cos, sin, sqrt, degrees, pow

flower_crown = pygame.image.load('overlays/flower_crown.png')
brownie_cap = pygame.image.load('overlays/brownie_cap.png')
eye_mask = pygame.image.load('overlays/eye_mask.png')
mustache = pygame.image.load('overlays/mustache.png')
fox_left_ear = pygame.image.load('overlays/fox_left_ear.png')
fox_right_ear = pygame.image.load('overlays/fox_right_ear.png')
fox_nose = pygame.image.load('overlays/fox_nose.png')
dog_left_ear = pygame.image.load('overlays/dog_left_ear.png')
dog_right_ear = pygame.image.load('overlays/dog_right_ear.png')
dog_nose = pygame.image.load('overlays/dog_nose.png')
dog_tongue = pygame.image.load('overlays/dog_tongue.png')
zorrohat = pygame.image.load('overlays/zorrohat.png')
zorromask = pygame.image.load('overlays/zorromask.png')
alps = pygame.image.load('overlays/alps.png')
cowboy = pygame.image.load('overlays/cowboy.png')
emo = pygame.image.load('overlays/emo.png')

def Landmarks(dlm, screen, ImageList):
    for v in dlm.values():
        x = (int(v[0]), int(v[1]))
        pygame.draw.circle(screen, (0,255,0), x, 6)

    pygame.display.update()
    return

def Zorro(dlm, screen, ImageList):
    hat = ImageList[0]
    mask = ImageList[1]
    
    overlay_image = ImageList[0]
    if dlm['LEFT_EYE_LEFT_CORNER'][1] >= dlm['RIGHT_EYE_RIGHT_CORNER'][1]:
        print("the left eye is lower ...")
        rise = dlm['LEFT_EYE_LEFT_CORNER'][1] - dlm['RIGHT_EYE_RIGHT_CORNER'][1]
        run = dlm['RIGHT_EYE_RIGHT_CORNER'][0] - dlm['LEFT_EYE_LEFT_CORNER'][0]
        angle = atan(rise / run)
        rotation = degrees(angle)
        DistanceBetweenEyes = sqrt(pow(rise, 2) + pow(run, 2))
        MidPointEyes = (dlm['LEFT_EYE_LEFT_CORNER'][0] + DistanceBetweenEyes / 2.0 * cos(angle), )
        MidPointEyes += (dlm['LEFT_EYE_LEFT_CORNER'][1] - DistanceBetweenEyes / 2.0 * sin(angle), )
        Crown = (MidPointEyes[0] - (DistanceBetweenEyes * 0.8 * cos(1.5708 - angle)), )
        Crown += (MidPointEyes[1] - (DistanceBetweenEyes * 0.8 * sin(1.5708 - angle)), )
        Mask = (MidPointEyes[0] - (cos(1.5708 - angle)), )
        Mask += (MidPointEyes[1] - (sin(1.5708 - angle)), )
    else:
        print("the right eye is lower ...")
        rise = dlm['RIGHT_EYE_RIGHT_CORNER'][1] - dlm['LEFT_EYE_LEFT_CORNER'][1]
        run = dlm['RIGHT_EYE_RIGHT_CORNER'][0] - dlm['LEFT_EYE_LEFT_CORNER'][0]        
        angle = atan(rise / run)
        rotation = degrees(angle) * -1.0
        DistanceBetweenEyes = sqrt(pow(rise, 2) + pow(run, 2))
        MidPointEyes = (dlm['RIGHT_EYE_RIGHT_CORNER'][0] - DistanceBetweenEyes / 2.0 * cos(angle), )
        MidPointEyes += (dlm['RIGHT_EYE_RIGHT_CORNER'][1] - DistanceBetweenEyes / 2.0 * sin(angle), )
        Crown = (MidPointEyes[0] + (DistanceBetweenEyes * 0.8 * cos(1.5708 - angle)), )
        Crown += (MidPointEyes[1] - (DistanceBetweenEyes * 0.8 * sin(1.5708 - angle)), )
        Mask = (MidPointEyes[0] - (cos(1.5708 - angle)), )
        Mask += (MidPointEyes[1] - (sin(1.5708 - angle)), )

    NewHeight = DistanceBetweenEyes * 1.5 * mask.get_height()  / mask.get_width() 
    mask = pygame.transform.smoothscale(mask, (int(DistanceBetweenEyes * 1.5), int(NewHeight)))   # the two settings here are from the flower crown analysis within the OverlayCalcs.xls spreadsheet
    rot_sprite = pygame.transform.rotate(mask, rotation)
    center = rot_sprite.get_rect().center
    screen.blit(rot_sprite, (Mask[0]-center[0], Mask[1]-center[1]))
    
    NewHeight = DistanceBetweenEyes * 3 * hat.get_height()  / hat.get_width() 
    hat = pygame.transform.smoothscale(hat, (int(DistanceBetweenEyes * 3), int(NewHeight)))   # the two settings here are from the flower crown analysis within the OverlayCalcs.xls spreadsheet
    rot_sprite = pygame.transform.rotate(hat, rotation)
    center = rot_sprite.get_rect().center
    screen.blit(rot_sprite, (Crown[0]-center[0], Crown[1]-center[1]))
    pygame.display.update()
    del rot_sprite
    
    return

def DogFace(dlm, screen, ImageList):
    l_ear  = ImageList[0]
    r_ear  = ImageList[1]
    nose   = ImageList[2]
    tongue = ImageList[3]
    
    if dlm['LEFT_EYE_LEFT_CORNER'][1] >= dlm['RIGHT_EYE_RIGHT_CORNER'][1]:
        print("the left eye is lower ...")
        rise = dlm['LEFT_EYE_LEFT_CORNER'][1] - dlm['RIGHT_EYE_RIGHT_CORNER'][1]
        run = dlm['RIGHT_EYE_RIGHT_CORNER'][0] - dlm['LEFT_EYE_LEFT_CORNER'][0]
        angle = atan(rise / run)
        rotation = degrees(angle)
        DistanceBetweenEyes = sqrt(pow(rise, 2) + pow(run, 2))
    else:
        print("the right eye is lower ...")
        rise = dlm['RIGHT_EYE_RIGHT_CORNER'][1] - dlm['LEFT_EYE_LEFT_CORNER'][1]
        run = dlm['RIGHT_EYE_RIGHT_CORNER'][0] - dlm['LEFT_EYE_LEFT_CORNER'][0]        
        angle = atan(rise / run)
        rotation = degrees(angle) * -1.0
        DistanceBetweenEyes = sqrt(pow(rise, 2) + pow(run, 2))

    NewHeight = DistanceBetweenEyes * nose.get_height()  / nose.get_width() 
    nose = pygame.transform.smoothscale(nose, (int(DistanceBetweenEyes), int(NewHeight)))   # the two settings here are from the flower crown analysis within the OverlayCalcs.xls spreadsheet
    rot_sprite = pygame.transform.rotate(nose, rotation)
    center = rot_sprite.get_rect().center
    screen.blit(rot_sprite, (dlm['NOSE_TIP'][0]-center[0], dlm['NOSE_TIP'][1]-center[1]))

    NewHeight = DistanceBetweenEyes * 0.75 * tongue.get_height()  / tongue.get_width() 
    tongue = pygame.transform.smoothscale(tongue, (int(DistanceBetweenEyes * 0.75), int(NewHeight)))   # the two settings here are from the flower crown analysis within the OverlayCalcs.xls spreadsheet
    rot_sprite = pygame.transform.rotate(tongue, rotation)
    center = rot_sprite.get_rect().center
    screen.blit(rot_sprite, (dlm['MOUTH_CENTER'][0]-center[0], dlm['MOUTH_CENTER'][1]))
    
    NewHeight = DistanceBetweenEyes * 0.75 * l_ear.get_height() / l_ear.get_width()
    l_ear = pygame.transform.smoothscale(l_ear, (int(DistanceBetweenEyes * 0.75), int(NewHeight)))                                                              
    rot_sprite = pygame.transform.rotate(l_ear, rotation)
    center = rot_sprite.get_rect().center
    newcenter = (center[0] + (int(rot_sprite.get_width() * 0.20)), center[1] + (int(rot_sprite.get_height() * 0.375)))   # .24 / .34 factors calculated externally
    screen.blit(rot_sprite, (dlm['LEFT_EAR_TRAGION'][0]-newcenter[0], dlm['LEFT_EAR_TRAGION'][1]-newcenter[1]))
    
    NewHeight = DistanceBetweenEyes * 0.75 * r_ear.get_height() / r_ear.get_width()
    r_ear = pygame.transform.smoothscale(r_ear, (int(DistanceBetweenEyes * 0.75), int(NewHeight)))                                                              
    rot_sprite = pygame.transform.rotate(r_ear, rotation)
    center = rot_sprite.get_rect().center
    newcenter = (center[0] - (int(rot_sprite.get_width() * 0.20)), center[1] + (int(rot_sprite.get_height() * 0.375)))
    screen.blit(rot_sprite, (dlm['RIGHT_EAR_TRAGION'][0]-newcenter[0], dlm['RIGHT_EAR_TRAGION'][1]-newcenter[1]))
    
    pygame.display.update()
    del rot_sprite
    
    return

def FoxFace(dlm, screen, ImageList):
    l_ear = ImageList[0]
    r_ear = ImageList[1]
    nose = ImageList[2]
    
    dlm['RIGHT_EAR_TRAGION'][0]
    
    if dlm['LEFT_EYE_LEFT_CORNER'][1] >= dlm['RIGHT_EYE_RIGHT_CORNER'][1]:
        print("the left eye is lower ...")
        rise = dlm['LEFT_EYE_LEFT_CORNER'][1] - dlm['RIGHT_EYE_RIGHT_CORNER'][1]
        run = dlm['RIGHT_EYE_RIGHT_CORNER'][0] - dlm['LEFT_EYE_LEFT_CORNER'][0]
        angle = atan(rise / run)
        rotation = degrees(angle)
        DistanceBetweenEyes = sqrt(pow(rise, 2) + pow(run, 2))
    else:
        print("the right eye is lower ...")
        rise = dlm['RIGHT_EYE_RIGHT_CORNER'][1] - dlm['LEFT_EYE_LEFT_CORNER'][1]
        run = dlm['RIGHT_EYE_RIGHT_CORNER'][0] - dlm['LEFT_EYE_LEFT_CORNER'][0]        
        angle = atan(rise / run)
        rotation = degrees(angle) * -1.0
        DistanceBetweenEyes = sqrt(pow(rise, 2) + pow(run, 2))

    NewHeight = DistanceBetweenEyes * nose.get_height()  / nose.get_width() 
    nose = pygame.transform.smoothscale(nose, (int(DistanceBetweenEyes), int(NewHeight)))   # the two settings here are from the flower crown analysis within the OverlayCalcs.xls spreadsheet
    rot_sprite = pygame.transform.rotate(nose, rotation)
    center = rot_sprite.get_rect().center
    screen.blit(rot_sprite, (dlm['NOSE_TIP'][0]-center[0], dlm['NOSE_TIP'][1]-center[1]))
    
    NewHeight = DistanceBetweenEyes * 0.75 * l_ear.get_height() / l_ear.get_width()
    l_ear = pygame.transform.smoothscale(l_ear, (int(DistanceBetweenEyes * 0.75), int(NewHeight)))                                                              
    rot_sprite = pygame.transform.rotate(l_ear, rotation)
    center = rot_sprite.get_rect().center
    newcenter = (center[0] + (int(rot_sprite.get_width() * 0.24)), center[1] + (int(rot_sprite.get_height() * 0.34)))   # .24 / .34 factors calculated externally
    screen.blit(rot_sprite, (dlm['LEFT_EAR_TRAGION'][0]-newcenter[0], dlm['LEFT_EAR_TRAGION'][1]-newcenter[1]))
    
    NewHeight = DistanceBetweenEyes * 0.75 * r_ear.get_height() / r_ear.get_width()
    r_ear = pygame.transform.smoothscale(r_ear, (int(DistanceBetweenEyes * 0.75), int(NewHeight)))                                                              
    rot_sprite = pygame.transform.rotate(r_ear, rotation)
    center = rot_sprite.get_rect().center
    newcenter = (center[0] - (int(rot_sprite.get_width() * 0.24)), center[1] + (int(rot_sprite.get_height() * 0.34)))
    screen.blit(rot_sprite, (dlm['RIGHT_EAR_TRAGION'][0]-newcenter[0], dlm['RIGHT_EAR_TRAGION'][1]-newcenter[1]))
    
    pygame.display.update()
    del rot_sprite
    
    return

def FlowerCrown(dlm, screen, ImageList):
    overlay_image = ImageList[0]
    if dlm['LEFT_EYE_LEFT_CORNER'][1] >= dlm['RIGHT_EYE_RIGHT_CORNER'][1]:
        print("the left eye is lower ...")
        rise = dlm['LEFT_EYE_LEFT_CORNER'][1] - dlm['RIGHT_EYE_RIGHT_CORNER'][1]
        run = dlm['RIGHT_EYE_RIGHT_CORNER'][0] - dlm['LEFT_EYE_LEFT_CORNER'][0]
        angle = atan(rise / run)
        rotation = degrees(angle)
        DistanceBetweenEyes = sqrt(pow(rise, 2) + pow(run, 2))
        MidPointEyes = (dlm['LEFT_EYE_LEFT_CORNER'][0] + DistanceBetweenEyes / 2.0 * cos(angle), )
        MidPointEyes += (dlm['LEFT_EYE_LEFT_CORNER'][1] - DistanceBetweenEyes / 2.0 * sin(angle), )
        Crown = (MidPointEyes[0] - (DistanceBetweenEyes * cos(1.5708 - angle)), )
        Crown += (MidPointEyes[1] - (DistanceBetweenEyes * sin(1.5708 - angle)), )
    else:
        print("the right eye is lower ...")
        rise = dlm['RIGHT_EYE_RIGHT_CORNER'][1] - dlm['LEFT_EYE_LEFT_CORNER'][1]
        run = dlm['RIGHT_EYE_RIGHT_CORNER'][0] - dlm['LEFT_EYE_LEFT_CORNER'][0]        
        angle = atan(rise / run)
        rotation = degrees(angle) * -1.0
        DistanceBetweenEyes = sqrt(pow(rise, 2) + pow(run, 2))
        MidPointEyes = (dlm['RIGHT_EYE_RIGHT_CORNER'][0] - DistanceBetweenEyes / 2.0 * cos(angle), )
        MidPointEyes += (dlm['RIGHT_EYE_RIGHT_CORNER'][1] - DistanceBetweenEyes / 2.0 * sin(angle), )
        Crown = (MidPointEyes[0] + (DistanceBetweenEyes * cos(1.5708 - angle)), )
        Crown += (MidPointEyes[1] - (DistanceBetweenEyes * sin(1.5708 - angle)), )
    
    NewHeight = DistanceBetweenEyes * 2.0 * overlay_image.get_height()  / overlay_image.get_width() 
    overlay_image = pygame.transform.smoothscale(overlay_image, (int(DistanceBetweenEyes * 2.0), int(NewHeight)))   # the two settings here are from the flower crown analysis within the OverlayCalcs.xls spreadsheet
    rot_sprite = pygame.transform.rotate(overlay_image, rotation)
    center = rot_sprite.get_rect().center
    screen.blit(rot_sprite, (Crown[0]-center[0], Crown[1]-center[1]))
    pygame.display.update()
    del rot_sprite
    
    return

def BrownieCap(dlm, screen, ImageList):
    overlay_image = ImageList[0]
    if dlm['LEFT_EYE_LEFT_CORNER'][1] >= dlm['RIGHT_EYE_RIGHT_CORNER'][1]:
        print("the left eye is lower ...")
        rise = dlm['LEFT_EYE_LEFT_CORNER'][1] - dlm['RIGHT_EYE_RIGHT_CORNER'][1]
        run = dlm['RIGHT_EYE_RIGHT_CORNER'][0] - dlm['LEFT_EYE_LEFT_CORNER'][0]
        angle = atan(rise / run)
        rotation = degrees(angle)
        DistanceBetweenEyes = sqrt(pow(rise, 2) + pow(run, 2))
        MidPointEyes = (dlm['LEFT_EYE_LEFT_CORNER'][0] + DistanceBetweenEyes / 2.0 * cos(angle), )
        MidPointEyes += (dlm['LEFT_EYE_LEFT_CORNER'][1] - DistanceBetweenEyes / 2.0 * sin(angle), )
        Crown = (MidPointEyes[0] - (DistanceBetweenEyes * 1.1 * cos(1.5708 - angle)), )
        Crown += (MidPointEyes[1] - (DistanceBetweenEyes * 1.1 * sin(1.5708 - angle)), )
    else:
        print("the right eye is lower ...")
        rise = dlm['RIGHT_EYE_RIGHT_CORNER'][1] - dlm['LEFT_EYE_LEFT_CORNER'][1]
        run = dlm['RIGHT_EYE_RIGHT_CORNER'][0] - dlm['LEFT_EYE_LEFT_CORNER'][0]        
        angle = atan(rise / run)
        rotation = degrees(angle) * -1.0
        DistanceBetweenEyes = sqrt(pow(rise, 2) + pow(run, 2))
        MidPointEyes = (dlm['RIGHT_EYE_RIGHT_CORNER'][0] - DistanceBetweenEyes / 2.0 * cos(angle), )
        MidPointEyes += (dlm['RIGHT_EYE_RIGHT_CORNER'][1] - DistanceBetweenEyes / 2.0 * sin(angle), )
        Crown = (MidPointEyes[0] + (DistanceBetweenEyes * 1.1 * cos(1.5708 - angle)), )
        Crown += (MidPointEyes[1] - (DistanceBetweenEyes * 1.1 * sin(1.5708 - angle)), )
    
    NewHeight = DistanceBetweenEyes * 1.5 * overlay_image.get_height()  / overlay_image.get_width() 
    overlay_image = pygame.transform.smoothscale(overlay_image, (int(DistanceBetweenEyes * 1.5), int(NewHeight)))   # the two settings here are from the flower crown analysis within the OverlayCalcs.xls spreadsheet
    rot_sprite = pygame.transform.rotate(overlay_image, rotation)
    center = rot_sprite.get_rect().center
    screen.blit(rot_sprite, (Crown[0]-center[0], Crown[1]-center[1]))
    pygame.display.update()
    del rot_sprite
    
    return

def Alps(dlm, screen, ImageList):
    overlay_image = ImageList[0]
    if dlm['LEFT_EYE_LEFT_CORNER'][1] >= dlm['RIGHT_EYE_RIGHT_CORNER'][1]:
        print("the left eye is lower ...")
        rise = dlm['LEFT_EYE_LEFT_CORNER'][1] - dlm['RIGHT_EYE_RIGHT_CORNER'][1]
        run = dlm['RIGHT_EYE_RIGHT_CORNER'][0] - dlm['LEFT_EYE_LEFT_CORNER'][0]
        angle = atan(rise / run)
        rotation = degrees(angle)
        DistanceBetweenEyes = sqrt(pow(rise, 2) + pow(run, 2))
        MidPointEyes = (dlm['LEFT_EYE_LEFT_CORNER'][0] + DistanceBetweenEyes / 2.0 * cos(angle), )
        MidPointEyes += (dlm['LEFT_EYE_LEFT_CORNER'][1] - DistanceBetweenEyes / 2.0 * sin(angle), )
        Crown = (MidPointEyes[0] - (DistanceBetweenEyes * 1.0 * cos(1.5708 - angle)), )
        Crown += (MidPointEyes[1] - (DistanceBetweenEyes * 1.0 * sin(1.5708 - angle)), )
    else:
        print("the right eye is lower ...")
        rise = dlm['RIGHT_EYE_RIGHT_CORNER'][1] - dlm['LEFT_EYE_LEFT_CORNER'][1]
        run = dlm['RIGHT_EYE_RIGHT_CORNER'][0] - dlm['LEFT_EYE_LEFT_CORNER'][0]        
        angle = atan(rise / run)
        rotation = degrees(angle) * -1.0
        DistanceBetweenEyes = sqrt(pow(rise, 2) + pow(run, 2))
        MidPointEyes = (dlm['RIGHT_EYE_RIGHT_CORNER'][0] - DistanceBetweenEyes / 2.0 * cos(angle), )
        MidPointEyes += (dlm['RIGHT_EYE_RIGHT_CORNER'][1] - DistanceBetweenEyes / 2.0 * sin(angle), )
        Crown = (MidPointEyes[0] + (DistanceBetweenEyes * 1.0 * cos(1.5708 - angle)), )
        Crown += (MidPointEyes[1] - (DistanceBetweenEyes * 1.0 * sin(1.5708 - angle)), )
    
    NewHeight = DistanceBetweenEyes * 2.0 * overlay_image.get_height()  / overlay_image.get_width() 
    overlay_image = pygame.transform.smoothscale(overlay_image, (int(DistanceBetweenEyes * 2.0), int(NewHeight)))   # the two settings here are from the flower crown analysis within the OverlayCalcs.xls spreadsheet
    rot_sprite = pygame.transform.rotate(overlay_image, rotation)
    center = rot_sprite.get_rect().center
    screen.blit(rot_sprite, (Crown[0]-center[0], Crown[1]-center[1]))
    pygame.display.update()
    del rot_sprite
    
    return

def Cowboy(dlm, screen, ImageList):
    overlay_image = ImageList[0]
    if dlm['LEFT_EYE_LEFT_CORNER'][1] >= dlm['RIGHT_EYE_RIGHT_CORNER'][1]:
        print("the left eye is lower ...")
        rise = dlm['LEFT_EYE_LEFT_CORNER'][1] - dlm['RIGHT_EYE_RIGHT_CORNER'][1]
        run = dlm['RIGHT_EYE_RIGHT_CORNER'][0] - dlm['LEFT_EYE_LEFT_CORNER'][0]
        angle = atan(rise / run)
        rotation = degrees(angle)
        DistanceBetweenEyes = sqrt(pow(rise, 2) + pow(run, 2))
        MidPointEyes = (dlm['LEFT_EYE_LEFT_CORNER'][0] + DistanceBetweenEyes / 2.0 * cos(angle), )
        MidPointEyes += (dlm['LEFT_EYE_LEFT_CORNER'][1] - DistanceBetweenEyes / 2.0 * sin(angle), )
        Crown = (MidPointEyes[0] - (DistanceBetweenEyes * 1.0 * cos(1.5708 - angle)), )
        Crown += (MidPointEyes[1] - (DistanceBetweenEyes * 1.0 * sin(1.5708 - angle)), )
    else:
        print("the right eye is lower ...")
        rise = dlm['RIGHT_EYE_RIGHT_CORNER'][1] - dlm['LEFT_EYE_LEFT_CORNER'][1]
        run = dlm['RIGHT_EYE_RIGHT_CORNER'][0] - dlm['LEFT_EYE_LEFT_CORNER'][0]        
        angle = atan(rise / run)
        rotation = degrees(angle) * -1.0
        DistanceBetweenEyes = sqrt(pow(rise, 2) + pow(run, 2))
        MidPointEyes = (dlm['RIGHT_EYE_RIGHT_CORNER'][0] - DistanceBetweenEyes / 2.0 * cos(angle), )
        MidPointEyes += (dlm['RIGHT_EYE_RIGHT_CORNER'][1] - DistanceBetweenEyes / 2.0 * sin(angle), )
        Crown = (MidPointEyes[0] + (DistanceBetweenEyes * 1.0 * cos(1.5708 - angle)), )
        Crown += (MidPointEyes[1] - (DistanceBetweenEyes * 1.0 * sin(1.5708 - angle)), )
    
    NewHeight = DistanceBetweenEyes * 2.5 * overlay_image.get_height()  / overlay_image.get_width() 
    overlay_image = pygame.transform.smoothscale(overlay_image, (int(DistanceBetweenEyes * 2.5), int(NewHeight)))   # the two settings here are from the flower crown analysis within the OverlayCalcs.xls spreadsheet
    rot_sprite = pygame.transform.rotate(overlay_image, rotation)
    center = rot_sprite.get_rect().center
    screen.blit(rot_sprite, (Crown[0]-center[0], Crown[1]-center[1]))
    pygame.display.update()
    del rot_sprite
    
    return

def Emo(dlm, screen, ImageList):
    overlay_image = ImageList[0]
    if dlm['LEFT_EYE_LEFT_CORNER'][1] >= dlm['RIGHT_EYE_RIGHT_CORNER'][1]:
        print("the left eye is lower ...")
        rise = dlm['LEFT_EYE_LEFT_CORNER'][1] - dlm['RIGHT_EYE_RIGHT_CORNER'][1]
        run = dlm['RIGHT_EYE_RIGHT_CORNER'][0] - dlm['LEFT_EYE_LEFT_CORNER'][0]
        angle = atan(rise / run)
        rotation = degrees(angle)
        DistanceBetweenEyes = sqrt(pow(rise, 2) + pow(run, 2))
        MidPointEyes = (dlm['LEFT_EYE_LEFT_CORNER'][0] + DistanceBetweenEyes / 2.0 * cos(angle), )
        MidPointEyes += (dlm['LEFT_EYE_LEFT_CORNER'][1] - DistanceBetweenEyes / 2.0 * sin(angle), )
        Crown = (MidPointEyes[0] - (DistanceBetweenEyes * 0.6 * cos(1.5708 - angle)), )
        Crown += (MidPointEyes[1] - (DistanceBetweenEyes * 0.6 * sin(1.5708 - angle)), )
    else:
        print("the right eye is lower ...")
        rise = dlm['RIGHT_EYE_RIGHT_CORNER'][1] - dlm['LEFT_EYE_LEFT_CORNER'][1]
        run = dlm['RIGHT_EYE_RIGHT_CORNER'][0] - dlm['LEFT_EYE_LEFT_CORNER'][0]        
        angle = atan(rise / run)
        rotation = degrees(angle) * -1.0
        DistanceBetweenEyes = sqrt(pow(rise, 2) + pow(run, 2))
        MidPointEyes = (dlm['RIGHT_EYE_RIGHT_CORNER'][0] - DistanceBetweenEyes / 2.0 * cos(angle), )
        MidPointEyes += (dlm['RIGHT_EYE_RIGHT_CORNER'][1] - DistanceBetweenEyes / 2.0 * sin(angle), )
        Crown = (MidPointEyes[0] + (DistanceBetweenEyes * 0.6 * cos(1.5708 - angle)), )
        Crown += (MidPointEyes[1] - (DistanceBetweenEyes * 0.6 * sin(1.5708 - angle)), )
    
    NewHeight = DistanceBetweenEyes * 2.5 * overlay_image.get_height()  / overlay_image.get_width() 
    overlay_image = pygame.transform.smoothscale(overlay_image, (int(DistanceBetweenEyes * 2.5), int(NewHeight)))   # the two settings here are from the flower crown analysis within the OverlayCalcs.xls spreadsheet
    rot_sprite = pygame.transform.rotate(overlay_image, rotation)
    center = rot_sprite.get_rect().center
    screen.blit(rot_sprite, (Crown[0]-center[0], Crown[1]-center[1]))
    pygame.display.update()
    del rot_sprite
    
    return


def EyeMask(dlm, screen, ImageList):
    overlay_image = ImageList[0]
    if dlm['LEFT_EYE_LEFT_CORNER'][1] >= dlm['RIGHT_EYE_RIGHT_CORNER'][1]:
        print("the left eye is lower ...")
        rise = dlm['LEFT_EYE_LEFT_CORNER'][1] - dlm['RIGHT_EYE_RIGHT_CORNER'][1]
        run = dlm['RIGHT_EYE_RIGHT_CORNER'][0] - dlm['LEFT_EYE_LEFT_CORNER'][0]
        angle = atan(rise / run)
        rotation = degrees(angle)
        DistanceBetweenEyes = sqrt(pow(rise, 2) + pow(run, 2))
        MidPointEyes = (dlm['LEFT_EYE_LEFT_CORNER'][0] + DistanceBetweenEyes / 2.0 * cos(angle), )
        MidPointEyes += (dlm['LEFT_EYE_LEFT_CORNER'][1] - DistanceBetweenEyes / 2.0 * sin(angle), )
        Mask = (MidPointEyes[0] - (DistanceBetweenEyes * 0.25 * cos(1.5708 - angle)), )
        Mask += (MidPointEyes[1] - (DistanceBetweenEyes * 0.25 * sin(1.5708 - angle)), )
    else:
        print("the right eye is lower ...")
        rise = dlm['RIGHT_EYE_RIGHT_CORNER'][1] - dlm['LEFT_EYE_LEFT_CORNER'][1]
        run = dlm['RIGHT_EYE_RIGHT_CORNER'][0] - dlm['LEFT_EYE_LEFT_CORNER'][0]        
        angle = atan(rise / run)
        rotation = degrees(angle) * -1.0
        DistanceBetweenEyes = sqrt(pow(rise, 2) + pow(run, 2))
        MidPointEyes = (dlm['RIGHT_EYE_RIGHT_CORNER'][0] - DistanceBetweenEyes / 2.0 * cos(angle), )
        MidPointEyes += (dlm['RIGHT_EYE_RIGHT_CORNER'][1] - DistanceBetweenEyes / 2.0 * sin(angle), )
        Mask = (MidPointEyes[0] - (DistanceBetweenEyes * 0.25 * cos(1.5708 - angle)), )
        Mask += (MidPointEyes[1] - (DistanceBetweenEyes * 0.25 * sin(1.5708 - angle)), )
    
    NewHeight = DistanceBetweenEyes * 2.0 * overlay_image.get_height()  / overlay_image.get_width() 
    overlay_image = pygame.transform.smoothscale(overlay_image, (int(DistanceBetweenEyes * 2.0), int(NewHeight)))   # the two settings here are from the flower crown analysis within the OverlayCalcs.xls spreadsheet
    rot_sprite = pygame.transform.rotate(overlay_image, rotation)
    center = rot_sprite.get_rect().center
    screen.blit(rot_sprite, (Mask[0]-center[0], Mask[1]-center[1]))
    pygame.display.update()
    del rot_sprite
    
    return


def Mustache(dlm, screen, ImageList):
    overlay_image = ImageList[0]
    if dlm['LEFT_EYE_LEFT_CORNER'][1] >= dlm['RIGHT_EYE_RIGHT_CORNER'][1]:
        print("the left eye is lower ...")
        rise = dlm['LEFT_EYE_LEFT_CORNER'][1] - dlm['RIGHT_EYE_RIGHT_CORNER'][1]
        run = dlm['RIGHT_EYE_RIGHT_CORNER'][0] - dlm['LEFT_EYE_LEFT_CORNER'][0]
        angle = atan(rise / run)
        rotation = degrees(angle)
        DistanceBetweenEyes = sqrt(pow(rise, 2) + pow(run, 2))
        MidPointEyes = (dlm['LEFT_EYE_LEFT_CORNER'][0] + DistanceBetweenEyes / 2.0 * cos(angle), )
        MidPointEyes += (dlm['LEFT_EYE_LEFT_CORNER'][1] - DistanceBetweenEyes / 2.0 * sin(angle), )
        Mustache = (dlm['UPPER_LIP'][0] - (DistanceBetweenEyes * 0.1 * cos(1.5708 - angle)), )
        Mustache += (dlm['UPPER_LIP'][1] + (DistanceBetweenEyes * 0.1 * sin(1.5708 - angle)), )
    else:
        print("the right eye is lower ...")
        rise = dlm['RIGHT_EYE_RIGHT_CORNER'][1] - dlm['LEFT_EYE_LEFT_CORNER'][1]
        run = dlm['RIGHT_EYE_RIGHT_CORNER'][0] - dlm['LEFT_EYE_LEFT_CORNER'][0]        
        angle = atan(rise / run)
        rotation = degrees(angle) * -1.0
        DistanceBetweenEyes = sqrt(pow(rise, 2) + pow(run, 2))
        MidPointEyes = (dlm['RIGHT_EYE_RIGHT_CORNER'][0] - DistanceBetweenEyes / 2.0 * cos(angle), )
        MidPointEyes += (dlm['RIGHT_EYE_RIGHT_CORNER'][1] - DistanceBetweenEyes / 2.0 * sin(angle), )
        Mustache = (dlm['UPPER_LIP'][0] - (DistanceBetweenEyes * 0.1 * cos(1.5708 - angle)), )
        Mustache += (dlm['UPPER_LIP'][1] + (DistanceBetweenEyes * 0.1 * sin(1.5708 - angle)), )
    
    NewHeight = DistanceBetweenEyes * 1.5 * overlay_image.get_height()  / overlay_image.get_width() 
    overlay_image = pygame.transform.smoothscale(overlay_image, (int(DistanceBetweenEyes * 1.5), int(NewHeight)))   # the two settings here are from the flower crown analysis within the OverlayCalcs.xls spreadsheet
    rot_sprite = pygame.transform.rotate(overlay_image, rotation)
    center = rot_sprite.get_rect().center
    screen.blit(rot_sprite, (Mustache[0]-center[0], Mustache[1]-center[1]))
    pygame.display.update()
    del rot_sprite
    
    return    

def OverlayProcess(dlm, screen):
    
    for k, v in dlm.iteritems():
        if k.find("EAR") >= 0 or k.find("NOSE") >= 0:
            print(k, v)
    
    screen_place_holder = screen.copy()
    list_functions = [Landmarks, FlowerCrown, BrownieCap, EyeMask, FoxFace, DogFace, Mustache, Zorro, Alps, Cowboy, Emo]
    list_overlay = [[], [flower_crown], [brownie_cap], [eye_mask], [fox_left_ear, fox_right_ear, fox_nose],\
        [dog_left_ear, dog_right_ear, dog_nose, dog_tongue], [mustache], [zorrohat, zorromask], [alps], [cowboy], [emo]]
    
    sendback = 0    
    i = 0
    j = -1
    
    while True:
        if j != i:
            list_functions[i](dlm, screen, list_overlay[i])
            j = i
        events = pygame.event.get()
        for e in events:
            if e.type == KEYDOWN and e.key == 273:
                print("Up arrow key was pressed")
                i += 1
                if i == len(list_functions):
                    i = 0
                    j = -1
                screen.blit(screen_place_holder, (0,0))
                pygame.display.update()
                ###list_functions[i](dlm, screen, list_overlay[i])

            elif e.type == KEYDOWN and e.key == 32:
                print("Twitter button (space) pressed, exiting OverlapProcess()")
                ## NEED TO SAVE THE SELECTED OVERLAP HERE!!! (note the screen overwrote it above)
                sendback = 18
                break

        if sendback != 0:
            break
            
            
    for lst in list_overlay:  # clean up image variables
        for l in lst:
            if l:
                del l
        
            
    return sendback
