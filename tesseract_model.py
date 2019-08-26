import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

# cube has 8 vertices or nodes -> (x,y,z)
vertices = ((1,-1,-1),(1,1,-1),(-1,1,-1),(-1,-1,-1),(1,-1,1),(1,1,1),(-1,-1,1),(-1,1,1))
vertices1 = ((2,-2,-2),(2,2,-2),(-2,2,-2),(-2,-2,-2),(2,-2,2),(2,2,2),(-2,-2,2),(-2,2,2))

spatial_sound = 'Interstellar.wav'

# each tuple correspond to a vertex, and the 'edge' that is going to be drawn
edges = ((0,1),(0,3),(0,4),(2,1),(2,3),(2,7),(6,3),(6,4),(6,7),(5,1),(5,4),(5,7))

# magic function to generate a cube
def cube(edges,vertices):
	# OpenGL opening
	glBegin(GL_LINES) # line-drawing code
	for edge in edges:
		for vertex in edge:
			glVertex3fv(vertices[vertex]) # OpenGL func to join vertex and draw lines
	glEnd()
	# OpenGL ending

# magic function to join the vertices of two cubes
def join_cubes(vertices,vertices1):
	for v1,v2 in zip(vertices,vertices1):
		glBegin(GL_LINES)
		glVertex3fv(v1)
		glVertex3fv(v2)
		glEnd()

def display_cube():
	pygame.init()
	pygame.mixer.music.load(spatial_sound)
	pygame.mixer.music.play(-1)
	display_window = (900,700)
	pygame.display.set_mode(display_window,DOUBLEBUF | OPENGL) # (display_window,opengl_referance)
	pygame.display.set_caption('Tesserect')

	gluPerspective(45,(display_window[0]/display_window[1]),0.1,50.0)
	# parameters -> (degree_value,aspect_ratio,znear,zfar) # near and far clippings
	# cliiping plane -> is at what distance does the object appear or disappear and the values should be positive

	glTranslatef(0.0,0.0,-11) # basically (x,y,z), -_ is to see the cube clearly
	#glEnable(GL_DEPTH_TEST)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		glRotatef(1,3,1,1) # (angle,x,y,z)
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

		cube(edges,vertices1) # large cube
		cube(edges,vertices) # small cube
		join_cubes(vertices,vertices1) # join edges of inner cube with the outer cube

		pygame.display.flip()
		pygame.time.wait(10)

display_cube()
