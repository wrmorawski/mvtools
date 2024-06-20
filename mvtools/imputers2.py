import pandas as pd
from sklearn.impute import KNNImputer


class SimpleImputer:
    def __init__(self, imputation_methods):
        """
        Initialize the SimpleImputer with a dictionary of imputation methods.

        :param imputation_methods: Dictionary with column names as keys and imputation methods as values.
        """
        self.imputation_methods = imputation_methods

    def fit_transform(self, df):
        """
        Fit and transform the DataFrame by imputing missing values according to the provided methods.

        :param df: DataFrame to impute.
        :return: DataFrame with imputed values.
        """
        for column, method in self.imputation_methods.items():
            if method == "mean":
                df[column].fillna(df[column].mean(), inplace=True)
            elif method == "median":
                df[column].fillna(df[column].median(), inplace=True)
            elif method == "mode":
                df[column].fillna(df[column].mode()[0], inplace=True)
            # Add other simple methods as needed
        return df


class ComplexImputer(SimpleImputer):
    def __init__(self, imputation_methods):
        """
        Initialize the ComplexImputer with a dictionary of imputation methods, including more complex methods.

        :param imputation_methods: Dictionary with column names as keys and imputation methods as values.
        """
        super().__init__(imputation_methods)

    def fit_transform(self, df):
        """
        Fit and transform the DataFrame by imputing missing values according to the provided methods.

        :param df: DataFrame to impute.
        :return: DataFrame with imputed values.
        """
        df = super().fit_transform(df)  # Apply simple imputation methods first

        for column, method in self.imputation_methods.items():
            if method == "knn":
                df = self.knn_impute(df, column)
            # Add other complex methods as needed

        return df

    def knn_impute(self, df, column):
        """
        Impute missing values in a column using KNN imputation.

        :param df: DataFrame to impute.
        :param column: Column to apply KNN imputation.
        :return: DataFrame with imputed values.
        """
        imputer = KNNImputer()
        df[column] = imputer.fit_transform(df[[column]])
        return df
