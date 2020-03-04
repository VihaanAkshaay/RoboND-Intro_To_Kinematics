from sympy import symbols,cos,sin,pi,simplify
from sympy.matrices import Matrix
import numpy as np

#symols for joint variables that are commonly represented as q
q1,q2,q3,q4 = symbols(q1:5)  #slicing does not include the last element
A,R,O,C = symbols('A R O C') #unrelated symbols are defined this way

#conversion factors
rtd = 180./np.pi
dtr = np.pi/180.

#rotation matrices
R_x = Matrix([[1,0,0],
              [0,cos(q1),-sin(q1)],
              [0,sin(q1),cos(q1)]])
R_y = Matrix = ([[cos(q2),0,sin(q2)],
                 [0,1,0],
                 [-sin(q2),0,cos(q2)]])
R_z = Matrix([[cos(q3),-sin(q3),0],
              [sin(q3),cos(q3), 0],
              [ 0,0,1]])


