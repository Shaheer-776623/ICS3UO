"""
    Author: Shaheer Mallick
    Revision Date: 6 December 2024
    Program: Making A Graphis Plotter - Turtle
    Description: A program to read points on a graphic data file
    and create a garaphic based on the information read.
    Variable Dictionary: 
  
"""
import turtle

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
    fh = open(filename, "r")
    colorData = fh.readline().strip()
    
    print(colorData)
    
    # Adjust to handle the possibility of four values
    values = colorData.split()
    if len(values) == 4:
        cols, rows, numColors, _ = values  # Ignore the fourth value
    else:
        cols, rows, numColors = values  # Handle the usual case
    
    cols, rows, numColors = int(cols), int(rows), int(numColors)
    
    # Initialize a list to store color definitions
    colorDefs = []
    for i in range(numColors):
        colorData = fh.readline().strip()
        sym, c, color = colorData.split()
        if sym == '~':
            sym = " "
        colorDefs.append([sym, color])
    
    print(colorDefs)
    
    # Read the image data
    image_data = []
    for _ in range(rows):
        line = fh.readline().rstrip()  # Read each line of the image data, removing trailing spaces
        if line:  # Skip empty lines
            image_data.append(line)
    
    fh.close()
    
    # Return columns, actual rows, color definitions, and image data
    return cols, len(image_data), colorDefs, image_data

def plotImage(t, cols, rows, color_defs, image_data, diameter):
    # Convert color definitions array to dictionary for plotting
    color_dict = {item[0]: item[1] for item in color_defs}

    # Calculate the center of the canvas
    x_offset = -cols // 2
    y_offset = rows // 2

    for y in range(len(image_data)):  # Use actual number of rows
        for x in range(cols):
            sym = image_data[y][x]  # Get the symbol at position (y, x)
            color = color_dict.get(sym, "gray40")  # Get the corresponding color or default to gray40
            plotIt(t, x + x_offset, y_offset - y, diameter, color)
                
def plotImage180(t, cols, rows, color_defs, image_data, diameter, rotate):
    # Convert color definitions array to dictionary for plotting
    color_dict = {item[0]: item[1] for item in color_defs}

    # Calculate the center of the canvas
    x_offset = -cols // 2
    y_offset = rows // 2

    for y in range(len(image_data)):  # Use actual number of rows
        for x in range(cols):
            sym = image_data[y][x]  # Get the symbol at position (y, x)
            color = color_dict.get(sym, "gray40")  # Get the corresponding color or default to gray40
            plotIt(t, -x - x_offset, -y_offset + y, diameter, color)
                


# Main execution
filename = input("Enter the filename (e.g., smiley_emoji_mod.xpm): ")
bg_color = input("Enter the background color (e.g., gray40): ")
diameter = int(input("Enter the diameter of the points (e.g., 4): "))
rotate = input("Would you like to rotate your image 180 degrees? (y/n): ")

# Set up canvas size
canvas_width = 1000 #Adjust as needed
canvas_height = 1000  # Adjust as needed
turtle.setup(canvas_width, canvas_height)

turtle.bgcolor(bg_color)  # Set background color to user input
turtle.tracer(0, 0)  # Turn off screen updates for faster plotting
t = turtle.Turtle()
t.hideturtle()  # Hide the turtle icon

# Read the data file and plot the image
cols, rows, color_dict, image_data = readDataFile(filename)

if rotate == 'y':
    plotImage180(t, cols, rows, color_dict, image_data, diameter, rotate)    
else:
    plotImage(t, cols, rows, color_dict, image_data, diameter)

# Update the screen and finish
turtle.update()
turtle.done()


