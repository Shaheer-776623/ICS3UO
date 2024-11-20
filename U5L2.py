filename = "smiley_emoji_mod.xpm"
fh = open(filename, "r") 
colorData = fh.readline()
colorData = colorData.strip()

print(colorData)

rows, cols, numColors = colorData.split()

numColors = int(numColors)

for i in range(numColors):
   colorLine = fh.readline()
   colorLine.strip() # gets rid of the carriage return
   sym, c, color = colorLine.split()

print(colorLine.split())

# Using arrays
colorDefs = [[0] * 2] * numColors # declare the array
for i in range(numColors):
   colorLine = fh.readline() # file handle must be open
   colorLine.strip() 
   sym, c, color = colorLine.split()
   # you need to insert code here to exchange
   # the tilde (~) for a space in the symbols!
   colorDefs[i][0] = sym
   colorDefs[i][1] = color

fh.close()
