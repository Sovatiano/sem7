import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

results_dir = 'results'
if not os.path.exists(results_dir):
    os.makedirs(results_dir)

image = cv2.imread('image.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
inverted = 255 - gray

plt.figure(figsize=(15, 10))
plt.subplot(2, 3, 1)
plt.imshow(gray, cmap='gray')
plt.title('Полутоновое')
plt.axis('off')

plt.subplot(2, 3, 2)
plt.imshow(inverted, cmap='gray')
plt.title('Инвертированное')
plt.axis('off')

plt.subplot(2, 3, 4)
plt.hist(gray.ravel(), bins=256, range=[0, 256])
plt.title('Гистограмма полутонового')

plt.subplot(2, 3, 5)
plt.hist(inverted.ravel(), bins=256, range=[0, 256])
plt.title('Гистограмма инвертированного')

flipped = cv2.flip(gray, 1)
brightness = 50
brightened = cv2.add(flipped, brightness)
brightened = np.clip(brightened, 0, 255)

plt.subplot(2, 3, 3)
plt.imshow(brightened, cmap='gray')
plt.title('Яркое отраженное')
plt.axis('off')

plt.subplot(2, 3, 6)
plt.hist(brightened.ravel(), bins=256, range=[0, 256])
plt.title('Гистограмма яркого')

plt.tight_layout()
plt.savefig(os.path.join(results_dir, 'гистограммы_сравнение.jpg'))
plt.close()

hist, bins = np.histogram(brightened.flatten(), bins=256, range=[0, 256])
cdf = hist.cumsum()
cdf_normalized = cdf * float(hist.max()) / cdf.max()

plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(cdf_normalized, color='b')
plt.hist(brightened.flatten(), bins=256, range=[0, 256], color='r', alpha=0.5)
plt.title('Гистограмма и CDF')
plt.legend(('CDF', 'Гистограмма'))

cdf_m = np.ma.masked_equal(cdf, 0)
cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())
cdf = np.ma.filled(cdf_m, 0).astype('uint8')
equalized = cdf[brightened]

plt.subplot(1, 2, 2)
plt.hist(equalized.flatten(), bins=256, range=[0, 256])
plt.title('Гистограмма после CDF')

plt.tight_layout()
plt.savefig(os.path.join(results_dir, 'cdf_обработка.jpg'))
plt.close()

cv2.imencode('.jpg', gray)[1].tofile(os.path.join(results_dir, 'исходное_полутоновое.jpg'))
cv2.imencode('.jpg', inverted)[1].tofile(os.path.join(results_dir, 'инвертированное.jpg'))
cv2.imencode('.jpg', brightened)[1].tofile(os.path.join(results_dir, 'отраженное_яркое.jpg'))
cv2.imencode('.jpg', equalized)[1].tofile(os.path.join(results_dir, 'выравненное.jpg'))