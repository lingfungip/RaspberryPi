#!/usr/bin/env python

import sys
import os
from twython import Twython
from datetime import timedelta

FILE_PATH = '/Users/ling/Google Drive/MyCode/RaspberryPi'

# Import your Twitter application keys and the users OAuth tokens from file TwitterAPI.cfg in the FILE_PATH
twitterConfig = open(os.path.join(FILE_PATH, 'TwitterAPI.cfg'), 'r')
twitterAPIKey = twitterConfig.readlines()
twitterConfig.close()

# Assign application keys and user OAuth tokens to variable for easy debug
APP_KEY = twitterAPIKey[0].split('=')[1].strip()
APP_SECRET = twitterAPIKey[1].split('=')[1].strip()
OAUTH_TOKEN = twitterAPIKey[2].split('=')[1].strip()
OAUTH_TOKEN_SECRET = twitterAPIKey[3].split('=')[1].strip()

# Create a Twython instance with keys and tokens
twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

# Calculate uptime of the host
uptimeSec = open('/proc/uptime', 'r').readline().split()[0]
uptimeStatus = str(timedelta(seconds=float(uptimeSec)))

# Send twitter update status
twitter.update_status(status='This Raspberry Pi has been up for ' + uptimeStatus)
