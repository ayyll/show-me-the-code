from PIL import Image, ImageDraw, ImageFont
import sys

def add_red_number(image_path, number, output_path='result.jpg'):
    """
    在图片右上角添加红色数字提示
    :param image_path: 头像路径
    :param number: 要显示的数字（超过99显示为99+）
    :param output_path: 输出路径
    """
    # 打开图片
    img = Image.open(image_path).convert('RGB')
    
    # 创建绘图对象
    draw = ImageDraw.Draw(img)
    
    # 设置字体（需替换为系统存在的字体路径）
    try:
        font = ImageFont.truetype('arial.ttf', 60)  # Windows系统字体
    except:
        font = ImageFont.truetype('/Library/Fonts/Arial.ttf', 60)  # Mac系统字体
    
    # 处理超大数字
    text = str(number) if number <= 99 else "99+"
    
    # 计算文字尺寸和位置
    text_width = draw.textlength(text, font)
    img_width, img_height = img.size
    position = (img_width - text_width - 20, 20)  # 右上角偏移20像素
    
    # 绘制红色文字
    draw.text(position, text, fill=(255, 0, 0), font=font)
    
    # 保存结果
    img.save(output_path)
    print(f"处理完成，结果已保存至：{output_path}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法：python 0000.py [数字]")
        sys.exit(1)
    
    
    number = int(sys.argv[1])  # 强制转换为整数
    add_red_number("avatar.jpg", number)