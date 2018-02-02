#Modulo per il calcolo della media logaritmica
#Modulo chiamato da It per visualizzazione media log complessiva per ogni intervallo
#di calcolo di FA
#versione 01/01/2018
import math
def calcolafa(F,alimit):
	appoggio = []
	for val in F:
		appoggio.append(math.log(val))
	counter = 0
	for valappoggio in appoggio:
		counter = counter + valappoggio
	print 'Risultato'
	print math.exp(counter/len(F)) #formula [13]
	print 'Fine chiamata'