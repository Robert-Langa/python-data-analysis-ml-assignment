import sys
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Load dataset
iris = load_iris()

# Get command-line inputs
sepal_length = float(sys.argv[1])
sepal_width = float(sys.argv[2])
petal_length = float(sys.argv[3])
petal_width = float(sys.argv[4])

# Create input array
X_new = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, random_state=0
)

# Create 3-NN classifier
knn = KNeighborsClassifier(n_neighbors=3)

# Train model
knn.fit(X_train, y_train)

# Predict
prediction = knn.predict(X_new)

# Output only class name
print(iris.target_names[prediction][0])
