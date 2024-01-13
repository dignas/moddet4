from math import exp
from numpy import shape


def get_model(A, c):
	def initial_condition(x):
		return exp(-(x - A)**2)
	
	def numerical_scheme(partial_solution, i, j, h_x, h_t):
		nx, nt = shape(partial_solution)
		if i == nx - 1 or i == 0:
			return 0

		ux = (partial_solution[i + 1, j - 1] - partial_solution[i, j - 1]) / h_x
		return partial_solution[i, j - 1] - c * h_t * ux * partial_solution[i, j - 1]

	return initial_condition, numerical_scheme


burgers_A = 10
burgers_c = 1
burgers_model = get_model(burgers_A, burgers_c)
