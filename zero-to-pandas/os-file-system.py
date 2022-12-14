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
