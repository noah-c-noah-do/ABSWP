tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

# column1_len = max(len(*tableData[0]))
column_lengths = []
for item in tableData:
    lens = []
    for x in item:
        lens.append(len(x))
    column_lengths.append(max(lens))

print(column_lengths)


rows = list(map(list, zip(*tableData)))
final_rows = []
for x in range(0, len(tableData)):
    # print(rows[x])
    new_columns = []
    for y in range(0, len(tableData[x])):
        new_columns.append(tableData[x][y].rjust(column_lengths[x]))
    final_rows.append(new_columns)


test = list(map(list, zip(*final_rows)))
for item in test:
    print(" ".join(item))

# for y in rows[x]:
#     print(rows[x].rjust(column_lengths[i]))

# print(" ".join(rows[x]).center(sum(column_lengths)))


# for item in rows:
#     print(item)
#     for x in range(0, len(item)):
#         print(item[x].center(column_lengths[x]))
# print(item[0].center(column_lengths[0]))
# for x in item:
#     print(x.center(column_lengths[0]))
