import firebase_admin
import linecache
from firebase_admin import credentials, firestore, storage, db
import os
import re

#Firebase credentials
cred=credentials.Certificate('./serviceAccountKey.json')
firebase_admin.initialize_app(cred, {
    'storageBucket': 'blackbox-57b40.appspot.com',
    'databaseURL': 'https://blackbox-57b40-default-rtdb.firebaseio.com/'
})

bucket = storage.bucket()
ref = db.reference('/')
homerefPto = ref.child('photo')
homerefVid = ref.child('video')


#Store jpg file in firebase storage
def storePhotoFb(fileLoc):
    filename=os.path.basename(fileLoc)
    blob = bucket.blob(filename)
    outfile=fileLoc
    blob.upload_from_filename(outfile)


#Push photo data to firebase database
def pushPhotoDb(fileLoc, time):
    #Initialise variables for location data 
    gpsDataFile = './gps.txt'
    lat = re.sub('[\n]', '', linecache.getline(gpsDataFile, 1))
    long = re.sub('[\n]', '', linecache.getline(gpsDataFile, 2))
    alt = re.sub('[\n]', '', linecache.getline(gpsDataFile, 3))
    speed = re.sub('[\n]', '', linecache.getline(gpsDataFile, 4))
    filename=os.path.basename(fileLoc)
    #Push file reference to image in Realtime DB
    homerefPto.push({
        'image': filename,
        'timestamp': time,
        'lat' : lat,
        'long' : long,
        'alt' : alt,
        'speed' : speed
        }
    )

#################

#Store mp4 file in firebase storage
def storeVidFb(fileLoc):
    filename=os.path.basename(fileLoc)
    blob = bucket.blob(filename)
    outfile=fileLoc
    blob.upload_from_filename(outfile)

#Push video data to firebase database
def pushVidDb(fileLoc, time):
    #Initialise variables for location data 
    gpsDataFile = './gps.txt'
    lat = re.sub('[\n]', '', linecache.getline(gpsDataFile, 1))
    long = re.sub('[\n]', '', linecache.getline(gpsDataFile, 2))
    alt = re.sub('[\n]', '', linecache.getline(gpsDataFile, 3))
    speed = re.sub('[\n]', '', linecache.getline(gpsDataFile, 4))
    filename=os.path.basename(fileLoc)
    #Push file reference to image in Realtime DB
    homerefVid.push({
        'vid': filename,
        'timestamp': time,
        'lat' : lat,
        'long' : long,
        'alt' : alt,
        'speed' : speed
        }
    )

