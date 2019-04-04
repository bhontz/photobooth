"""
   Raspberry Pi Jam GSOC Photo Booth

"""
import base64, os, sys, time
from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

def GoogleCloudVision(dLandmarks, fp):
    sys.stdout.write("--------------------------------------------------------------\n")
    sys.stdout.write("Start of Google Cloud Vision Process: %s\n\n" % (time.strftime("%H:%M:%S", time.localtime())))

    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credentials/googlevisionauthentication.json"
    credentials = GoogleCredentials.get_application_default()
    service = discovery.build('vision', 'v1', credentials=credentials)
    image_content = base64.b64encode(fp.read())
    service_request = service.images().annotate(body={'requests':[{'image':{'content':image_content.decode('UTF-8')},'features':[{'type':'FACE_DETECTION','maxResults':10}]}]})

    dLandmarks = {}
    
    try:
        response = service_request.execute()
    except Exception as e:
        print("** COULDN'T CONNECT TO THE GOOGLE CLOUD, TRY AGAIN LATER! ** %s" % str(e))
        return dLandmarks

    try:
        dResponse = response['responses'][0]['faceAnnotations'][0]
    except KeyError as e:
        print("** TRY AGAIN - COULDN'T GET A GOOD LOOK AT YOUR EYES!!! ** %s" % str(e))
    else:
        for i in range(0, len(dResponse['landmarks'])):
            dLandmarks[dResponse['landmarks'][i]['type']] = (dResponse['landmarks'][i]['position']['x'], dResponse['landmarks'][i]['position']['y'])
        del dResponse

    del credentials
    del service
    del service_request
    
    sys.stdout.write("End of Google CloudVision Process: %s\n\n" % (time.strftime("%H:%M:%S", time.localtime())))
    sys.stdout.write("--------------------------------------------------------------\n")

    return dLandmarks
    
    
