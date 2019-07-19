import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle
from os.path import join

def str2float(string):
	try:
		return float(string.replace(",","."))
	except:
		return np.nan

def str2int(string):
	try:
		return int(string)
	except:
		return 1

def loadData(fileName):
	f = open(fileName)
	estudiantes_dict = {}
	header = f.readline().strip()
	flag = False
	if "Unnamed" in header:
		flag = True
	
	header = header.split(";")
	if(flag):
		header = header[1:]


	for line in f:
		columns = line.strip().split(";")
		if flag:
			columns = columns[1:]
		estudiante_dict = {}
		for i in range(1,7):
			estudiante_dict[header[i]]=columns[i]
		
		if "veces_tomadas" in estudiante_dict:
			estudiante_dict["veces_tomadas"]=str2int(estudiante_dict["veces_tomadas"])
		
		for i in range(7,len(header)-1):
			estudiante_dict[header[i]]=str2float(columns[i])
		estudiantes_dict[estudiante_dict["matricula"]]=estudiante_dict

		estudiante_dict["AP"]=columns[-1]

	f.close()
	return estudiantes_dict,header

def getAttrs(estudiantes_dict,attr):
	matriculas = []
	values = []
	keys = list(estudiantes_dict.keys())
	keys.sort()
	for matricula in keys:
		estudiante_dict = estudiantes_dict[matricula]
		matriculas.append(matricula)
		values.append(estudiante_dict[attr])
	return np.array(matriculas),np.array(values)


def createHist(titulo,notas):
	plt.figure(titulo)
	plt.title(titulo)
	bins = [0,1,2,3,4,5,6,7,8,9,10]
	N, bins, patches = plt.hist(notas,bins=10,normed=False)

	rp_color = "#FF0000"
	ap_color = "#95D049"

	for j in range(0,6):
		patches[j].set_facecolor(rp_color)
	for j in range(6,10):
		patches[j].set_facecolor(ap_color)


	handles = [Rectangle((0,0),1,1,color=c,edgecolor="k") for c in [ap_color,rp_color]]
	labels= ["AP","RP"]
	plt.legend(handles, labels)
	axes = plt.gca()
	axes.set_ylim([0,400])
	axes.set_ylabel('Frecuencia')
	axes.set_xlabel('Calificaciones')




if __name__== "__main__": 
	semestres = ["2017-1T","2017_2T","2018_1T","2018_2T"]
	for semestre in semestres:
		fileName = join("modificados",semestre + ".csv")
		data_dict, header = loadData(fileName)
		matriculas,final_notes = getAttrs(data_dict,"final")
		final_notes = final_notes[np.logical_not(np.isnan(final_notes))]
		#final_notes = final_notes[np.logical_and(final_notes>=0, final_notes<=100)]

		matriculas,ap = getAttrs(data_dict,"AP")
		print((ap=="True").sum(), ap.size)
		ap_percent = float((ap=="True").sum())/float(ap.size)

		print("Semestre ",semestre)
		print("Promedio: ", final_notes.mean())
		print("AP %", ap_percent*100)
		print("_"*20)
		createHist(semestre,final_notes)

	plt.show()


