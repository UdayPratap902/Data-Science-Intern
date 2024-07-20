import seaborn as sns  # Importing the seaborn library for visualization
import matplotlib.pyplot as plt  # Importing the matplotlib library for plotting

# Load the Iris dataset from seaborn
# The Iris dataset contains measurements of iris flowers of three species: Setosa, Versicolor, and Virginica
iris = sns.load_dataset("iris")

# Display the first few rows of the dataset to understand its structure
print(iris.head())

# Pairplot: This plot shows pairwise relationships in the dataset
# It helps to visualize the relationships between each pair of features (sepal length, sepal width, petal length, petal width)
# The 'hue' parameter adds colors based on species, making it easy to distinguish between different species
sns.pairplot(iris, hue='species', markers=["o", "s", "D"])
plt.suptitle("Pairplot of Iris Dataset", y=1.02)  # Adding a title to the plot
plt.show()  # Display the plot

# Boxplot: This plot shows the distribution of a single feature for each species
# It displays the median, quartiles, and potential outliers
# Boxplots help in comparing the distribution of features between different species

# Boxplot for Sepal Length by Species
plt.figure(figsize=(10, 6))  # Setting the size of the plot
sns.boxplot(x='species', y='sepal_length', data=iris)  # Creating the boxplot
plt.title("Boxplot of Sepal Length by Species")  # Adding a title
plt.show()  # Display the plot

# Boxplot for Sepal Width by Species
plt.figure(figsize=(10, 6))  # Setting the size of the plot
sns.boxplot(x='species', y='sepal_width', data=iris)  # Creating the boxplot
plt.title("Boxplot of Sepal Width by Species")  # Adding a title
plt.show()  # Display the plot

# Boxplot for Petal Length by Species
plt.figure(figsize=(10, 6))  # Setting the size of the plot
sns.boxplot(x='species', y='petal_length', data=iris)  # Creating the boxplot
plt.title("Boxplot of Petal Length by Species")  # Adding a title
plt.show()  # Display the plot

# Boxplot for Petal Width by Species
plt.figure(figsize=(10, 6))  # Setting the size of the plot
sns.boxplot(x='species', y='petal_width', data=iris)  # Creating the boxplot
plt.title("Boxplot of Petal Width by Species")  # Adding a title
plt.show()  # Display the plot

# Violin Plot: This plot combines a boxplot with a kernel density plot
# It provides a richer visualization of the data distribution
# Violin plots show the density of the data at different values

# Violin Plot for Sepal Length by Species
plt.figure(figsize=(10, 6))  # Setting the size of the plot
sns.violinplot(x='species', y='sepal_length', data=iris)  # Creating the violin plot
plt.title("Violin Plot of Sepal Length by Species")  # Adding a title
plt.show()  # Display the plot

# Violin Plot for Sepal Width by Species
plt.figure(figsize=(10, 6))  # Setting the size of the plot
sns.violinplot(x='species', y='sepal_width', data=iris)  # Creating the violin plot
plt.title("Violin Plot of Sepal Width by Species")  # Adding a title
plt.show()  # Display the plot

# Violin Plot for Petal Length by Species
plt.figure(figsize=(10, 6))  # Setting the size of the plot
sns.violinplot(x='species', y='petal_length', data=iris)  # Creating the violin plot
plt.title("Violin Plot of Petal Length by Species")  # Adding a title
plt.show()  # Display the plot

# Violin Plot for Petal Width by Species
plt.figure(figsize=(10, 6))  # Setting the size of the plot
sns.violinplot(x='species', y='petal_width', data=iris)  # Creating the violin plot
plt.title("Violin Plot of Petal Width by Species")  # Adding a title
plt.show()  # Display the plot

