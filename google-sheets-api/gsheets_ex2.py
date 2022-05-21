'''
---------------------------------------------------------------------------------------------
This exemple shows how to use Google Sheets API with functions defined in an external module.
---------------------------------------------------------------------------------------------

References:
1: Learn Google Spreadsheets - Google Sheets - Python API, Read & Write Data: https://www.youtube.com/watch?v=4ssigWmExak&t=1671s
2: https://developers.google.com/sheets/api/quickstart/python
3: https://github.com/googleapis/google-api-python-client/tree/main/samples
4: https://github.com/googleworkspace/python-samples
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

    # Create new sheet in the existing spreadsheet.
    gsheets_api.create_sheet(creds=creds, title='My New Sheet', spreadsheet_id=sample_spreadsheet_id)

    # Update newly created sheet with data from a list.
    sample_data=['Name','Company','Address']
    gsheets_api.update_sheet(creds, title = 'My New Sheet', spreadsheet_id=sample_spreadsheet_id, data=sample_data)

if __name__ == '__main__':
    main()
