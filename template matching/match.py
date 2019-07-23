import numpy as np
import argparse
import imutils
import glob
import cv2

# construir el analizador de argumentos y analizar los argumentos
ap = argparse.ArgumentParser()
ap.add_argument("-t", "--template", required=True, help="Ruta a la imagen de la plantilla")
ap.add_argument("-i", "--imagenes", required=True,
	help="Ruta a las imágenes donde la plantilla será emparejada")
ap.add_argument("-v", "--visualizar",
	help="Flag que indica si visualizar o no cada iteración.")
args = vars(ap.parse_args())

# cargue la imagen, conviértala a escala de grises y detecte bordes
template = cv2.imread(args["template"])
template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
template = cv2.Canny(template, 50, 200)
(tH, tW) = template.shape[:2]
cv2.imshow("Template", template)

# recorre las imágenes para encontrar la plantilla en
for imagePath in glob.glob(args["imagenes"] + "/*.jpg"):
	# cargue la imagen, conviértala a escala de grises e inicialice la variable de contabilidad para hacer un seguimiento de la región coincidente
	image = cv2.imread(imagePath)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	found = None

	# bucle sobre las escalas de la imagen
	for scale in np.linspace(0.2, 1.0, 20)[::-1]:
		# cambiar el tamaño de la imagen según la escala y realizar un seguimiento de la proporción de cambio de tamaño
		resized = imutils.resize(gray, width = int(gray.shape[1] * scale))
		r = gray.shape[1] / float(resized.shape[1])

		# si la imagen redimensionada es más pequeña que la plantilla, entonces salte del bucle
		if resized.shape[0] < tH or resized.shape[1] < tW:
			break

		# detecte bordes en la imagen redimensionada, en escala de grises y aplique la coincidencia de plantillas para encontrar la plantilla en la imagen
		edged = cv2.Canny(resized, 50, 200)
		result = cv2.matchTemplate(edged, template, cv2.TM_CCOEFF)
		(_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)

		# Compruebe si la iteración debe ser visualizada
		if args.get("visualize", False):
			# dibujar un cuadro delimitador alrededor de la región detectada
			clone = np.dstack([edged, edged, edged])
			cv2.rectangle(clone, (maxLoc[0], maxLoc[1]),
				(maxLoc[0] + tW, maxLoc[1] + tH), (0, 0, 255), 2)
			cv2.imshow("Visualize", clone)
			cv2.waitKey(0)

		# Si hemos encontrado un nuevo valor máximo de correlación, entonces actualice la variable de contabilidad
		if found is None or maxVal > found[0]:
			found = (maxVal, maxLoc, r)

	# descomprima la variable contable y calcule las coordenadas (x, y) del cuadro delimitador en función de la relación de cambio de tamaño
	(_, maxLoc, r) = found
	(startX, startY) = (int(maxLoc[0] * r), int(maxLoc[1] * r))
	(endX, endY) = (int((maxLoc[0] + tW) * r), int((maxLoc[1] + tH) * r))

	# dibuje un cuadro delimitador alrededor del resultado detectado y muestre la imagen
	cv2.rectangle(image, (startX, startY), (endX, endY), (0, 0, 255), 2)
	cv2.imshow("Imagen", image)
	cv2.waitKey(0)