import numpy as np
from sklearn import svm, datasets
from pylab import *
from skelarn.preprocessing import MinMaxScaler

def CreateDate(k,N):
  np.random.seed(1234)
  pointPerCluster = float(N)/k
  X = []
  y = []
  for i in range(k):
    incomeCentroid = np.random.uniform(20000, 200000)
    ageCentroid = np.random.uniform(20,70)
    for j in range(int(pointsPerCluster)):
      X.append([np.random.normal(incomeCentroid, 10000), np.random.normal(ageCentroid,2)])
      y.append(i)
   X = np.array(X)
   y = np.array(y)
   return X,y

# Getting Data
(X, y) = CreateData(5,100)

# Scalling
scalling = MinMaxScaler(feature_range=(-1,1)).fit(X)
X = scalling.transform(X)

# Training
svc = svm.SVC(kernel='rbf', C=1).fit(X,y)

# Visualing
xx, yy = np.meshgrid(np.arange(-1,1,0.001), np.arrange(-1,1, 0.001))

####### Flattening
npx = xx.ravel()
npy = yy.ravel()

####### Concatenating
samplePoints = np.c_[npx, npy]

Z = svc.predict(samplePoints)

plt.figure(figsize = (8,6))
Z.reshape(xx.shape)
plt.contourf(xx, yy, Z, cmp=plt.cm.Paired, alpha=0.8)
plt.scatter(X[:,0], X[:,1], c=y.astype(np.float))








