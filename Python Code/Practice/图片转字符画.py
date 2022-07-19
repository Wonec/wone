from PIL import Image

# 使用到的字符集
code_lib = '''$@B%8&WM#*oahkbdpqw mZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_ +~<>i!lI;:,"^`'.'''
count = len(code_lib)

# 将彩色图片转换为黑白图片
def transform(image_file):
    image_file = image_file.convert("L")
    codePic = ""

    for h in range(0, image_file.size[1]):  # 纵向
        for w in range(0, image_file.size[0]):  # 横向
            gray = image_file.getpixel((w, h))
            codePic = codePic + code_lib[int(((count) * gray) / 256)]

        codePic = codePic + "\r\n"  # 每行结尾自动换行

    return codePic

fp = open(u"xxx.jpg", 'rb')
image_file = Image.open(fp)
image_file = image_file.resize((int(image_file.size[0] * 0.5), int(image_file.size[1] * 0.25)))

tmp = open('result.txt', 'w')
tmp.write(transform(image_file))
tmp.close()

