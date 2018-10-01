from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/spreadsheets'

def getSheet(SPREADSHEET_ID, RANGE_NAME):
    """
    Fetches data from the Sheets API.
    Takes arguments (SPREADSHEET_ID, RANGE_NAME),
    Prints values from a spreadsheet.
    """
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('sheets', 'v4', http=creds.authorize(Http()))

    # Call the Sheets API
    result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID,
                                                range=RANGE_NAME).execute()
    values = result.get('values', [])
    
    if not values:
        print('No data found.')
    else:
        return values
    return None

if __name__ == '__main__':
    print(getSheet('1BNJKDTg_-c84h5BpSOkJTQOL4axuxCPB-rLaCbHAcfg', 'db!A2:J18'))
