import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import os

os.makedirs('results/', exist_ok=True)


def process_image(image_path, title):
    img = cv.imread(image_path)
    img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    equalized = cv.equalizeHist(gray)

    plt.figure(figsize=(15, 10))

    plt.subplot(2, 3, 1)
    plt.imshow(img_rgb)
    plt.title(f'{title} - Исходное')
    plt.axis('off')

    plt.subplot(2, 3, 2)
    plt.imshow(gray, cmap='gray')
    plt.title(f'{title} - Ч/Б')
    plt.axis('off')

    plt.subplot(2, 3, 3)
    plt.hist(gray.ravel(), 256, range=[0, 256])
    plt.title('Гистограмма ч/б')

    plt.subplot(2, 3, 4)
    plt.imshow(equalized, cmap='gray')
    plt.title(f'{title} - Эквализированное')
    plt.axis('off')

    plt.subplot(2, 3, 5)
    plt.hist(equalized.ravel(), 256, range=[0, 256])
    plt.title('Гистограмма эквализированная')

    plt.subplot(2, 3, 6)
    hist_orig, _ = np.histogram(gray, bins=256, range=(0, 255))
    cdf_orig = hist_orig.cumsum()
    cdf_orig = cdf_orig / cdf_orig[-1]

    hist_eq, _ = np.histogram(equalized, bins=256, range=(0, 255))
    cdf_eq = hist_eq.cumsum()
    cdf_eq = cdf_eq / cdf_eq[-1]

    plt.plot(cdf_orig, label='Исходная')
    plt.plot(cdf_eq, label='Эквализированная')
    plt.title('Эмпирическая функция распределения')
    plt.legend()

    plt.tight_layout()
    plt.savefig(f'results/{title}.png')
    plt.show()

    return gray, equalized

process_image('underexp.jpg', 'Недоэкспонированное')
process_image('normal.jpg', 'Нормальное')
process_image('overexp.jpg', 'Переэкспонированное')