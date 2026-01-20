import cv2
import pytesseract

img = cv2.imread("formiga.png")
data = [[0] * 100 for _ in range(100)]
for j in range(100):
  for i in range(100):
    data[j][i] = int(img[j][i][0] == 255)

sx, sy = 36, 50
pos = sy * 1j + sx
fdir = 1j
for _ in range(10000):
  pos -= fdir
  sy, sx = int(pos.imag), int(pos.real)
  if data[sy][sx] == 1:
    data[sy][sx] = 0
    fdir *= 1j
  else:
    data[sy][sx] = 1
    fdir *= -1j

for j in range(100):
  for i in range(100):
    img[j][i] = ((255, 255, 255) if (data[j][i] > 0) else (0, 0, 0))

print(pytesseract.image_to_string(img).upper())
