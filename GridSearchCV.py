from time import time
from os import listdir
from os.path import basename
from PIL import Image
from sklearn import svm
from sklearn.model_selection import GridSearchCV

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

# 创建模型
svcClassifier=svm.SVC()
parameters={'kernel':('linear','rbf'),'C':(0.001,1,10,100,1000),'gamma':(0.001,0.1,0.5,1,10)}

# 使用网格搜索寻找最佳参数
start=time()
clf=GridSearchCV(svcClassifier,parameters)
clf.fit(data[0],data[1])

print(clf.best_params_)
print('得分：',clf.score(data[0],data[1]))
print('用时（秒）：',time()-start)



