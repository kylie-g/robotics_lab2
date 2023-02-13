# import the rigid body motion module, math, and numpy
import p2_sol
import math
import numpy as np

# transformation H_1 - current frame
def H_1():
	# translation of 2.5 units along the current x-axis
	Tx = p2_sol.trans_x(2.5)
	# translation of 0.5 units along the current z-axis
	Tz = p2_sol.trans_z(0.5)
	# translation of -1.5 units along the current y-axis
	Ty = p2_sol.trans_y(-1.5)
	
	# define a 3D vector
	v0 = p2_sol.vec(0,1,1,1) # values from the example in class

	T = np.matmul(Tx, Tz)
	T = np.matmul(T, Ty)
	
	print('The 4x4 matrix for H_1 (current frame) is:\n', T)
	
# transformation H_2 - current frame
def H_2():
	
	# translation of 0.5 units along the current z-axis
	Tz = p2_sol.trans_z(0.5)
	# translation of 2.5 units along the current x-axis
	Tx = p2_sol.trans_x(2.5)
	# translation of -1.5 units along the current y-axis
	Ty = p2_sol.trans_y(-1.5)
	
	# define a 3D vector
	v0 = p2_sol.vec(0,1,1,1) # values from the example in class

	T = np.matmul(Tz, Tx)
	T = np.matmul(T, Ty)
	
	print('The 4x4 matrix for H_2 (current frame) is:\n', T)
	
# transformation H_3 - fixed frame
def H_3():
	# translation of 2.5 units along the current x-axis
	Tx = p2_sol.trans_x(2.5)
	# translation of 0.5 units along the current z-axis
	Tz = p2_sol.trans_z(0.5)
	# translation of -1.5 units along the current y-axis
	Ty = p2_sol.trans_y(-1.5)
	
	# define a 3D vector
	v0 = p2_sol.vec(0,1,1,1) # values from the example in class

	T = np.matmul(Ty, Tz)
	T = np.matmul(T, Tx)
	
	print('The 4x4 matrix for H_3 (fixed frame) is:\n', T)


# transformation H_4 - fixed frame
def H_4():
	# translation of 0.5 units along the current z-axis
	Tz = p2_sol.trans_z(0.5)
	# translation of 2.5 units along the current x-axis
	Tx = p2_sol.trans_x(2.5)
	# translation of -1.5 units along the current y-axis
	Ty = p2_sol.trans_y(-1.5)
	
	# define vector
	v0 = p2_sol.vec(0,1,1,1) # values from the example in class

	T = np.matmul(Ty, Tx)
	T = np.matmul(T, Tz)
	
	print('The 4x4 matrix for H_4 (fixed frame) is:\n', T)
	

def H_5():
	Rx = p2_sol.rot_x(math.pi/2)
	Tx = p2_sol.trans_x(3)
	Tz = p2_sol.trans_z(-3)
	Rz = p2_sol.rot_z(-math.pi/2)
	
	# define vector
	v0 = p2_sol.vec(0,1,1,1) # values from the example in class
	TR = np.matmul(Rx, Tx)
	TR = np.matmul(TR, Tz)
	TR = np.matmul(TR, Rz)
	
	print('The 4x4 matrix for H_5 is:\n', TR)
	
	
if __name__ == '__main__':
	# update the output format
	np.set_printoptions(precision = 2, suppress = True)
	H_1()
	H_2()
	H_3()
	H_4()
	H_5()
