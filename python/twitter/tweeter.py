#!/usr/bin/env python

import sys
import tweepy

CONSUMER_KEY = 'GvCF4RA5wnB1W25FvOfWvA'
CONSUMER_SECRET = '4NCGsZV6qqIEi0Ux4EI2yY1neTWifnY3pAHANlm5k'
ACCESS_KEY = '1654721785-78Eqt2R5uLvghITw3ux7GarSdtMdNGmG3eOnAWw'
ACCESS_SECRET = 'v6Q1zEpTpLOCbpn5ZJDV8as71yrARitY5m3COxXA'


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
api.update_status(sys.argv[1])
