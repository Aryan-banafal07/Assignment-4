import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load Titanic dataset
titanic_data = sns.load_dataset('titanic')

# Basic info
print("Dataset Info:")
titanic_data.info()

# Describe all columns
print("\nDescriptive Statistics:")
print(titanic_data.describe(include='all'))

# Missing values
missing = titanic_data.isnull().sum()
missing = missing[missing > 0].sort_values(ascending=False)

plt.figure(figsize=(10, 5))
sns.barplot(x=missing.values, y=missing.index, palette="coolwarm")
plt.title("Missing Values by Column")
plt.xlabel("Missing Count")
plt.ylabel("Column")
plt.show()

# Target distribution
sns.countplot(x='survived', data=titanic_data, palette='Set2')
plt.title("Survival Count")
plt.show()

# Passenger class
sns.countplot(x='pclass', data=titanic_data, palette='Set3')
plt.title("Passenger Class")
plt.show()

# Gender distribution
sns.countplot(x='sex', data=titanic_data, palette='Set1')
plt.title("Gender Distribution")
plt.show()

# Age distribution
plt.figure(figsize=(8, 5))
sns.histplot(titanic_data['age'].dropna(), bins=30, kde=True, color='skyblue')
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

# Fare distribution
plt.figure(figsize=(8, 5))
sns.histplot(titanic_data['fare'], bins=40, kde=True, color='salmon')
plt.title("Fare Distribution")
plt.xlabel("Fare")
plt.xlim(0, 300)
plt.show()

# Outlier detection
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
sns.boxplot(x='age', data=titanic_data)
plt.title("Age Outliers")
plt.subplot(1, 2, 2)
sns.boxplot(x='fare', data=titanic_data)
plt.title("Fare Outliers")
plt.tight_layout()
plt.show()

# Gender vs Survival
sns.countplot(x='sex', hue='survived', data=titanic_data, palette='pastel')
plt.title("Survival by Gender")
plt.xlabel("Sex")
plt.ylabel("Count")
plt.legend(title='Survived')
plt.show()

# Class vs Survival
sns.countplot(x='pclass', hue='survived', data=titanic_data, palette='pastel')
plt.title("Survival by Class")
plt.xlabel("Class")
plt.ylabel("Count")
plt.legend(title='Survived')
plt.show()

# Age distribution by survival
plt.figure(figsize=(8, 6))
sns.kdeplot(data=titanic_data[titanic_data['survived'] == 1]['age'].dropna(), label='Survived', shade=True, color='green')
sns.kdeplot(data=titanic_data[titanic_data['survived'] == 0]['age'].dropna(), label='Did Not Survive', shade=True, color='red')
plt.title("Age Distribution by Survival")
plt.xlabel("Age")
plt.legend()
plt.show()

# Embarked vs Survival
sns.countplot(x='embarked', hue='survived', data=titanic_data, palette='pastel')
plt.title("Survival by Embarkation Port")
plt.xlabel("Embarked")
plt.ylabel("Count")
plt.legend(title='Survived')
plt.show()

# Correlation heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(titanic_data.corr(numeric_only=True), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()

# Encode categorical values for ML use (optional)
titanic_encoded = titanic_data.copy()
titanic_encoded['sex'] = titanic_encoded['sex'].map({'male': 0, 'female': 1})
titanic_encoded['embarked'] = titanic_encoded['embarked'].map({'S': 0, 'C': 1, 'Q': 2})

# Drop unnecessary columns
titanic_encoded = titanic_encoded.drop(columns=['deck', 'embark_town', 'alive', 'who', 'class', 'adult_male'])

# Preview cleaned data
print("\nEncoded Data Preview:")
print(titanic_encoded.head())
