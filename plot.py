import data as dt
import matplotlib.pyplot as plt


# test
x = dt.pega_arquivo()

print("rodando...")


plt.title("Trajetoria da bola")
plt.scatter(x[1][0], x[2][0], s=1.5, label="bola")
plt.xlabel(" posicao X(m)")
plt.ylabel(" posicao Y(m)")

plt.grid()
plt.legend()
plt.show()
