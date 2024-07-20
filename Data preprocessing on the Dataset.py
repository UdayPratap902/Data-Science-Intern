import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load the Titanic dataset
url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
df = pd.read_csv(url)

# Display the first few rows of the dataset to understand its structure
print("Initial DataFrame:")
print(df.head())

# Data cleaning: Drop irrelevant columns
df.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1, inplace=True)

# Check for duplicates and drop them if any
print(f'Duplicates: {df.duplicated().sum()}')
df.drop_duplicates(inplace=True)

# Handling missing values
# Fill missing values in 'Age' with the mean
df['Age'] = df['Age'].fillna(df['Age'].mean())

# Fill missing values in 'Embarked' with the mode
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

# Check for any remaining missing values
print("\nMissing values after handling:")
print(df.isnull().sum())

# Transformation: Create a new feature 'FamilySize'
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1

# Drop the original 'SibSp' and 'Parch' columns
df.drop(['SibSp', 'Parch'], axis=1, inplace=True)

# Normalization: Initialize the scaler
scaler = StandardScaler()

# Select numerical columns for normalization
num_cols = ['Age', 'Fare', 'FamilySize']

# Fit and transform the numerical columns
df[num_cols] = scaler.fit_transform(df[num_cols])

# Display the first few rows of the transformed dataset
print("\nDataFrame after normalization:")
print(df.head())

# Encoding: One-hot encode the 'Sex' and 'Embarked' columns
df = pd.get_dummies(df, columns=['Sex', 'Embarked'], drop_first=True)

# Display the first few rows of the encoded dataset
print("\nDataFrame after encoding:")
print(df.head())

# Feature engineering example (already done: FamilySize)
# If needed, add more features based on domain knowledge

# Display the final preprocessed dataset
print("\nFinal preprocessed DataFrame:")
print(df.head())
