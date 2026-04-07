from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier

X,y = make_classification(n_samples=500,n_features=10)
model = RandomForestClassifier()
model.fit(X,y)

print("Model trained")
