#Modulo per calcolo FA chiamato da CallStrata.py
#Calcola il rapporto FA tra due spettri per tutti i limiti di integrazione richiesti
#versione 01/01/2018

def calcolostrata(Fhi,zin,zout,alimit,blimit,naccel):
	iteratore = 1
	while iteratore < naccel:
		print '***', 'Inizio calcolo accelerogramma: ',iteratore,'***'
		for limiti, value in enumerate(alimit):
			limiteinf = alimit[limiti]
			limitesup = blimit[limiti]
			i = []
			for index, value in enumerate(zin[0]):
				if float(value) > limiteinf and float(value) < limitesup:
					i.append(index)
					ax = min(i)
					bx = max(i)
			AreaIn = 0
			AreaOut = 0
			while ax != bx:
				dxg = float(zin[0][ax])
				dxp = float(zin[0][ax+1])
				dyg = float(zin[iteratore][ax])
				dyp = float(zin[iteratore][ax+1])
				dy2g = float(zout[iteratore][ax])
				dy2p = float(zout[iteratore][ax+1])
				dx = dxp - dxg
				dy = dyp - dyg
				dy2 = dy2p - dy2g
				if dy == 0:
					Areai = dx*(zin[iteratore][ax])
					Areai2 = dx*(zout[iteratore][ax])
				else:
					Areai = dx*(float(zin[iteratore][ax]))+((dx*dy)/2)
					Areai2 = dx*(float(zout[iteratore][ax]))+((dx*dy2)/2)
				ax = ax + 1	
				#print float(zin[iteratore][ax+1])
				AreaIn = AreaIn + Areai
				AreaOut = AreaOut + Areai2
			fh = (round(float(AreaOut/AreaIn),4))
			Fhi.append(fh)
			print 'Intervallo',alimit[limiti],'-',blimit[limiti],':',fh

			del ax,bx
		print '***', 'Fine calcolo accelerogramma: ',iteratore,'-- Site in strata: ', int(iteratore-1),'***'
		iteratore = iteratore + 1
	#return Fhi

	




