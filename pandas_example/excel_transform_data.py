import pandas as pd

input_data = pd.read_csv('data/input_file.csv', sep=',', dtype=object)
output_df = pd.DataFrame()

data1 = input_data.ix[:, 0:3]
data2 = input_data.ix[:, 4:]

column_names = data2.columns.values

for index, row in data1.iterrows():
    lookup_value = data2.loc[index]
    for column_name in column_names:
        new_values = pd.Series([column_name, lookup_value[column_name]])
        new_row = row.append(new_values)
        output_df = output_df.append(new_row, ignore_index=True)

output_df.to_csv('data/output_file.csv', sep=',', encoding='utf-8',
                 index=False, header=None)
