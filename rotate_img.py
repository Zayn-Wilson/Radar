from PIL import Image

def rotate_image(image_path, clockwise=True):
    # 打开图片
    img = Image.open(image_path)
    
    # 确定旋转角度
    # 顺时针旋转 270° 等同于逆时针旋转 90°
    angle = -90 if clockwise else 90
    
    # 旋转图片
    rotated_img = img.rotate(angle, expand=True)
    
    # 生成输出文件名
    direction = "clockwise" if clockwise else "counterclockwise"
    output_path = f"2025map_rotated_{direction}.png"
    
    # 保存旋转后的图片
    rotated_img.save(output_path)
    print(f"已保存旋转后的图片到: {output_path}")

# 主函数
def main():
    image_path = "images/map.jpg"
    
    # 顺时针旋转
    rotate_image(image_path, clockwise=True)
    
    # 逆时针旋转
    rotate_image(image_path, clockwise=False)

if __name__ == "__main__":
    main()