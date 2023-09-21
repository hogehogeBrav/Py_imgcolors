# 一番近い色を出力

import webcolors

def closest_color(requested_color):
    min_colors = {}
    for key, name in webcolors.CSS3_HEX_TO_NAMES.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_color[0]) ** 2
        gd = (g_c - requested_color[1]) ** 2
        bd = (b_c - requested_color[2]) ** 2
        min_colors[(rd + gd + bd)] = name
    return min_colors[min(min_colors.keys())]

# RGB値を指定 (例: 赤色)
requested_rgb = (209, 89, 100)

# 一番近い色の名前を取得
closest_name = closest_color(requested_rgb)

print("RGB値:", requested_rgb)
print("一番近い色の名前:", closest_name)