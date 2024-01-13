from model_transport import transport_model, transport_A, transport_c
from model_burgers import burgers_model, burgers_A, burgers_c

import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib import cm


def run_13_14_15(model, A, c, plot_ts, plot_inds, plot_no, plot_names, run_15=False):
	init_cond, _, num_schem = model
	nhs = 20
	hxs = np.linspace(0.03, 0.3, nhs)
	maes = np.zeros(nhs)

	for h_ind in range(nhs):
		h_x = hxs[h_ind]
		t_range = 5
		plot_margin = 3
		x_min = A - plot_margin
		x_max = A + c * t_range + plot_margin
		h_t = h_x / 10
		nx = math.ceil((x_max - x_min) / h_x)
		nt = math.ceil(t_range / h_t)
		xs = np.linspace(x_min, x_max, nx)
		xs2 = np.linspace(x_min, x_max, nx * 2)
		ts = np.linspace(0, 5, nt)

		result = np.zeros((nx, nt))
		result2 = np.zeros((nx * 2, nt * 2))

		for i in range(1, nx - 1):
			result[i, 0] = init_cond(xs[i])

		for i in range(1, nx * 2 - 1):
			result2[i, 0] = init_cond(xs2[i])

		for j in range(1, nt):
			for i in range(1, nx - 1):
				result[i, j] = num_schem(result[i, j - 1], result[i + 1, j - 1], h_x, h_t)

		for j in range(1, nt * 2):
			for i in range(1, nx * 2 - 1):
				result2[i, j] = num_schem(result2[i, j - 1], result2[i + 1, j - 1], h_x / 2, h_t / 2)

		if h_ind == 0:
			_, ax = plt.subplots(plot_no, 1)
			for i in range(len(plot_ts)):
				t = plot_ts[i]
				ax_ind = plot_inds[i]
				t_desc = round(t_range * t / nt, 3)
				ax[ax_ind].plot(xs, result[:, t], label=f"t = {t_desc}")
				ax[ax_ind].legend()
			plt.savefig(f"plots/{plot_names[1]}.png")

			if run_15:
				plt.clf()
				tmax = 200
				X, T = np.meshgrid(ts[:tmax], xs)
				_, ax = plt.subplots(subplot_kw={"projection": "3d"})
				ax.plot_surface(X, T, result[:,:tmax], vmin=result.min() * 2, cmap=cm.Blues)
				plt.show()

		mask = np.logical_and(np.isfinite(result2[::2, ::2]), np.isfinite(result))
		maes[h_ind] = np.mean(np.abs(result2[::2, ::2][mask] - result[mask]))

	plt.clf()
	_, ax = plt.subplots(1)
	ax.plot(hxs, np.log(maes))
	ax.set_title("Mean absolute error between h and h/2")
	ax.set_xlabel("h")
	ax.set_ylabel("MAE [log]")
	plt.savefig(f"plots/{plot_names[0]}.png")


run_13_14_15(transport_model, transport_A, transport_c, [0, 100, 150, 175, 200, 500], [0, 0, 0, 0, 1, 2], 3, ["transport_13", "transport_14"], run_15=True)
run_13_14_15(burgers_model, burgers_A, burgers_c, [0, 100, 150, 175, 200, 225, 235], [0, 0, 0, 0, 0, 1, 2], 3, ["burgers_13", "burgers_14"])


