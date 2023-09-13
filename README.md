# Establishment-and-evaluation-of-handwritten-digit-recognition-model
一、使用支持向量机对随机生成的数字图像进行分类:
首  先定义一个函数 generateDigits(dstDir,num) 来随机生成num个数字图像，并存储在文件夹dstDir中。再定义另一个函数loadDigits(dstDir) 来读取dstDir文件夹中图像的数字信息，
对图像空白处就行处理，并按照标准进行分类。最后将生成的数据随机划分训练集和测试集，运用训练集来创建和训练模型，再通过测试集对模型进行评分。
run temp.py
二、使用交叉验证评估模型泛化能力
分别使用K折叠、随机拆分、逐个测试交叉验证对手写数字识别的支持向量机分类算法进行模型泛化能力评估，并将三种交叉验证评估结果进行对比。由于逐个测试交叉验证运行时间过长，没能获得该验证结果。  
run Cross_validation.py
三、使用网格搜索确定模型最佳参数
对手写数字的支持向量机分类算法模型赋予不同参数值，对于每组参数使用交叉验证对模型进行评分，从中选出最佳参数。
run GridSearchCV.py
