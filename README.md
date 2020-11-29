# LoBonDetector
En primer lloc hem dividir l'estanteria en seccions, cadascuan de les quals representa un producte, obtenint les coordenades de cad aproducte en pixels. A continuació hem entrenat un model de Deep Learning anb "subimatges" de cada secció anterior, que hem etiquetat com a "Buit" o "No buit". En fer una petició d'una imatge es fa una crida a la API Vision de Google Clod que etiqueta objectes i la seva ubicació. A la matriu de l'estanteria marquem quines subimatges es troben bloquejades per un obstacle. Les que no estan bloquejades es passen al model de Deep Learning que ens retorna si es troben buides o no buides. Finalment retornem una matriu on cada posició por estar buida, no buida, o bloquejada. Això es el que representem en la nostra app de flask.

 #### Per fer us d'aquest programa cal seguir les pautes seguents:
     pip install -r requirements.txt
     flask run 
     
