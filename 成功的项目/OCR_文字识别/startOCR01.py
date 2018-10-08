from PIL import Image
import pytesseract

text = pytesseract.image_to_string(Image.open('b.jpg'), lang='chi_sim')
print("ok")
print(text)


# C:\Program Files (x86)\Tesseract-OCR\tessdata  chi_sim.traineddata
# C:\Users\Administrator\AppData\Local\Programs\Python\Python36\lib\site-packages\pytesseract

'''
tesseract-OCR,win7,python3.6,配置
1. 选用tesseract3.x,不用4.x
2. 安装到D盘好一些。（方便后面的查找复制）
3. 系统环境变量（2个名称都配置，也会自动配置的）
4. 把语语言包拖放到 data里面。
5. 修改 cmd 命令。


下一步是优化一下，搞成一个exe离线文件





'''
