import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler

X = np.random.randn(200,3)
X = StandardScaler().fit_transform(X)

model = DBSCAN(eps=0.5, min_samples=5)
labels = model.fit_predict(X)

print("Clusters:", set(labels))
