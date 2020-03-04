import pandas as pd
import numpy as np

# Numpy N-D Arrays
oddNumbers = np.arange(1, 100, 2)
print(oddNumbers)
evenNumbers = np.arange(0, 100, 2)
print(evenNumbers)
# Python Dictionary
numbers = {"oddNumbers": oddNumbers, "evenNumbers": evenNumbers}
print(numbers)

"creating a dataFrame with Dictionary"

table = pd.DataFrame(numbers)
print(table)

print("~~~~~~~~~~~")

print(table.sum())

print("~~~~~~~~~~~")

print(table.max())

print("~~~~~~~~~~~")

print(table.min())

print("~~~~~~~~~~~")

print(table.std())
