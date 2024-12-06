"""
    Author: Shaheer Mallick
    Revision Date: 6 December 2024
    Program: Making A Graphics Plotter - Turtle
    Description: A program to read points from a graphic data file
    and create a graphic based on the information read.
    Variable Dictionary: 
    - T: The turtle object used for drawing.
    - x, y: Coordinates where the point will be plotted.
    - d: Diameter of the point to be plotted.
    - color: Color of the point to be plotted.
    - filename: The name of the file containing the graphic data.
    - colorData: String containing the initial data line from the file.
    - values: List of values parsed from the initial data line.
    - cols: Number of columns in the graphic data.
    - rows: Number of rows in the graphic data.
    - numColors: Number of color definitions in the graphic data.
    - colorDefs: List of color definitions (symbol and color pairs).
    - sym: Symbol representing a color.
    - c: Placeholder variable for unused color component.
    - image_data: List of strings, each representing a row of the graphic.
    - color_dict: Dictionary mapping symbols to colors for plotting.
    - bg_color: Background color for the turtle canvas.
    - diameter: Diameter of the points to be plotted.
    - rotate: User input indicating whether to rotate the image 180 degrees.
    - canvas_width: Width of the turtle canvas.
    - canvas_height: Height of the turtle canvas.
    - x_offset: Offset to center the image on the x-axis.
    - y_offset: Offset to center the image on the y-axis.
"""

import turtle
#imports turtle

def plotIt(T, x, y, d, color):
    # T is the turtle object
    # (x, y) are the coordinates
    # d is the diameter of the point
    # color is the color of the point
    T.penup()  # Raise the pen to prevent drawing while moving
    T.goto(x, y)  # Move to the specified coordinates
    T.pendown()  # Lower the pen to start drawing
    T.dot(d, color)  # Draw a dot of specified diameter and color
    T.penup()  # Raise the pen again after drawing the dot

def readDataFile(filename):
#function to read data file
    fh = open(filename, "r")
    #opens and reads data file
    colorData = fh.readline().strip()
    #strips line for color data
    
    print(colorData)
    #prints color data
    
    # Adjust to handle the possibility of four values
    values = colorData.split()
    #splits color data to values
    if len(values) == 4:
    #if there are 4 values add an extra spot in values
        cols, rows, numColors, _ = values  
    else:
        cols, rows, numColors = values  # Handle the usual case
    
    cols, rows, numColors = int(cols), int(rows), int(numColors)
    #turns the numbers into integers
    
    # Initialize a list to store color definitions
    colorDefs = []
    #colorDefs is an empty array
    for i in range(numColors):
        colorData = fh.readline().strip()
        #reads each color definition line
        sym, c, color = colorData.split()
        #splits data into sym, c, color
        if sym == '~':
            sym = " "
            #converts tilde to space
        colorDefs.append([sym, color])
        #appends the symbol and color pair
    
    print(colorDefs)
    #prints the symbol color pair
    
    # Read the image data
    image_data = []
    for row in range(rows):
        line = fh.readline().rstrip()  
        # Read each line of the image data,             
        #removing trailing spaces
        if line:  
        # Skip empty lines
            image_data.append(line)
    
    fh.close()
    #closes file
    
    return cols, len(image_data), colorDefs, image_data
    # Return columns, actual rows, color definitions, and image data

def plotImage(t, cols, rows, color_defs, image_data, diameter):
    color_dict = {item[0]: item[1] for item in color_defs}
    # Convert color definitions array to dictionary for plotting

    x_offset = -cols // 2
    y_offset = rows // 2
    # Calculate the center of the canvas

    for y in range(len(image_data)):  # Use actual number of rows
        for x in range(cols):
            sym = image_data[y][x]  # Get the symbol at position (y, x)
            color = color_dict.get(sym, "gray40")  # Get the corresponding color or default to gray40
            plotIt(t, x + x_offset, y_offset - y, diameter, color)
                
def plotImage180(t, cols, rows, color_defs, image_data, diameter, rotate):
    color_dict = {item[0]: item[1] for item in color_defs}
    # Convert color definitions array to dictionary for plotting

    x_offset = -cols // 2
    y_offset = rows // 2
    # Calculate the center of the canvas

    for y in range(len(image_data)):  # Use actual number of rows
        for x in range(cols):
            sym = image_data[y][x]  # Get the symbol at position (y, x)
            color = color_dict.get(sym, "gray40")  # Get the corresponding color or default to gray40
            plotIt(t, -x - x_offset, -y_offset + y, diameter, color)
            #plots image 180 degrees rotated

try:
    filename = input("Enter the filename (e.g., smiley_emoji_mod.xpm): ")
    bg_color = input("Enter the background color (e.g., gray40): ")
    diameter = int(input("Enter the diameter of the points (e.g., 4): "))
    rotate = input("Would you like to rotate your image 180 degrees? (y/n): ")
    #asks for user input for each
except ValueError: 
    print("Invalid input")
    exit(1)
    #Value error causes exiting of program
except FileNotFoundError:
    print("File not found")
    exit(1)
    #File not found error causes exit


# Set up canvas size
canvas_width = 600 #Adjust as needed
canvas_height = 600  # Adjust as needed
turtle.setup(canvas_width, canvas_height)

turtle.bgcolor(bg_color)  # Set background color to user input
turtle.tracer(0, 0)  # Turn off screen updates for faster plotting
t = turtle.Turtle()
t.hideturtle()  # Hide the turtle icon

# Read the data file and plot the image
cols, rows, color_dict, image_data = readDataFile(filename)

if rotate == 'y':
    plotImage180(t, cols, rows, color_dict, image_data, diameter, rotate)    
    #plots 180 degrees if rotate = 'y'
else:
    plotImage(t, cols, rows, color_dict, image_data, diameter)

# Update the screen and finish
turtle.update()
turtle.done()


