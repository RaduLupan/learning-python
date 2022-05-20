'''
------------------------------------------------------------------------
This exemple shows how to use Google Sheets API with a Service Account.
------------------------------------------------------------------------

References:
1: Learn Google Spreadsheets - Google Sheets - Python API, Read & Write Data: https://www.youtube.com/watch?v=4ssigWmExak&t=1671s
2: https://developers.google.com/sheets/api/quickstart/python
3: https://github.com/googleapis/google-api-python-client/tree/main/samples
4: https://github.com/googleworkspace/python-samples
'''

from __future__ import print_function

import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from oauth2client.service_account import ServiceAccountCredentials

def get_values(creds, spreadsheet_id, range_name):
    try:
        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API.
        request = service.spreadsheets().values().get(
            spreadsheetId=spreadsheet_id, 
            range=range_name
        )

        response = request.execute()

        rows = response.get('values', [])

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

def main():
    scopes = ['https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive']

    service_account_file = 'credentials.json'

    # The ID and range of a sample spreadsheet.
    sample_spreadsheet_id = '1z36C1xvQwrvrxyLlYIHx5wTZFt_BpOYi-q6DF_2B39g'
    sample_range_name = 'A1:A4'

    creds = ServiceAccountCredentials.from_json_keyfile_name(
        service_account_file,
        scopes,
    )

    # Get values from sample spreadsheet.
    result = get_values(creds, sample_spreadsheet_id, sample_range_name)
    print(result)

    # Append values to sample spreadsheet.
    result = append_values(creds, sample_spreadsheet_id, "A1:C2", "USER_ENTERED",
             [
                 ['F', 'B'],
                 ['C', 'D']
            ])
    print(result)

if __name__ == '__main__':
    main()
