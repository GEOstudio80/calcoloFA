#Iteratore per slip dell'array
#Chiamata da CallStrata.py per eseguire la media log dei valori di FA per tutti
# i limiti di integrazione richiesti. 
#versione 01/01/2018
import calcolo

def iterazione(Ar,alimit):
	i = 0
	for value in range(len(alimit)):
		a = i
		F = []
		while a < len(Ar):
			F.append(Ar[a])
			a = a + len(alimit)
		calcolo.calcolafa(F,alimit)
		print len(F)
		i = i + 1
		print 'Ciclo: %d di %d' %(i,len(alimit))
	


