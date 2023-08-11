import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class EDA:

    def __init__(self, file_path):
        # Load necessary libraries and initialize DataFrame
        self.df = self.load_dataset(file_path)
        self.separator = '\n' + "=" * 50

        # Perform EDA tasks
        self.explore_data()
        self.clean_data()
        self.visualize_data()

    def load_dataset(self, file_path):
        # Load dataset based on file extension
        file_extension = file_path.split('.')[-1]
        if file_extension == 'csv':
            return pd.read_csv(file_path)
        elif file_extension == 'xlsx':
            return pd.read_excel(file_path)
        else:
            raise ValueError("Unsupported file format")

    def explore_data(self):
        # Display basic information and summary statistics
        print(
            f'Dataset Shape: {self.df.shape[0]} rows, {self.df.shape[1]} columns.{self.separator}')
        print(f'Basic Info:{self.separator}')
        self.df.info()
        print(
            f'Summary Statistics:{self.separator}\n{self.df.describe()}{self.separator}')

    def clean_data(self):
        # Handle duplicates
        n_duplicates = self.df.duplicated().sum()
        if n_duplicates > 0:
            self.df.drop_duplicates(inplace=True)
            print(f'Removed {n_duplicates} duplicated rows.{self.separator}')
        else:
            print('No duplicated rows found.')

        # Handle missing values
        if self.df.isna().any().any():
            print(f'Missing Values:\n{self.df.isna().sum()}{self.separator}')
            self.handle_missing_values()

    def handle_missing_values(self):
        na_handling = input('Choose how to handle missing values:'
                            '\n[1]: Drop rows with missing values'
                            '\n[2]: Fill with mean'
                            '\n[3]: Fill with median\n')
        try:
            if na_handling == '1':
                self.df.dropna(inplace=True)
            elif na_handling == '2':
                self.df.fillna(self.df.mean(), inplace=True)
            elif na_handling == '3':
                self.df.fillna(self.df.median(), inplace=True)
        except Exception as e:
            print(e)
            self.df.dropna(inplace=True)
            print('Dropped rows with missing values.')

    def visualize_data(self):
        # Heatmap for numeric feature correlations
        numeric_cols = self.df.select_dtypes('number').columns
        if len(numeric_cols) > 1:
            sns.heatmap(self.df[numeric_cols].corr(), annot=True)
            plt.title('Numeric Feature Correlations')
            plt.show()

        # Count plots for categorical features with less than 10 unique values
        categorical_cols = self.df.select_dtypes('object').columns
        for col in categorical_cols:
            unique_values = self.df[col].nunique()
            if 1 < unique_values < 11:
                sns.countplot(data=self.df, x=col)
                plt.title(f'{col} Frequency')
                plt.xticks(rotation=90)
                plt.show()

        # Histograms for numeric features
        for col in numeric_cols:
            sns.histplot(data=self.df, x=col, binwidth=1)
            plt.title(f'{col} Distribution')
            plt.show()

        # Pair plot for numeric features
        sns.pairplot(data=self.df)
        plt.show()


# Example usage
if __name__ == "__main__":
    dataset_path = 'your_dataset.csv'  # Replace with your actual dataset path
    eda_instance = EDA(dataset_path)
