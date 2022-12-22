import math

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

def create_item_dict(values, headers):
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

def write_csv(items, path):
    '''
    Writes the items (a list of dictionaries) to a CSV file.
    '''

    # Open the file in write mode.
    with open(path, 'w') as f:
        
        # Return if there is nothing to write.
        if len(items) == 0:
            return
        
        # Write the headers on the first line.
        headers = list(items[0].keys())
        f.write(','.join(headers) + '\n')

        # Write one item per line.
        for item in items:
            values = []

            for header in headers:
                values.append(str(item.get(header,"")))

            f.write(','.join(values) + '\n')

def loan_emi(amount, duration, rate, down_payment=0):
    ''''
    Calculates the equal montly installment (EMI) for a loan.
    Arguments: 
        amount - Total amount to be spent (loan + down payment)
        duration - Duration of the loan (in months)
        rate - Rate of interest (monthly)
        down_payment (optional) - Optional intial payment (deducted from amount)
    '''
    loan_amount = amount - down_payment
    
    try:
        emi = loan_amount * rate * ((1+rate)**duration) / (((1+rate)**duration)-1)
    except ZeroDivisionError:
        emi = loan_amount / duration
    
    emi = math.ceil(emi)
    
    return emi

def compute_emi(loans):
    '''
    Computes the Equal Monthly Installment (EMI) for a list of loans. Each loan is a dictionary.
    '''

    for loan in loans:
        loan['emi'] = loan_emi(amount = loan['amount'],
                               duration = loan['duration'],
                               rate = loan['rate'] /12, # the CSV contains yearly rates
                               down_payment = loan['down_payment'])



for i in range(1,4):
    loans_path = './data/loans{}.txt'.format(i)
    loans = read_csv(loans_path)
    print(f"Processing EMI for loans file: {loans_path}")
    compute_emi(loans)
    write_csv(loans, './data/emis{}.txt'.format(i))
