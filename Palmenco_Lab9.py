#Enter the num of rows
num_rows =int(input('Enter The number of rows: '))

row_number = 1 
triangle_row = ''


for row in range(1, num_rows + 1): 

    for column in range(row): 

      triangle_row += str(row_number) + ' ' 

      row_number += 1 

    print(triangle_row) 

    triangle_row = '' 