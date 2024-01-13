from math import exp
from numpy import shape


def get_model(A, c):
	def initial_condition(x):
		return exp(-(x - A)**2)
	
	def exact_solution(x, t):
		return exp(-(x - c * t - A)**2)
	
	def numerical_scheme(prev_t, prev_t_next_x, h_x, h_t):
		u = prev_t
		ux = (prev_t_next_x - u) / h_x
		return u - c * h_t * ux

	return initial_condition, exact_solution, numerical_scheme


transport_A = 10
transport_c = 1
transport_model = get_model(transport_A, transport_c)
