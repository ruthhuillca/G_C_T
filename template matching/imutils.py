import numpy as np
import cv2

def translate(image, x, y):
	# Definir la matriz de traducción y realizar la traducción.
	M = np.float32([[1, 0, x], [0, 1, y]])
	shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

	# Devolver la imagen traducida.
	return shifted

def rotate(image, angle, center = None, scale = 1.0):
	# Agarra las dimensiones de la imagen.
	(h, w) = image.shape[:2]

	# Si el centro es None, inicialícelo como el centro de la imagen.
	if center is None:
		center = (w / 2, h / 2)

	# Realizar la rotacion
	M = cv2.getRotationMatrix2D(center, angle, scale)
	rotated = cv2.warpAffine(image, M, (w, h))

	# Devolver la imagen girada.
	return rotated

def resize(image, width = None, height = None, inter = cv2.INTER_AREA):
	# Inicialice las dimensiones de la imagen a cambiar de tamaño y tome el tamaño de la imagen.
	dim = None
	(h, w) = image.shape[:2]

	# Si tanto el ancho como el alto son None, devuelva la imagen original.
	if width is None and height is None:
		return image

	# Compruebe si el ancho es None
	if width is None:
		# Calcula la relación de la altura y construye las dimensiones.
		r = height / float(h)
		dim = (int(w * r), height)

	# de lo contrario, la altura es None.
	else:
		# Calcula la relación del ancho y construye las dimensiones.
		r = width / float(w)
		dim = (width, int(h * r))

	# cambiar el tamaño de la imagen
	resized = cv2.resize(image, dim, interpolation = inter)

	# devuelve la imagen redimensionada
	return resized