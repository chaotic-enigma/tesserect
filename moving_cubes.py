import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

import random

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
	glTranslatef(random.randrange(-5,5),random.randrange(-5,5),-30)
	glRotatef(25,2,1,0)

	object_passed = False

	while not object_passed:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					glTranslatef(-.5,0,0)
				if event.key == pygame.K_RIGHT:
					glTranslatef(.5,0,0)
				if event.key == pygame.K_UP:
					glTranslatef(0,1,0)
				if event.key == pygame.K_DOWN:
					glTranslatef(0,-1,0)

		x = glGetDoublev(GL_MODELVIEW_MATRIX)
		#print(x)

		camera_x = x[3][0]
		camera_y = x[3][1]
		camera_z = x[3][2]

		glTranslatef(0,0,.5)

		glRotatef(1,2,1,0)
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

		cube()

		pygame.display.flip()

		if camera_z <= 0:
			object_passed = True

for x in range(10):
	glLoadIdentity()
	display_cube()