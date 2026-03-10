from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Load dataset
iris = load_iris()

# Split data (50/50 split, fixed random state)
X_train, X_test, y_train, y_test = train_test_split(
    iris.data,
    iris.target,
    test_size=0.5,
    random_state=0
)

k_values = [1, 5, 15]
best_k = None
best_score = 0

for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    score = knn.score(X_test, y_test)
    
    print(f"k={k}, accuracy={score:.4f}")
    
    if score > best_score:
        best_score = score
        best_k = k

print(f"Best k: {best_k} with accuracy: {best_score:.4f}")
