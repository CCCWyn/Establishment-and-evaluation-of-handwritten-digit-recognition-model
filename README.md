# Establishment-and-evaluation-of-handwritten-digit-recognition-model

[![license](https://camo.githubusercontent.com/4738d430387c93da0d49ef0428a7c7ddae18e81eaff99a014996d4f6b30fd3ef/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6963656e73652f3a757365722f3a7265706f2e737667)](https://github.com/RichardLitt/standard-readme/blob/main/example-readmes/LICENSE) [![standard-readme compliant](https://camo.githubusercontent.com/f116695412df39ab3c98d8291befdb93af123f56aecc79fff4b20c410a5b54c7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f726561646d652532307374796c652d7374616e646172642d627269676874677265656e2e7376673f7374796c653d666c61742d737175617265)](https://github.com/RichardLitt/standard-readme)

This is an example file with maximal choices selected.

This is a long description.

## Table of Contents

- [SVM](#SVM)
- [Cross-validation](#Cross-validation)
- [GridSearchCV](#GridSearchCV)


## SVM

just run the following command:

```
run temp.py
```

一、使用支持向量机对随机生成的数字图像进行分类.
首先定义一个函数 generateDigits(dstDir,num) 来随机生成num个数字图像，并存储在文件夹dstDir中。再定义另一个函数loadDigits(dstDir) 来读取dstDir文件夹中图像的数字信息，对图像空白处就行处理，并按照标准进行分类。最后将生成的数据随机划分训练集和测试集，运用训练集来创建和训练模型，再通过测试集对模型进行评分。





## Cross-validation

just run the following command:

```
run Cross-validation.py
```
二、使用交叉验证评估模型泛化能力
分别使用K折叠、随机拆分、逐个测试交叉验证对手写数字识别的支持向量机分类算法进行模型泛化能力评估，并将三种交叉验证评估结果进行对比。



## GridSearchCV

just run the following command:

```
run GridSearchCV.py
```

三、使用网格搜索确定模型最佳参数
对手写数字的支持向量机分类算法模型赋予不同参数值，对于每组参数使用交叉验证对模型进行评分，从中选出最佳参数。


