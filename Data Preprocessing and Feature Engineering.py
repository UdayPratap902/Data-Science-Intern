import pandas as pd
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt

# Load datasets
train_df = pd.read_csv('train.csv')
test_df = pd.read_csv('test.csv')

# Print out the column names to verify
print("Columns in train_df:", train_df.columns)
print("Columns in test_df:", test_df.columns)

# Inspect the data
print("Train Data:")
print(train_df.head())
print(train_df.info())
print(train_df.describe())

# Handle missing values
# For categorical features
categorical_columns = ['Alley', 'MasVnrType', 'BsmtQual', 'BsmtCond', 'BsmtExposure', 'BsmtFinType1', 
                        'BsmtFinType2', 'FireplaceQu', 'GarageType', 'GarageFinish', 'CentralAir', 
                        'Electrical', 'KitchenQual', 'Functional', 'PoolQC', 'Fence', 'MiscFeature', 
                        'SaleType', 'SaleCondition']

for col in categorical_columns:
    if col in train_df.columns:
        mode_value = train_df[col].mode()[0]
        train_df[col] = train_df[col].fillna(mode_value)

# For numerical features
numerical_columns = ['LotFrontage', 'LotArea', 'MasVnrArea', 'BsmtFinSF1', 'BsmtFinSF2', 'BsmtUnfSF', 
                      'TotalBsmtSF', '1stFlrSF', '2ndFlrSF', 'LowQualFinSF', 'GrLivArea', 'BsmtFullBath', 
                      'BsmtHalfBath', 'FullBath', 'HalfBath', 'BedroomAbvGr', 'KitchenAbvGr', 'TotRmsAbvGrd', 
                      'Fireplaces', 'GarageYrBlt', 'GarageCars', 'GarageArea', 'WoodDeckSF', 'OpenPorchSF', 
                      'EnclosedPorch', '3SsnPorch', 'ScreenPorch', 'PoolArea', 'MiscVal']

for col in numerical_columns:
    if col in train_df.columns:
        median_value = train_df[col].median()
        train_df[col] = train_df[col].fillna(median_value)

# Convert categorical variables to numerical using One-Hot Encoding
train_df = pd.get_dummies(train_df, columns=[col for col in categorical_columns if col in train_df.columns])

# Normalization/Scaling
scaler = StandardScaler()
train_df[numerical_columns] = scaler.fit_transform(train_df[numerical_columns])

# Create new features
train_df['HouseAge'] = train_df['YrSold'] - train_df['YearBuilt']
train_df['RemodelAge'] = train_df['YrSold'] - train_df['YearRemodAdd']

# Ensure all columns are numeric before calculating the correlation matrix
numeric_df = train_df.select_dtypes(include=['float64', 'int64'])

# Feature Selection (example: correlation heatmap)
plt.figure(figsize=(12, 10))
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
plt.show()

# Save the processed data
train_df.to_csv('train_processed.csv', index=False)
test_df.to_csv('test_processed.csv', index=False)
