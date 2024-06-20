import pandas as pd

from mvtools.imputers2 import ComplexImputer, SimpleImputer

# Sample DataFrame
data = {"A": [1, 2, None, 4, 5], "B": [None, 2, 3, None, 5], "C": [1, None, 3, 4, None]}
df = pd.DataFrame(data)

# Define imputation methods
simple_methods = {"A": "mean", "B": "median"}
complex_methods = {"A": "mean", "B": "median", "C": "knn"}

# Using SimpleImputer
simple_imputer = SimpleImputer(imputation_methods=simple_methods)
df_simple_imputed = simple_imputer.fit_transform(df.copy())
print("Simple Imputed DataFrame:")
print(df_simple_imputed)

# Using ComplexImputer
complex_imputer = ComplexImputer(imputation_methods=complex_methods)
df_complex_imputed = complex_imputer.fit_transform(df.copy())
print("Complex Imputed DataFrame:")
print(df_complex_imputed)
