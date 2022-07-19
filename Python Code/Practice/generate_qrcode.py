import qrcode

# 需要生成的地址
data = input("请输入网址：")
# 生成文件名称
filename = input("请输入文件名称：")
# 生成二维码
img = qrcode.make(data)
# 保存文件
img.save(filename)