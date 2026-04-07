from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier

X,y = load_breast_cancer(return_X_y=True)

models = [
    LogisticRegression(max_iter=1000),
    SVC(probability=True),
    RandomForestClassifier()
]

for m in models:
    m.fit(X,y)
    print(type(m).__name__, "trained")
