'''
---------------------------------------------------------------------------------------------
This exemple shows how to use Google Sheets API with functions defined in an external module.
---------------------------------------------------------------------------------------------

References:
1: https://developers.google.com/sheets/api/quickstart/python
2: https://github.com/googleapis/google-api-python-client/tree/main/samples
3: https://github.com/googleworkspace/python-samples
'''

import gsheets_api

def main():
    scopes = ['https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive']

    service_account_file = 'credentials.json'

    # The ID and range of a sample spreadsheet.
    sample_spreadsheet_id = '1z36C1xvQwrvrxyLlYIHx5wTZFt_BpOYi-q6DF_2B39g'
    sample_range_name = 'A1:A4'

    creds = gsheets_api.ServiceAccountCredentials.from_json_keyfile_name(
        service_account_file,
        scopes,
    )

    # Get values from sample spreadsheet.
    result = gsheets_api.get_values(creds, sample_spreadsheet_id, sample_range_name)
    print(result)

    # Append values to sample spreadsheet.
    result = gsheets_api.append_values(creds, sample_spreadsheet_id, "A1:C2", "USER_ENTERED",
             [
                 ['F', 'B'],
                 ['C', 'D']
            ])
    print(result)

if __name__ == '__main__':
    main()
