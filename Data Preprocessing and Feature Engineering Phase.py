import pandas as pd
import os

def load_titanic():
    # Check if the file exists before trying to load it
    if os.path.exists("titanic.csv"):
        data = pd.read_csv("titanic.csv")
        return data
    else:
        print("Error: 'titanic.csv' file not found.")
        return pd.DataFrame()

def preprocess_data(df):
    # Print the initial DataFrame
    print("Initial DataFrame:")
    print(df.head())
    
    # Example preprocessing
    print("\nData Info:")
    print(df.info())
    
    # Handle missing values
    df['Age'] = df['Age'].fillna(df['Age'].median())  # Fill missing ages with median
    df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])  # Fill missing embarked values with mode
    
    # Drop columns that are not useful
    if 'PassengerId' in df.columns:
        df.drop(['PassengerId'], axis=1, inplace=True)
    
    # Convert categorical columns to numerical
    df = pd.get_dummies(df, columns=['Sex', 'Embarked'], drop_first=True)
    
    # Print updated DataFrame
    print("\nDataFrame after preprocessing:")
    print(df.head())

def main():
    # Load the dataset
    df_titanic = load_titanic()
    
    # Check if DataFrame is not empty
    if not df_titanic.empty:
        # Preprocess the dataset
        preprocess_data(df_titanic)
    else:
        print("No data to preprocess.")

if __name__ == "__main__":
    main()
