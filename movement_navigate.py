import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

vertices = ((1,-1,-1),(1,1,-1),(-1,1,-1),(-1,-1,-1),(1,-1,1),(1,1,1),(-1,-1,1),(-1,1,1))
edges = ((0,1),(0,3),(0,4),(2,1),(2,3),(2,7),(6,3),(6,4),(6,7),(5,1),(5,4),(5,7))

colors = ((1,0,0),(0,1,0),(0,0,1),(0,1,0),(1,1,1),(0,1,1),(1,0,0),(0,1,0),(0,0,1),(1,0,0),(1,1,1),(0,1,1))

surfaces = ((0,1,2,3),(3,2,7,6),(6,7,5,4),(4,5,1,0),(1,5,7,2),(4,0,3,6))

def cube():
	glBegin(GL_QUADS)
	for surface in surfaces:
		x = 1
		for vertex in surface:
			x += 1
			glColor3fv(colors[x])
			glVertex3fv(vertices[vertex])
	glEnd()

	glBegin(GL_LINES)
	for edge in edges:
		for vertex in edge:
			glVertex3fv(vertices[vertex])
	glEnd()

def display_cube():
	pygame.init()
	display_window = (800,600)
	pygame.display.set_mode(display_window,DOUBLEBUF | OPENGL)

	gluPerspective(45,(display_window[0]/display_window[1]),0.1,50.0)
	glTranslatef(0.0,0.0,-10)
	glRotatef(25,2,1,0)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

			# key events
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					#(x,y,z)
					glTranslatef(-.5,0,0) # shift left side
				if event.key == pygame.K_RIGHT:
					glTranslatef(.5,0,0) # shift right side
				if event.key == pygame.K_UP:
					glTranslatef(0,1,0) # shift upwards
				if event.key == pygame.K_DOWN:
					glTranslatef(0,-1,0) # shift downwards

			# mouse events
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 4:
					glTranslatef(0,0,1) # forward
				if event.button == 5:
					glTranslatef(0,0,-1) # backward

		glRotatef(1,2,1,0)
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

		cube()

		pygame.display.flip()
		pygame.time.wait(10)

display_cube()