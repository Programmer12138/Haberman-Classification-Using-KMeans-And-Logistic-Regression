import pandas as pd
import numpy as np
import matplotlib.pyplot as mp
from sklearn.cluster import KMeans
from sklearn.linear_model import LogisticRegression
data = pd.read_excel('haberman_data.xlsx')
attr1 = data.iloc[0:, 0:1].values
attr2 = data.iloc[0:, 1:2].values
attr3 = data.iloc[0:, 2:3].values
lable = amount=data.iloc[0:, 3:4].values
#print(attr1)
#三维数据可视化
x = np.array(attr1)
y = np.array(attr2)
z = np.array(attr3)
mp.figure("3D Scatter", facecolor="lightgray")
ax3d = mp.gca(projection="3d")
mp.title('3D Scatter', fontsize=20)
ax3d.set_xlabel('attr1', fontsize=14)
ax3d.set_ylabel('attr2', fontsize=14)
ax3d.set_zlabel('attr3', fontsize=14)
mp.tick_params(labelsize=10)
ax3d.scatter(x, y, z, s=20, cmap="jet", marker="o")
mp.show()
#使用k均值聚类算法对数据进行分类
estimator=KMeans(n_clusters=2)
kmeans_data=data.iloc[0:, 0:3].values
kmeans_data=np.array(kmeans_data)
#print(kmeans_data)
estimator.fit(kmeans_data)
y_pre=estimator.predict(kmeans_data)
#展示聚类的结果
color=["red","green"]
mp.figure("3D Scatter", facecolor="lightgray")
ax3d = mp.gca(projection="3d")
mp.title('result of k-means', fontsize=20)
ax3d.set_xlabel('attr1', fontsize=14)
ax3d.set_ylabel('attr2', fontsize=14)
ax3d.set_zlabel('attr3', fontsize=14)
mp.tick_params(labelsize=10)
ax3d.scatter(x[y_pre==0], y[y_pre==0], z[y_pre==0], s=20, cmap="jet", marker="o",color=color[0])
ax3d.scatter(x[y_pre==1], y[y_pre==1], z[y_pre==1], s=20, cmap="jet", marker="o",color=color[1])
mp.show()
#使用逻辑回归经行分类
estimator=LogisticRegression()
x_train=data.iloc[0:299, 0:3].values
y_train=data.iloc[0:299, 3:4].values
#print(y_train)
estimator.fit(x_train,y_train)
x_test=data.iloc[0:, 0:3].values
y_pre=estimator.predict(x_test)
#展示逻辑回归预测的结果
mp.figure("3D Scatter", facecolor="lightgray")
ax3d = mp.gca(projection="3d")
mp.title('result of logic regression', fontsize=20)
ax3d.set_xlabel('attr1', fontsize=14)
ax3d.set_ylabel('attr2', fontsize=14)
ax3d.set_zlabel('attr3', fontsize=14)
mp.tick_params(labelsize=10)
ax3d.scatter(x[y_pre==2], y[y_pre==2], z[y_pre==2], s=20, cmap="jet", marker="o",color=color[0])
ax3d.scatter(x[y_pre==1], y[y_pre==1], z[y_pre==1], s=20, cmap="jet", marker="o",color=color[1])
mp.show()