from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

X = load_iris().data

X_pca = PCA(n_components=2).fit_transform(X)
labels = KMeans(n_clusters=3).fit_predict(X_pca)

print(labels[:10])
