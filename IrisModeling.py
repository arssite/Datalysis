#!/usr/bin/env python
# coding: utf-8

# # IrisFlowerDataSet

# In[1]:


#Step 1: Import Libraries
#Let's start by importing the necessary libraries. We'll use scikit-learn for the machine learning tasks and pandas for data preprocessing.
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report



# In[2]:


#Step 2: Load the Dataset
#Next, we'll load the Iris dataset. We can directly import it from scikit-learn's built-in datasets.

from sklearn.datasets import load_iris
iris_data = load_iris()


# In[5]:


#Step 3: Data Preprocessing
#Now, we'll preprocess the data. We'll convert the dataset into a pandas DataFrame and split it into features (X) and labels (y). We'll also split the data into training and testing sets.
# Convert dataset to pandas DataFrame
df = pd.DataFrame(data=iris_data.data, columns=iris_data.feature_names)
df['target'] = iris_data.target

# Split features and labels
X = df.drop('target', axis=1)
y = df['target']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# In[6]:


#Step 4: Feature Scaling
#We'll perform feature scaling to normalize the input data. This is important for some machine learning algorithms, such as SVM.
# Scale the features using StandardScaler
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


# In[7]:


#Step 5: Model Training
#Next, we'll train our machine learning model. In this example, we'll use a Support Vector Classifier (SVC) from scikit-learn.
# Create an SVC classifier
classifier = SVC()
# Train the model
classifier.fit(X_train, y_train)


# In[8]:


#Step 6: Model Evaluation
#Finally, we'll evaluate the trained model by making predictions on the test set and calculating the accuracy and classification report.
# Make predictions on the test set
y_pred = classifier.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")

# Generate classification report
report = classification_report(y_test, y_pred)
print(f"Classification Report:\n{report}")


# In[ ]:




