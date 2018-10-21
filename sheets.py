from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/spreadsheets'

def getSheet(spreadsheet_id, range_name):
    """
    Fetches data from the Sheets API.
    Takes arguments (spreadsheet_id, range_name),
    Returns values from a spreadsheet.
    """
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('sheets', 'v4', http=creds.authorize(Http()))

    # Call the Sheets API
    result = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id,
                                                range=range_name).execute()
    values = result.get('values', [])
    
    if not values:
        print('No data found.')
    else:
        return values
    return None

def updateSheet(spreadsheet_id, range_name, value_range_body):
    """ 
    Update data from the Sheets API.
    Takes arguments (spreadsheet_id, range_name),
    Returns updated values from a spreadsheet.
    """
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('sheets', 'v4', http=creds.authorize(Http()))

    # Call the Sheets API
    result = service.spreadsheets().values().update(
        spreadsheetId=spreadsheet_id,
        range=range_name,
        valueInputOption='USER_ENTERED',
        body=value_range_body
        ).execute()
    values = result.get('values', [])
    
    if not values:
        print('No data found.')
    else:
        return values
    return None

if __name__ == '__main__':
    print('running sheets.py')
    # print(getSheet('1BNJKDTg_-c84h5BpSOkJTQOL4axuxCPB-rLaCbHAcfg', 'db!A2:J18'))
    # print(updateSheet(
    #     '1BNJKDTg_-c84h5BpSOkJTQOL4axuxCPB-rLaCbHAcfg',
    #     'store', { 'range': 'store', 'values': [[1, 2, 3], ['foo', 'bar', 'car']], }
    #     ))
