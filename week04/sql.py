import pandas as pd
import numpy as np

# 1. SELECT * FROM data;
data = {'id':[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],
        'age':[20,23,35,32,28,33,26,40,24,37,35,27,30,21,38]}

df = pd.DataFrame(data)
print(df)

# 2. SELECT * FROM data LIMIT 10;
print(df[0:10])

# 3. SELECT id FROM data;  //id 是 data 表的特定一列
df = pd.DataFrame(data, columns=['id'])
print(df['id'])

# 4. SELECT COUNT(id) FROM data;
df = pd.DataFrame(data, columns=['id'])
print(df.count())

# 5. SELECT * FROM data WHERE id<1000 AND age>30;
print(df.loc[(df['id']<1000) & (df['age']>30)])

# 6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
table1 = {'id':[1,2,3,4,5],
        'order_id':[20,23,35,32,23]}

t1 = pd.DataFrame(table1)
print(t1.drop_duplicates(subset=['order_id']))

t1.groupby('id').order_id.nunique()

# 7. SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;
table1 = pd.DataFrame({
    'id':[1,2,3,4,5],
    'order_id':[20,23,35,32,23]
    })

table2 = pd.DataFrame({
    'id':[1,2,3,6,7],
    'order_id':[20,23,35,20,25]
    })

print(pd.merge(table1, table2, on='id'))

# 8. SELECT * FROM table1 UNION SELECT * FROM table2;
print(pd.concat([table1, table2]).drop_duplicates(subset=['id','order_id']))

# 9. DELETE FROM table1 WHERE id=10;
table1 = pd.DataFrame({
    'id':[1,2,3,4,5,10],
    'order_id':[20,23,35,32,23,28]
    })

print(table1)
# table1 [  table1['id'] == 10 ]
table1.drop(table1[table1['id'] == 10].index, inplace=True)
# index = table1[table1['id'] == 10].index
# table1.drop(index, inplace=True)
print(table1)

# 10. ALTER TABLE table1 DROP COLUMN column_name;
table1.drop( 'column_name' ,axis = 1)
