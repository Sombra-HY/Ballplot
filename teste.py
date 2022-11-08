import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


# O np cria uma lista com intervalo de dominio
# tendo a sintaxe (inicio(incluido), fim(incluido), Qpontos)
# exemplo, [1,3] --> (1>x<3) xE(conjunto)
#
# basicamente ele cria um conjuto com o intervalo passado a este...
#
#t = np.linspace(-10, 10, 200)
#y = 2t +3


# t = np.linspace()
#  x = ((0.021 * (t**2)) - (0.34 * t) + 2.5)



# F(t) = 2t +3

#fig, ax = plt.subplots(figsize=(6, 4), tight_layout=True)
#plt.plot(x, y)
#plt.plot([1,2], [2,2])

#plt.grid()
#plt.show()

"""Vbx = ((0.021 * (t**2)) - (0.34 * t) + 2.5)  #velocidade da bola no eixo x no intante t
Vby = ((-0.4 * t) + 1.8)  #velocidade da bola no eixo y no intante t"""


"""
fig = plt.figure(tight_layout=True)
gs = gridspec.GridSpec(2, 2)

ax = fig.add_subplot(gs[0, :])
ax.plot(np.arange(0, 1e6, 1000))
ax.set_ylabel('YLabel0')
ax.set_xlabel('XLabel0')

for i in range(2):
    ax = fig.add_subplot(gs[1, i])
    ax.plot(np.arange(1., 0., -0.1) * 2000., np.arange(1., 0., -0.1))
    ax.set_ylabel('YLabel1 %d' % i)
    ax.set_xlabel('XLabel1 %d' % i)
    if i == 0:
        ax.tick_params(axis='x', rotation=55)
fig.align_labels()  # same as fig.align_xlabels(); fig.align_ylabels()
"
plt.show()""