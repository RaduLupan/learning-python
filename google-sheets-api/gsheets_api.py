'''
-------------------------------------------------------------
This module contains functions to use with Google Sheets API.
-------------------------------------------------------------
'''

from __future__ import print_function

import google.auth

from googleapiclient.discovery import build    #  !!
from googleapiclient.errors import HttpError

from oauth2client.service_account import ServiceAccountCredentials  # !!

def get_values(creds, spreadsheet_id, range_name):
    try:
        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API.
        sheet = service.spreadsheets()

        result = sheet.values().get(
            spreadsheetId=spreadsheet_id, range=range_name).execute()
        rows = result.get('values', [])
        print(f"{len(rows)} rows retrieved")
        return rows
    except HttpError as error:
        print(f"An error occurred: {error}")
        return error

def append_values(creds, spreadsheet_id, range_name, value_input_option,
                  _values):
    try:
        service = build('sheets', 'v4', credentials=creds)

        values = [
            [
                # Cell values ...
            ],
            # Additional rows ...
        ]
        # [START_EXCLUDE silent]
        values = _values
        # [END_EXCLUDE]
        body = {
            'values': values
        }
        result = service.spreadsheets().values().append(
            spreadsheetId=spreadsheet_id, range=range_name,
            valueInputOption=value_input_option, body=body).execute()
        print(f"{(result.get('updates').get('updatedCells'))} cells appended.")
        return result

    except HttpError as error:
        print(f"An error occurred: {error}")
        return error

def create_sheet(creds,title,spreadsheet_id):
    try:
        service = build('sheets', 'v4', credentials=creds)
        
        batch_update_spreadsheet_request_body = {'requests':[{'addSheet': {'properties': {'title': title}}}]}
        
        request = service.spreadsheets().batchUpdate(spreadsheetId=spreadsheet_id, body=batch_update_spreadsheet_request_body)
        response = request.execute()
    except HttpError as error:
        print(f"An error occurred: {error}")
        return error

def update_sheet(creds, title, spreadsheet_id, data):
    try:
        service = build('sheets', 'v4', credentials=creds)
        
        batch_update_values_request_body = {"data":[{"majorDimension": "ROWS", "range": (title+"!A1"), "values": [data]}], "valueInputOption": "USER_ENTERED"}
        
        request = service.spreadsheets().values().batchUpdate(spreadsheetId=spreadsheet_id, body=batch_update_values_request_body)

        response = request.execute()
    except HttpError as error:
        print(f"An error occurred: {error}")
        return error
