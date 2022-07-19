import cv2

# 读取图片
position = input(r"请输入文件路径：")
img = cv2.imread(position)

# 解析二维码
detector = cv2.QRCodeDetector()
data, bbox, straight_qrcode = detector.detectAndDecode(img)

# 输出结果
print(data)
input('')
