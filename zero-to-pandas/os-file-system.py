def parse_headers(header_line):
    '''
    Returns a list of headers after stripping out the spaces, new line characters and commas.
    '''
    return header_line.strip().split(',')
