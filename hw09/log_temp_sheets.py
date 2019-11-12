#!/usr/bin/env python3
import smbus
import time
from os import system
from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import time, sys

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/spreadsheets'

# The ID and range of a sample spreadsheet.
SPREADSHEET_ID = 'BdrytnF5lPkVf8wl0qBTlypdmz2s07RfQ931bIhJ3B3d'
RANGE_NAME = 'A2'

def log_to_google_sheets(temp):
    store = file.Storage('tokenPython.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('sheets', 'v4', http=creds.authorize(Http()))

    # Call the Sheets API
    # Compute a timestamp and pass the first two arguments
    values = [ [time.time()/60/60/24+ 25569 - 4/24, temp]]
    body = { 'values': values }
    result = service.spreadsheets().values().append(spreadsheetId=SPREADSHEET_ID,
                            range=RANGE_NAME,
                            #  How the input data should be interpreted.
                            valueInputOption='USER_ENTERED',
                            # How the input data should be inserted.
                            # insertDataOption='INSERT_ROWS'
                            body=body
                            ).execute()
    
    updates = result.get('updates', [])
    # print(updates)

    if not updates:
        print('Not updated')



system("./setup.sh")
i2cbus = smbus.SMBus(2)
temp_addr = 0x48
bus.write_byte_data(temp_addr, 1, 0x60)
temp_old = None
while True:
    temp = bus.read_byte_data(address, 0)
    temp = temp*1.8 + 32

    if(temp != temp_old):
        log_to_google_sheets(temp1)
        temp_old = temp
    else:
        time.sleep(1)
