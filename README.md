**GSOC Raspberry Pi Photobooth**

Created as a STEM table display activity to illustrate cool STEM projects that Girl Scouts can do!

Designed to run on a Raspberry Pi with a USB camera.  This can be easily converted to the Raspberry Pi camera; I just didn't have access to one.

There are three "buttons" which are really homemade aluminum foil "touch" objects that use the Adafruit MPR121 library and the Adafruit capacitive touch sensor.

Button 1 snaps a picture, button 2 toggles through "Snapchat like" overlays, and button 3 sends the toggled image to Twitter.

Use some arts and crafts skills to make the buttons look like a camera, and the twitter logo!

**Installation:**

From the Raspberry Pi's terminal, first change to folder /home/pi.  

Next, use github to clone this project to your raspberry pi as follows:

    sudo git clone https://github.com/bhontz/photobooth


Change into the photobooth folder (created by the process above) and run the shell script:

    cd photobooth

    sudo sh photoboothsetup.sh

The script will install (or try to) the python modules required by this project as well as the "overlay images" used within the project.

**IMPORTANT:**
This project utilizes the GoogleVision API as well as a Twitter account.   As this is a public respository, I did not provide the authentication files required to use the GoogleVision or Twitter accounts associated with the code within.

Therefore, **_you need to provide_** a GoogleAppCredentials JSON file (see: https://cloud.google.com/docs/authentication/production) and a similar Twitter credentials JSON file with the structure:

{"consumer_key": strValue, "consumer_secret": strValue, "access_token": strValue, "access_token_secret": strValue}

These files need to be named googlevisionauthentication.json and twitteraccountauthentication.json, and both files need to reside within the /home/pi/photobooth/credentials folder. This folder is created by the scripting process mentioned above.  The scripting process additionally creates two "template files" with these filenames which the appropriate authentication values can be added to. 

**Usage:**

First be sure that the USB camera is connected, and that you have alligator clip connections between the three "buttons" and the Adafruit capacitive touch sensor pins 0, 1 and 2 (picture = 0, overlays = 1, twitter = 2).

You need these connections in place PRIOR TO POWERING ON the Raspberry Pi, as the capacitive touch sensor calibrates on power up.
 
Next, from the Raspberry Pi's terminal, change to folder /home/pi/photobooth and then execute the command:

    python3 photobooth.py

You should see the camera's image on the monitor after a second or two; once you do you're read to go!  Start inviting people over to visit the booth!





  