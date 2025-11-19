import cv2
import numpy as np
import os
from matplotlib import pyplot as plt

results_dir = 'results'
os.makedirs(results_dir, exist_ok=True)

image = cv2.imread('image.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imencode('.jpg', gray)[1].tofile(os.path.join(results_dir, 'исходное.jpg'))

noise = np.random.normal(0, 25, gray.shape)
noisy_image_float = np.clip(gray.astype(np.float64) + noise, 0, 255)
noisy_image = noisy_image_float.astype(np.uint8)

cv2.imencode('.jpg', noisy_image)[1].tofile(os.path.join(results_dir, 'шумное.jpg'))

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.hist(gray.ravel(), 256, [0, 256], color='blue', alpha=0.7)
plt.title('Гистограмма исходного изображения')
plt.xlabel('Значение пикселя')
plt.ylabel('Частота')
plt.grid(True, alpha=0.3)

plt.subplot(1, 2, 2)
plt.hist(noisy_image.ravel(), 256, [0, 256], color='red', alpha=0.7)
plt.title('Гистограмма изображения с шумом')
plt.xlabel('Значение пикселя')
plt.ylabel('Частота')
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(os.path.join(results_dir, 'гистограммы.png'), dpi=300, bbox_inches='tight')
plt.close()

blur1 = cv2.GaussianBlur(gray, (15, 15), 3)
blur2 = cv2.GaussianBlur(gray, (15, 15), 6)
blur3 = cv2.GaussianBlur(gray, (15, 15), 9)

cv2.imencode('.jpg', blur1)[1].tofile(os.path.join(results_dir, 'размытие1.jpg'))
cv2.imencode('.jpg', blur2)[1].tofile(os.path.join(results_dir, 'размытие2.jpg'))
cv2.imencode('.jpg', blur3)[1].tofile(os.path.join(results_dir, 'размытие3.jpg'))

def draw_isolines(img, filename):
    edges = cv2.Canny(img, 50, 150)
    isolines = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    cv2.imencode('.jpg', isolines)[1].tofile(os.path.join(results_dir, filename))

draw_isolines(gray, 'исходное_изолинии.jpg')
draw_isolines(blur1, 'размытие1_изолинии.jpg')
draw_isolines(blur2, 'размытие2_изолинии.jpg')
draw_isolines(blur3, 'размытие3_изолинии.jpg')