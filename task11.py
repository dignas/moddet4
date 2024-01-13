from model_transport import transport_model, transport_A, transport_c

import numpy as np
import matplotlib.pyplot as plt


if __name__ == "__main__":
	init_cond, exact = transport_model
	t_range = 5
	resolution = 1000
	plot_margin = 3

	xs = np.linspace(transport_A - plot_margin, transport_A + transport_c * t_range + plot_margin, resolution)
	ts = np.arange(5)

	for t in ts:
		ys = [exact(x, t) for x in xs]
		plt.plot(xs, ys, label=f"t = {t}")

	plt.legend()
	plt.savefig("plots/task1.png")
