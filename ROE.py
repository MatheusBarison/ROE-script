import math as mt
import matplotlib.pyplot as plt

#Variáveis
f0 = 300
z0 = 100 + 0j
z1 = 141.4
z2 = 282.8
zc = 400
y = []
x = []

i0 = 0

# Calcula ROE variando a freq de 200MHz a 400MHz, de 1MHz em 1MHz
for fc in range(200, 401, 1):   

    lqwt = (1/4)*(fc/f0)

    # QWT_2
    complexo_a = complex(0,(z2*mt.tan(2*mt.pi*lqwt)))
    complexo_b = complex(0,(zc*mt.tan(2*mt.pi*lqwt)))

    z_f_1 = z2*((zc + complexo_a)/(z2 + complexo_b))

    # QWT_1
    complexo_a = complex(0,(z1*mt.tan(2*mt.pi*lqwt)))
    complexo_b = complex(0,(z_f_1*mt.tan(2*mt.pi*lqwt)))

    z_f_2 = z1*((z_f_1 + complexo_a)/(z1 + complexo_b))

    coef = (z_f_2 - z0)/(z_f_2 + z0)
    roe = (1 + abs(coef))/(1 - abs(coef))

    y.append(roe)
    x.append(fc)

    # Marca no gráfico ponto inicial e final para ROE <= 1,2
    if roe <= 1.2 :
        if i0 == 0:
            inicio = fc
            i0 = 1
        else:
            fim = fc

plt.plot(x, y)
plt.xlabel('frequência [MHz]')
plt.ylabel('ROE')
plt.grid()
plt.axhline(y = 1.2, color = 'r', linestyle = '--')
plt.axvline(x = inicio, color='green', linestyle = '--')
plt.axvline(x = fim, color='green', linestyle = '--')
plt.show()
