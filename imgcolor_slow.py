#フォルダ内の画像の色の平均値を計算し、色の名前をパーセントで出力する

from PIL import Image
import webcolors
import os

def calculate_average_color(image_path):
    # 画像を開く
    image = Image.open(image_path)

    # 画像をRGBモードに変換
    image_rgb = image.convert('RGB')

    # 画像の幅と高さを取得
    width, height = image_rgb.size

    # 各色の合計を初期化
    total_red = 0
    total_green = 0
    total_blue = 0

    # 画像のすべてのピクセルを走査して色を合計
    for x in range(width):
        for y in range(height):
            r, g, b = image_rgb.getpixel((x, y))
            total_red += r
            total_green += g
            total_blue += b

    # 色の平均値を計算
    num_pixels = width * height
    average_red = total_red // num_pixels
    average_green = total_green // num_pixels
    average_blue = total_blue // num_pixels

    # RGB値を返す
    return average_red, average_green, average_blue

# 色の名前を取得（入力値に近い物）
def closest_color(requested_color):
    min_colors = {}
    for key, name in webcolors.CSS21_HEX_TO_NAMES.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_color[0]) ** 2
        gd = (g_c - requested_color[1]) ** 2
        bd = (b_c - requested_color[2]) ** 2
        min_colors[(rd + gd + bd)] = name
    return min_colors[min(min_colors.keys())]

# フォルダ内の画像ファイルを取得
def get_image_files(folder_path):
    return [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith(('.jpg', '.jpeg', '.png'))]

# フォルダ内の画像の平均色を計算
def imgcolor(folder_path):
    # 画像の平均色を格納する配列
    result = ""
    count = 0
    closest_colors = {}

    # 各画像の平均色を計算し、配列に格納
    for image_path in get_image_files(folder_path):
        count += 1
        average_color = calculate_average_color(image_path)

        # 色が既に連想配列に存在するか確認
        if closest_color(average_color) in closest_colors:
            closest_colors[closest_color(average_color)] += 1
        else:
            closest_colors[closest_color(average_color)] = 1

    # 色の出現回数を降順にソートして確率を計算
    closest_colors = sorted(closest_colors.items(), key=lambda x:x[1], reverse=True)

    for i in range(len(closest_colors)):
        percent = round(closest_colors[i][1] / count * 100, 2)
        color = closest_colors[i][0]
        result = result + color + " " +  str(percent) + "%,"
        # print(color + " " +  str(percent) + "%,", end="")
    return result

# 画像フォルダのパスを指定
folder_path = './img'
print(imgcolor(folder_path))