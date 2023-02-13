#basic homogeneous transformations based off slide 46
# import the required modules
import math
import numpy as np

# homogeneous transformation for x
def trans_x(a):
	rot = np.array([[1, 0, 0, a],
					[0, 1, 0, 0],
					[0, 0, 1, 0],
					[0, 0, 0, 1]])
	return rot
	
				
# homogeneous transformation for y
def trans_y(b):
	rot = np.array([[1, 0, 0, 0],
					[0, 1, 0, b],
					[0, 0, 1, 0],
					[0, 0, 0, 1]])
	return rot
	
				
# homogeneous transformation for z
def trans_z(c):
	rot = np.array([[1, 0, 0, 0],
					[0, 1, 0, 0],
					[0, 0, 1, c],
					[0, 0, 0, 1]])
	return rot
	
				
# homogeneous rotation of x
def rot_x(alpha):
	rot = np.array([[1, 0, 0, 0],
					[0, math.cos(alpha), -math.sin(alpha), 0],
					[0, math.sin(alpha), math.cos(alpha), 0],
					[0, 0, 0, 1]])
	return rot
	
				
# homogeneous rotation for y
def rot_y(beta):
	rot = np.array([[math.cos(beta), 0, math.sin(beta), 0],
					[0, 1, 0, 0],
					[-math.sin(beta), 0, math.cos(beta), 0],
					[0, 0, 0, 1]])
	return rot
	
				
# homogeneous rotation for z
def rot_z(gamma):
	rot = np.array([[math.cos(gamma), -math.sin(gamma), 0, 0],
					[math.sin(gamma), math.cos(gamma), 0, 0],
					[0, 0, 1, 0],
					[0, 0, 0, 1]])
	return rot
	
	
	
def vec(x,y,z,t):
#	Define a vector as an numpy and transpose it to a column vector.
	vec = np.array([[x, y, z, t]]).T 
	return vec
