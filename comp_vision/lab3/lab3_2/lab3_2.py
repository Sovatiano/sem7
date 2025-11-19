import cv2
import os

image_path = 'image.jpg'
results_dir = 'results'

if not os.path.exists(results_dir):
    os.makedirs(results_dir)

image = cv2.imread(image_path)

print(f"Размер изображения: {image.shape}")
print(f"Высота: {image.shape[0]} пикселей")
print(f"Ширина: {image.shape[1]} пикселей")
print(f"Количество каналов: {image.shape[2]}")
print(f"Тип данных: {image.dtype}")

thumbnail_size = (300, 200)
color_thumbnail = cv2.resize(image, thumbnail_size)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
bw_thumbnail = cv2.resize(gray_image, thumbnail_size)

cv2.imencode('.jpg', color_thumbnail)[1].tofile(os.path.join(results_dir, 'цветная_миниатюра.jpg'))
cv2.imencode('.jpg', bw_thumbnail)[1].tofile(os.path.join(results_dir, 'чб_миниатюра.jpg'))

h, w = image.shape[:2]
square_size = min(h, w) // 4
start_x = w // 2 - square_size // 2
start_y = h // 2 - square_size // 2

square_region = image[start_y:start_y+square_size, start_x:start_x+square_size]

rotated_180 = cv2.rotate(square_region, cv2.ROTATE_180)
center = (square_size // 2, square_size // 2)
rotation_matrix_75 = cv2.getRotationMatrix2D(center, -75, 1.0)
rotated_minus_75 = cv2.warpAffine(square_region, rotation_matrix_75, (square_size, square_size))

image_180 = image.copy()
image_180[start_y:start_y+square_size, start_x:start_x+square_size] = rotated_180
cv2.rectangle(image_180, (start_x, start_y), (start_x+square_size, start_y+square_size), (0, 255, 0), 2)

image_minus_75 = image.copy()
image_minus_75[start_y:start_y+square_size, start_x:start_x+square_size] = rotated_minus_75
cv2.rectangle(image_minus_75, (start_x, start_y), (start_x+square_size, start_y+square_size), (0, 255, 0), 2)

cv2.imencode('.jpg', image_180)[1].tofile(os.path.join(results_dir, 'повернуто_180.jpg'))
cv2.imencode('.jpg', image_minus_75)[1].tofile(os.path.join(results_dir, 'повернуто_-75.jpg'))