#------------------------------------------------------------------------
# This exemple shows how to use Google Sheets API with a Service Account.
#------------------------------------------------------------------------

# References:
#------------

# 1: https://developers.google.com/sheets/api/quickstart/python
# 2: https://github.com/googleapis/google-api-python-client/tree/main/samples
# 3: https://github.com/googleworkspace/python-samples

from __future__ import print_function

import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.service_account import ServiceAccountCredentials

scopes = ['https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive']

service_account_file = 'credentials.json'

# The ID and range of a sample spreadsheet.
sample_spreadsheet_id = '1z36C1xvQwrvrxyLlYIHx5wTZFt_BpOYi-q6DF_2B39g'
sample_range_name = 'A1:A4'


def get_values(creds, spreadsheet_id, range_name):
    try:
        service = build('sheets', 'v4', credentials=creds)

        result = service.spreadsheets().values().get(
            spreadsheetId=spreadsheet_id, range=range_name).execute()
        rows = result.get('values', [])
        print(f"{len(rows)} rows retrieved")
        return result
    except HttpError as error:
        print(f"An error occurred: {error}")
        return error


def main():

    creds = ServiceAccountCredentials.from_json_keyfile_name(
        service_account_file,
        SCOPES,
    )

    result = get_values(creds, sample_spreadsheet_id, sample_range_name)
    print(result)

if __name__ == '__main__':
    main()

