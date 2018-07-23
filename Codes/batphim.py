import pygame
import stddraw
pygame.init()
x = 0
y = 0
stddraw.setPenColor(stddraw.RED)
while True:
	keys=pygame.key.get_pressed()
	if keys[pygame.K_LEFT]:
		x -= 0.01
	if keys[pygame.K_RIGHT]:
		x += 0.01
	if keys[pygame.K_UP]:
		y += 0.01
	if keys[pygame.K_DOWN]:
		y -= 0.01
	stddraw.filledCircle(x,y,0.05)
	stddraw.show(20)
	stddraw.clear()