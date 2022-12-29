'''
Exercise: Processing CSV files using a dictionary of lists
In this exercise, we'll transform the CSV data into a dictionary of lists instead, with one list for each column in the file.

For example, consider the following CSV file:

amount,duration,rate,down_payment
828400,120,0.11,100000
4633400,240,0.06,
42900,90,0.08,8900
983000,16,0.14,
15230,48,0.07,4300

We'll convert it into the following dictionary of lists:

{
  amount: [828400, 4633400, 42900, 983000, 15230],
  duration: []120, 240, 90, 16, 48],
  rate: [0.11, 0.06, 0.08, 0.14, 0.07],
  down_payment: [100000, 0, 8900, 0, 4300]
}

1. Download three CSV files to the folder data2 using the URLs listed in the code cell below, and verify the downloaded files.
2. Define a function read_csv_columnar that reads a CSV file and returns a dictionary of lists in the format shown above.
3. Define a function compute_emis that adds another key emi into the dictionary with a list of EMIs computed for each row of data.
4. Define a function write_csv_columnar that writes the data from the dictionary of lists into a correctly formatted CSV file.
5. Process all three downloaded files and write the results by creating new files in the directory data2.
'''

import os, math
from urllib.request import urlretrieve

def parse_headers(headers_line):
    return headers_line.strip().split(',')

def parse_values(values_line):
    values = []

    for item in values_line.strip().split(','):
        if item == "":
            values.append(0.0)
        else:
            try:
                values.append(float(item))
            except ValueError:
                values.append(item)
    return values

def create_dict_item(headers):
    '''
    Creates a dictionary of empty lists based on the keys read from the headers line. 
    '''
    result = {}
    for header in headers:
        result[header] = []
    return result

def read_csv_columnar(path):
    
    # Open the CSV file in read mode and read all lines.
    with open(path, 'r') as f:
        lines = f.readlines()
        
    # Parse the headers.
    headers = parse_headers(lines[0])
    
    # Create a dictionary of empty lists based on the headers as keys.
    result = create_dict_item(headers)
    
    # Parse each data line and append the values to the corresponding list in the result dictionary.
    for line in lines[1:]:
        values_line = parse_values(line)
        for header, value in zip(headers, values_line):
            result[header].append(value)
    
    return result

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

def compute_emis(loans):
    '''
    Adds an emi key to the dictionary of lists passed in the loans argument. Uses the loan_emi function to compute
    the emi for the loans.
    '''
    emi = []
    for amount, duration, rate, down_payment in zip(loans['amount'], loans['duration'], loans['rate'], loans['down_payment']):
        emi_item = loan_emi(amount = amount,
                       duration = duration,
                       rate = rate/12,
                       down_payment = down_payment)
        emi.append(emi_item)
    
    loans['emi'] = emi
    
    return loans

def write_csv_columnar(loans, path):
    '''
    Converts a dictionary of lists in to a list of lines representing headers and values and saves it as a CSV file. 
    '''
    headers_line = []
        
    for key in loans:
        headers_line.append(key)
    
    headers = ','.join(headers_line) + "\n"
    
    with open(path, 'w') as f:
        # Write the headers in the first line.
        f.write(headers)
        
        for amount, duration, rate, down_payment, emi in zip(loans['amount'], loans['duration'], loans['rate'], loans['down_payment'], loans['emi']):
            values_line = []
            values_line.append(str(amount))
            values_line.append(str(duration))
            values_line.append(str(rate))
            values_line.append(str(down_payment))
            values_line.append(str(emi))
            
            #print(values_line)
            
            # Write the values line in the CSV file.
            f.write(','.join(values_line) + "\n")

os.makedirs('./data2', exist_ok=True)

url1 = 'https://gist.githubusercontent.com/aakashns/257f6e6c8719c17d0e498ea287d1a386/raw/7def9ef4234ddf0bc82f855ad67dac8b971852ef/loans1.txt'
url2 = 'https://gist.githubusercontent.com/aakashns/257f6e6c8719c17d0e498ea287d1a386/raw/7def9ef4234ddf0bc82f855ad67dac8b971852ef/loans2.txt'
url3 = 'https://gist.githubusercontent.com/aakashns/257f6e6c8719c17d0e498ea287d1a386/raw/7def9ef4234ddf0bc82f855ad67dac8b971852ef/loans3.txt'

urls = [url1, url2, url3]

# Download all files in the data2 folder.
for i, url in enumerate(urls):
    urlretrieve(url, './data2/loans{}.txt'.format(i+1))
