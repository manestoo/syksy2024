import numpy as np
import math
import matplotlib.pyplot as plt


testidata = []
with open('hae_tiedot.csv', mode='r') as file:
    for line in file:
        testidata.append(line.strip('"'))
viimeisimmat_sensoriarvot = testidata[-320:]

testidata = np.zeros((320,3))

a = 0
for i in viimeisimmat_sensoriarvot:
    line = i.split(';')
    testidata[a][0] = line[5]
    testidata[a][1] = line[6]
    testidata[a][2] = line[7]
    a += 1


success = False
while not success:
    try:
        keskipiste = np.random.uniform(np.min(testidata),np.max(testidata),(6,3))
        ryhma = {i: [] for i in range(8)}    
        lista = []

        for opetus in range(50):

            for piste in range(len(testidata)):
                for i in range(6):
                    x_etaisyys = keskipiste[i][0] - testidata[piste][0]
                    y_etaisyys = keskipiste[i][1] - testidata[piste][1]
                    z_etaisyys = keskipiste[i][2] - testidata[piste][2]

                    etaisyys = math.sqrt(x_etaisyys**2 + y_etaisyys**2 + z_etaisyys**2)
                    lista.append(etaisyys)
                
                indexi = lista.index(min(lista))

                ryhma[indexi].append(testidata[piste])

                lista.clear()

            for i in range(6):
                x = 0
                y = 0
                z = 0
                for j in range(len(ryhma[i])):
                    x += ryhma[i][j][0]
                    y += ryhma[i][j][1]
                    z += ryhma[i][j][2]
                keskipiste[i][0] = x / len(ryhma[i])
                keskipiste[i][1] = y / len(ryhma[i])
                keskipiste[i][2] = z / len(ryhma[i])
        
        success = True

    except Exception as e:
        pass  #Jos randomilla alustetuissa keskipisteissä tulee piste, joka ei kerää itselle yhtäkään pistettä, alustetaan keskipisteet uudelleen



fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(testidata[:, 0], testidata[:, 1], testidata[:, 2], c='b', marker='o', label='Testidata')
ax.scatter(keskipiste[:, 0], keskipiste[:, 1], keskipiste[:, 2], c='r', marker='^', s=100, label='Keskipiste')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.legend()
plt.show()




with open('algorithm\keskipisteet.h', mode='w') as file:
    file.write("float keskipisteet[6][3];\n")
    for i in keskipiste:
        if (round(i[0]) == 18):
            file.write(f"keskipisteet[0] = {{{i[0]}, {i[1]}, {i[2]}}};\n")
        elif(round(i[0]) == 12):
            file.write(f"keskipisteet[1] = {{{i[0]}, {i[1]}, {i[2]}}};\n")
        elif (round(i[1]) == 18):
            file.write(f"keskipisteet[2] = {{{i[0]}, {i[1]}, {i[2]}}};\n")
        elif(round(i[1]) == 12):
            file.write(f"keskipisteet[3] = {{{i[0]}, {i[1]}, {i[2]}}};\n")
        elif (round(i[2]) == 18):
            file.write(f"keskipisteet[4] = {{{i[0]}, {i[1]}, {i[2]}}};\n")
        elif(round(i[2]) == 12):
            file.write(f"keskipisteet[5] = {{{i[0]}, {i[1]}, {i[2]}}};\n")

print(keskipiste)