import cv2
import pytesseract

img = cv2.imread("formiga.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

startx, starty = 36, 50
pos = starty * 1j + startx
direction = 1j
for _ in range(10000):
  pos -= direction
  y, x = int(pos.imag), int(pos.real)
  if img[y][x] > 127:
    img[y][x] = 0
    direction *= 1j
  else:
    img[y][x] = 255
    direction *= -1j

print(pytesseract.image_to_string(img).upper())
