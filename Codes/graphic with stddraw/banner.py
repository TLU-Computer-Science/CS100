import stddraw
import sys

# Accept string command-line argument s. Draw s, and move it across
# the screen, left-to-right, wrapping around when it reaches the border.

s = sys.argv[1]

# Remove the 5% border.
stddraw.setXscale(1.0/22.0, 21.0/22.0)
stddraw.setYscale(1.0/22.0, 21.0/22.0)

# Set the font.
stddraw.setFontFamily('Arial') 
stddraw.setFontSize(60)
stddraw.setPenColor(stddraw.BLACK)

i = 0.0
while True:
    stddraw.clear()
    stddraw.text((i % 1.0),       0.5, s)
    stddraw.text((i % 1.0) - 1.0, 0.5, s)
    stddraw.text((i % 1.0) + 1.0, 0.5, s)
    stddraw.show(60.0)
    i += 0.01
    