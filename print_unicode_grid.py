import requests
from bs4 import BeautifulSoup

def decode_secret_message(url):

    page = requests.get(url)

    #Parsing
    soup = BeautifulSoup(page.text, 'html.parser')

    #Find the table
    table = soup.find('table')

    #print(table)

    data = []

    # Extract data from the table
    for row in table.find_all('tr'):
        columns = row.find_all(['td']) #'th', 
        #print([column.text for column in columns])

        data.append([column.text for column in columns])

    del data[0]
    #print(data)

    grid = make_grid(data) 
    #print(grid)

    fill_grid(grid, data)

    print(grid)
    print_grid(grid)
    

def make_grid(data):

    max_x = 0
    max_y = 0
    grid = []

    for element in data:
        if int(element[0]) > max_x:
            max_x = int(element[0])
        if int(element[2]) > max_y:
            max_y = int(element[2])

    #print(max_x)
    #print(max_y)

    for col in range(max_y + 1):

        value = []

        for row in range(max_x + 1): 

            value.append(" ")

        grid.append(value)

    return grid

def fill_grid(grid, data):

    for element in data:

        grid[int(element[2])][int(element[0])] = element[1]

    return grid.reverse()

def print_grid(grid):

    for row in range (len(grid)):

        decipher = ""

        for element in grid[row]:

            decipher += element

        print(decipher)

"""
# Function to handle colspan and rowspan
def extract_cell_data(cell):
    colspan = int(cell.get('colspan', 1))
    rowspan = int(cell.get('rowspan', 1))
    return [cell.text] * colspan, rowspan
"""



#url = 'https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub'

url = 'https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub'

decode_secret_message(url)

