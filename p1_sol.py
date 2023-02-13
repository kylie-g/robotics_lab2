# import the rigid body motion module, math, and numpy
import rbm
import math
import numpy as np


if __name__ == '__main__':
	# define a test values psi, theta, and phi for x, y, and z 
	psi = math.pi/2
	theta = math.pi/2
	phi = math.pi/2
	
	# update the output format
	np.set_printoptions(precision = 2, suppress = True)
	
	# define a 3D vector
	v0 = rbm.vec(0,1,1) # values from the example in class
	
	# define rotation around the x axis
	Rx = rbm.rot_x(theta)
	# define a 3D rotation about y axis
	Ry = rbm.rot_y(theta)
	# define rotation around the z axis
	Rz = rbm.rot_z(theta)
	
	# calculate a total rotation via CURRENT FRAMES - first with rx and ry, then include rz with the first matmul (R) - in order of rotations rx -> ry -> rz
	R = np.matmul(Rx, Ry)
	R = np.matmul(R, Rz)
	
	# calculate the results of rotation
	v01 = R.dot(v0)
	print('The transformed vector is:\n',v01)
