from math import exp
from numpy import shape


def get_model(A, c):
	def initial_condition(x):
		return exp(-(x - A)**2)
	
	def exact_solution(x, t):
		return exp(-(x - c * t - A)**2)
	
	def numerical_scheme(partial_solution, i, j, h_x, h_t):
		nx, nt = shape(partial_solution)
		if i == nx - 1 or i == 0:
			return 0

		ux = (partial_solution[i + 1, j - 1] - partial_solution[i, j - 1]) / h_x
		return partial_solution[i, j - 1] - c * h_t * ux

	return initial_condition, exact_solution, numerical_scheme


transport_A = 10
transport_c = 1
transport_model = get_model(transport_A, transport_c)
