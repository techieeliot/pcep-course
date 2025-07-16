import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 30, 22, 35],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

df = pd.DataFrame(data)


list_of_rows = df.values.tolist()
list_of_columns = df.columns.tolist()

print("List of Rows:", list_of_rows)
print("List of Columns:", list_of_columns)
print("DataFrame:\n", df)