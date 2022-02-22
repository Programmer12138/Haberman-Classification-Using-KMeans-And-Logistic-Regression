# Haberman-Classification-Using-KMeans-And-Logistic-Regression
基于KMeans和逻辑回归算法的Haberman癌症分类<br>
运行效果：<br>
![3d](https://user-images.githubusercontent.com/72424079/150261998-fcc901a8-2527-4637-8160-77c7c76d1944.PNG)
![km](https://user-images.githubusercontent.com/72424079/150262023-5b6e434b-04e7-444a-9424-6dff8424632f.PNG)
![lr](https://user-images.githubusercontent.com/72424079/150262039-b237d6ac-86bd-4146-89e6-d832a3bf9f77.PNG)
<br>
<br>
原理简介：<br>
根据样本在空间的分布远近，将样本划分为不同的类，也就是给样本贴上不同的标签。比如说根据身高体重用聚类算法分类胖瘦，每一个样本就是二维坐标系里的一个点，横轴是身高，纵轴是体重，标签就是胖或者瘦。样本点离哪个聚类中心近，就被分为哪一类。<br>
这就是kmeans的大致原理。<br>
<br>
逻辑回归原理：<br>
logistic回归是一种广义线性回归（generalized linear model），因此与多重线性回归分析有很多相同之处。它们的模型形式基本上相同，都具有 w‘x+b，其中w和b是待求参数，其区别在于他们的因变量不同，多重线性回归直接将w‘x+b作为因变量，即y =w‘x+b，而logistic回归则通过函数L将w‘x+b对应一个隐状态p，p =L(w‘x+b),然后根据p 与1-p的大小决定因变量的值。如果L是logistic函数，就是logistic回归，如果L是多项式函数就是多项式回归。<br>
<br>
代码实现：<br>
涉及的第三方包：sklearn包	<br>
所用函数：KMeans(n_clusters=划分类别的个数) <br>
np.array函数把输入的数据变成numpy格式的数组<br>		
fit函数进行迭代训练<br>
predict函数进行预测，该函数输出的结果就是样本属于的类，比如在二分类的问题中输出的结果就是0或者1<br>
![image](https://user-images.githubusercontent.com/72424079/155089191-262c8df5-dabd-4783-89cb-682d0debd8cf.png)<br>
![image](https://user-images.githubusercontent.com/72424079/155089845-9a4a34c0-787b-4270-aa6d-1e538fd53285.png)
