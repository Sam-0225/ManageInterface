import random
import string

from PIL import Image, ImageDraw, ImageFont, ImageFilter


def check_captcha(width=120, height=30, char_length=5, font_file='monaco.ttf', font_size=28):
    code = []
    img = Image.new(mode='RGB', size=(width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(img, mode='RGB')

    def rnd_char():
        """
        生成隨機文字
        :return:
        """
        # result = random.choice([chr(random.randint(65, 90)), str(random.randint(0, 9))])
        # return result
        characters = string.ascii_uppercase + string.digits
        return random.choice(characters)


    def rnd_color():
        """
        生成隨機顏色
        :return:
        """
        return random.randint(0, 255), random.randint(10, 255), random.randint(64, 255)

    # 畫文字
    font = ImageFont.truetype(font_file, font_size)
    for i in range(char_length):
        char = rnd_char()
        code.append(char)
        h = random.randint(0, 4)
        draw.text([i * width / char_length, h], char, font=font, fill=rnd_color())

    # 畫干擾點
    for i in range(40):
        draw.point([random.randint(0, width), random.randint(0, height)], fill=rnd_color())

    # 畫干擾圓圈
    for i in range(40):
        draw.point([random.randint(0, width), random.randint(0, height)], fill=rnd_color())
        x = random.randint(0, width)
        y = random.randint(0, height)
        draw.arc((x, y, x + 4, y + 4), 0, 90, fill=rnd_color())

    # 畫干擾線
    for i in range(5):
        x1 = random.randint(0, width)
        y1 = random.randint(0, height)
        x2 = random.randint(0, width)
        y2 = random.randint(0, height)

        draw.line((x1, y1, x2, y2), fill=rnd_color())

    img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
    return img, ''.join(code)


if __name__ == '__main__':
    # 1. 直接打開
    # img,code = check_code()
    # img.show()

    # 2. 寫入檔案
    # img,code = check_code()
    # with open('code.png','wb') as f:
    #     img.save(f,format='png')

    # 3. 寫入記憶體(Python3)
    # from io import BytesIO
    # stream = BytesIO()
    # img.save(stream, 'png')
    # stream.getvalue()

    pass