"""
   Raspberry Pi Jam GSOC Photo Booth

"""
import json
from twython import Twython

# might want to change this to @GirlScoutsOC
# example message:  message = "Thanks for visiting our photobooth!  #WomenInSTEM @GirlScouts"

def TwitterPost(message):

    with open('credentials/twitteraccountauthentication.json') as json_file:
        dictKeys = json.load(json_file)
        twitter = Twython(dictKeys[consumer_key], dictKeys[consumer_secret], dictKeys[access_token], dictKeys[access_token_secret])
        try:
            image_open = open('picture_overlay.png', 'rb')
        except IOError as detail:
            print("** Couldn't find the PICTURE_OVERLAY.PNG file to send! ** %s" % detail)
        else:
            image_id = twitter.upload_media(media=image_open)
            twitter.update_status(status=message, media_ids=image_id['media_id'])
    
        del twitter
    
    return