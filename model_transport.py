import math


def get_model(A, c):
	def initial_condition(x):
		return math.exp(-(x - A)**2)
	
	def exact_solution(x, t):
		return math.exp(-(x - c * t - A)**2)

	return initial_condition, exact_solution


transport_A = 10
transport_c = 1
transport_model = get_model(transport_A, transport_c)
