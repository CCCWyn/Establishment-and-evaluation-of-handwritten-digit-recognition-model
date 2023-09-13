from os import listdir
from os.path import basename
from PIL import Image
from sklearn import svm
from sklearn.model_selection import train_test_split

# 设定手写数字图像的尺寸、图片中数字字体大小、噪点比例
width,height=30,60

def loadDigits(dstDir='datasets'):
    # 获取所有图像文件名
    digitsFile=[dstDir+'\\'+fn for fn in listdir(dstDir) if fn.endswith('.jpg')]
    # 按编号排序
    digitsFile.sort(key=lambda fn:int(basename(fn) [:-4]))
    # digitsData 用于存放读取的图片中数字信息
    # 每个图片中所有像素值存放于digitsData 中的一行数据
    digitsData=[]
    for fn in digitsFile:
        with Image.open(fn) as im:
            # getpixel() 方法用来读取指定位置像素的颜色值
            data=[sum(im.getpixel((w,h)))/len(im.getpixel((w,h)))
                  for w in range(width)
                  for h in range(height)]
            digitsData.append(data)
    # digitsLabel 用于存放图片中数字的标准分类
    with open(dstDir+'\\digits.txt') as fp:
        digitsLabel=fp.readlines()
    # 删除数字字符两侧的空白字符
    digitsLabel=[label.strip() for label in digitsLabel]
    return(digitsData,digitsLabel)
    
# 加载数据
data=loadDigits()
print('数据加载完成')

# 随机划分训练集和测试集，其中参数 test_size 用来指定测试集大小
X_train,X_test,y_train,y_test=train_test_split(data[0],data[1],test_size=0.1)

# 创建并训练模型
svcClassifier=svm.SVC(kernel='linear',C=1000,gamma=0.001)
svcClassifier.fit(X_train,y_train)
print('模型训练完成。')

# 使用测试集对模型进行评分
score=svcClassifier.score(X_test,y_test)
print('模型测试得分：',score)

