from math import exp
from numpy import shape


def get_model(A, c):
	def initial_condition(x):
		return exp(-(x - A)**2)
	
	def numerical_scheme(prev_t, prev_t_next_x, h_x, h_t):
		u = prev_t
		ux = (prev_t_next_x - u) / h_x
		return u - c * h_t * ux * u

	return initial_condition, None, numerical_scheme


burgers_A = 10
burgers_c = 1
burgers_model = get_model(burgers_A, burgers_c)
