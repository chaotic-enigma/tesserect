import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

# cube has 8 vertices or nodes -> (x,y,z)
vertices = ((1,-1,-1),(1,1,-1),(-1,1,-1),(-1,-1,-1),(1,-1,1),(1,1,1),(-1,-1,1),(-1,1,1))

# each tuple correspond to a vertex, and the 'edge' that is going to be drawn
edges = ((0,1),(0,3),(0,4),(2,1),(2,3),(2,7),(6,3),(6,4),(6,7),(5,1),(5,4),(5,7))

# magic function to generate a cube
def cube():
	# OpenGL opening
	glBegin(GL_LINES) # line-drawing code
	for edge in edges:
		for vertex in edge:
			glVertex3fv(vertices[vertex]) # OpenGL func to join vertex and draw lines
	glEnd()
	# OpenGL ending

def display_cube():
	pygame.init()
	display_window = (800,600)
	pygame.display.set_mode(display_window,DOUBLEBUF | OPENGL)

	gluPerspective(45,(display_window[0]/display_window[1]),0.1,50.0)
	# parameters -> (degree_value,aspect_ratio,znear,zfar) # near and far clippings
	# cliiping plane -> is at what distance does the object appear or disappear and the values should be positive

	glTranslatef(0.0,0.0,-7) # basically (x,y,z), -_ is to see the cube clearly, moving about the object

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		glRotatef(3,2,0,0) # (angle,x,y,z)
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # clearing the frame with two constants (constant | constant)
		cube()

		pygame.display.flip()
		pygame.time.wait(10) # 10ms

display_cube()
