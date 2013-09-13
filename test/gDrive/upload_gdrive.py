#! /usr/bin/python
# Written by Peter Nichols to copy files to Google Drive. http://www.itdiscovery.info
# Sample file from http://planzero.org/blog/2012/04/13/uploading_any_file_to_google_docs_with_python
# Desired feature to grab all the kml/jpg files on the directory and dump them at once
# License: GPL 2.0

import sys, time, os.path, argparse
import atom.data, gdata.client, gdata.docs.client, gdata.docs.data


#parser = argparse.ArgumentParser(description='Python script that KML files and uploads them to Google Drive.')
#parser.add_argument('-u','--username', help='-u --username. Google Drive Username to Login as. Required!',required=True)
#parser.add_argument('-p','--password', help='-p --password. Google Drive Password to Login as. Required!',required=True)
#parser.add_argument('-l','--location', default='My Tracks', help='-l --location. [My Tracks] Google Drive Directory to store the KML files.',required=False)
#parser.add_argument('-f','--filename', help='-f --filename The file name/directory for the KML file.',required=True)
#parser.add_argument('-s', '--single', default=0, type=int, help= '-s --single [1] A single file [0] or all files [1] of that type in the directory', required=False)
#parser.add_argument('-m','--mimetype', default='jpg', choices=['kml','jpg','txt','csv','mpg','mp4'],help='-m --mimetype [jpg] The file type of the files: kml, jpg, txt, csv, mpg, mp4',required=False )
#args = parser.parse_args()

username = "rpi.fongming@gmail.com"
password = "Fongshek702"
collection = "rpi"
targetdir = "rpi-d27c111c.cfg" 

#Start the Google Drive Login
docsclient = gdata.docs.client.DocsClient(source='RPi Python-GData 2.0.17')

# Get a list of all available resources (GetAllResources() requires >= gdata-2.0.15)
print 'Logging in...',
try:
    docsclient.ClientLogin(username, password, docsclient.source);
except (gdata.client.BadAuthentication, gdata.client.Error), e:
    sys.exit('Unknown Error: ' + str(e))
except:
    sys.exit('Login Error, perhaps incorrect username/password')
print 'success!'

# The default root collection URI
#uri = 'https://docs.google.com/feeds/download/create-session/default/private/full'
# Get a list of all available resources (GetAllResources() requires >= gdata-2.0.15)
print 'Fetching Collection/Directory ID...',
try:
#   resources = docsclient.GetAllResources(uri='https://docs.google.com/feeds/default/private/full/-/folder?title=' + collection + '&title-exact=true')
   resources = docsclient.GetAllResources(uri='https://docs.google.com/feeds/default/private/full/-/file?title=' + collection + '&title-exact=true')
except:
   sys.exit('ERROR: Unable to retrieve resources')
# If no matching resources were found
if not resources:
   sys.exit('Error: The collection "' + collection + '" was not found.')
# Set the collection URI
uri = resources[0].get_resumable_create_media_link().href
print 'success!'
print uri

