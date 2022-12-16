def parse_headers(header_line):
    '''
    Returns a list of headers after stripping out the spaces, new line characters and commas.
    '''
    return header_line.strip().split(',')

def parse_values(data_line):
    '''
    Returns a list of values from a comma separated data line.
    '''
    values = []

    for item in data_line.strip().split(','):
        if item == "":
            values.append(0.0)
        else:
            try:
                values.append(float(item))
            except ValueError:
                values.append(item)
    return values

def creat_item_dict(values, headers):
    '''
    Creates a dictionary with the keys passed in the headers argument and values passed in the values argument.
    '''
    result = {}

    for value, header in zip(values, headers):
        result[header] = value
    
    return result

def read_csv(path):
    '''
    Reads lines from CSV file and returns a list of dictionaries representing each line.
    '''

    result = []

    # Open the file in read mode.
    with open(path, 'r') as f:
        lines = f.readlines()

    # Parse the headers.
    headers = parse_headers(lines[0])

    # Parse the remaining lines.
    for data_line in lines[1:]:
        # Parse the values.
        values = parse_values(data_line)
        # Create dictionary.
        item_dict = create_item_dict(values, headers)
        # Add dictionary to the result.
        result.append(item_dict)
    
    return result
