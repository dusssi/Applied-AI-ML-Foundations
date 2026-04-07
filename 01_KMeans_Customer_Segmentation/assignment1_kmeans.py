import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

data = pd.DataFrame({
    'Income': np.random.randint(20000,100000,200),
    'Score': np.random.randint(1,100,200),
    'Age': np.random.randint(18,70,200)
})

X = StandardScaler().fit_transform(data)
kmeans = KMeans(n_clusters=4, random_state=42)
data['Cluster'] = kmeans.fit_predict(X)

print(data.head())
