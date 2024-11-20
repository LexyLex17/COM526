from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score, matthews_corrcoef, \
    confusion_matrix, ConfusionMatrixDisplay
import pandas as pd
import matplotlib.pyplot as plt

# Load in the dataset from CSV using Pandas
data = pd.read_csv("iris.csv")

X = data.drop(["species"], axis=1)
y = data["species"]

# Split data into training samples and test samples
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=33)

# Create a decision tree classifier
dt = DecisionTreeClassifier()

# Train Decision Tree Classifier
dt_model = dt.fit(X_train, y_train)

# Test the model against the test data
dt_pred = dt_model.predict(X_test)

# For multiclass situations, you need to take in to account the average parameter. Details of options can
# be found here for f1 score and is similar on other metrics:
# https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.f1_score.html
print(f"Accuracy is {accuracy_score(y_test, dt_pred)}")
print(f"Recall is {recall_score(y_test, dt_pred, average='macro')}")
print(f"Precision is {precision_score(y_test, dt_pred, average='macro')}")
print(f"F1-Score is {f1_score(y_test, dt_pred, average='macro')}")
print(f"MCC is {matthews_corrcoef(y_test, dt_pred)}")

# See the confusion matrix
cm = confusion_matrix(y_test, dt_pred, labels=dt_model.classes_)
cm_visual = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=dt_model.classes_)
cm_visual.plot()
plt.show()