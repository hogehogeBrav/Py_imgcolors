from PIL import Image
import webcolors
import os
import numpy as np

def calculate_average_color(image_path):
    image = Image.open(image_path)
    image_rgb = image.convert('RGB')
    pixels = np.array(image_rgb)
    average_color = np.mean(pixels, axis=(0, 1))
    return tuple(map(int, average_color))

def closest_color(requested_color):
    min_colors = {}
    for key, name in webcolors.CSS21_HEX_TO_NAMES.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_color[0]) ** 2
        gd = (g_c - requested_color[1]) ** 2
        bd = (b_c - requested_color[2]) ** 2
        min_colors[(rd + gd + bd)] = name
    return min_colors[min(min_colors.keys())]

folder_path = './img'
image_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

count = 0
closest_colors = {}

for image_path in image_files:
    count += 1
    average_color = calculate_average_color(image_path)
    color_name = closest_color(average_color)
    
    if color_name:
        closest_colors[color_name] = closest_colors.get(color_name, 0) + 1

closest_colors = sorted(closest_colors.items(), key=lambda x: x[1], reverse=True)

for i in range(len(closest_colors)):
    percent = round(closest_colors[i][1] / count * 100, 2)
    color = closest_colors[i][0]
    print(color + str(percent) + "% ")