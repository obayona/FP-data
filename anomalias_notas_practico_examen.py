from datastatistic import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.patches import Patch
from matplotlib.lines import Line2D



examen = np.array([])
practico = np.array([])


semestres = ["2017_2T","2018_1T","2018_2T"]
for semestre in semestres:
	fileName = join("modificados",semestre + ".csv")
	data_dict, header = loadData(fileName)
	matriculas,examen_notas = getAttrs(data_dict,"2do_calif_final")
	matriculas,practico_notas = getAttrs(data_dict,"calif_final_practica")
	
	examen = np.concatenate([examen,examen_notas])
	practico = np.concatenate([practico,practico_notas])






#Practica < 40 y Examen > 70
cant1 = 0
for i,p in enumerate(practico):
	e = examen[i]
	if(p<=40 and e >= 70):
		cant1 +=1


#Practica > 70 y Examen < 40
cant2 = 0
for i,p in enumerate(practico):
	e = examen[i]
	if(p>=70 and e <= 40):
		cant2 +=1


fig,ax = plt.subplots(1)

ax.scatter(practico,examen)
plt.xlabel("Calif Final Practica")
plt.ylabel("2do examen")

rect = Rectangle((0,70),40,30,linewidth=2,edgecolor='g',facecolor='none')
ax.add_patch(rect)
rect = Rectangle((70,0),30,40,linewidth=2,edgecolor='r',facecolor='none')
ax.add_patch(rect)



#leyenda

leg1 = str(cant1)
leg2 = str(cant2)
ax.legend([leg1,leg2] ,loc='center right')
title =  "Tres semestres 2017_2T, 2018_1T, 2018_2T y %d estudiantes"%(len(examen))

plt.title(title)


plt.show()



