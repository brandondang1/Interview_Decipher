# Interview_Decipher
Coding Exercise: Decoding a Secret Message

Problem
You are given a Google Doc like [this one](https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub) that contains a list of Unicode characters and their positions in a 2D grid. Your task is to write a function that takes in the URL for such a Google Doc as an argument, retrieves and parses the data in the document, and prints the grid of characters. When printed in a fixed-width font, the characters in the grid will form a graphic showing a sequence of uppercase letters, which is the secret message.

The document specifies the Unicode characters in the grid, along with the x- and y-coordinates of each character.

The minimum possible value of these coordinates is 0. There is no maximum possible value, so the grid can be arbitrarily large.

Any positions in the grid that do not have a specified character should be filled with a space character.

You can assume the document will always have the same format as the example document linked above.

For example, the simplified example document linked above draws out the letter 'F':

█▀▀▀

█▀▀ 

█   

Note that the coordinates (0, 0) will always correspond to the same corner of the grid as in this example, so make sure to understand in which directions the x- and y-coordinates increase.

Specifications
Your code must be written in Python (preferred) or JavaScript.

You may use external libraries.

You may write helper functions, but there should be one function that:

1. Takes in one argument, which is a string containing the URL for the Google Doc with the input data, AND

2. When called, prints the grid of characters specified by the input data, displaying a graphic of correctly oriented uppercase letters.

[TEST CASE](https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub) 

To begin decoding the secret message, I first needed to use external libraries to scrap the HTML from the google doc. Doing this would allow me to use the extract the data to be further processed in my code. 'Requests' was first used to send an HTTP request for the HTML where BeautifulSouip was used to parse over the HTML page, and extract the table. Following, I then append the data from the scraped table into a list to be worked on in Python. Subsequently, I remove the table headings seen in line 25. Line 28 I call to generate an empty grid filled with spaces. The 'make_grid' function looks to iterate over each set of data from the table, recording the greatest x and y coordinates. After this, a grid can then be created using 2 for loops with the largest coordinates. Line 31 then calls the 'fill_grid' funciton to go over the generated grid and fill in the unicode characters from the original data. Finally the 'print_grid' function prints out the final list in a readable format to decipher the secret message.
