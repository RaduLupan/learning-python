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
