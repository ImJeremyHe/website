import torndb


db = torndb.Connection(host='127.0.0.1:3306', database='miaomushan', user='root', password='123')
series = 't_1, t_2, t_3, t_4, t_5, t_6, t_7, t_8, t_9, t_10, t_11, t_12, t_13, t_14, t_15, t_16, t_17, t_18, t_19, t_20, t_21, t_22, t_23, t_24, t_25, t_26, t_27, t_28, t_29, t_30, t_32, t_34, t_36, t_38, t_40, t_42, t_45, t_48, t_50, t_55, t_60'
with open('all', 'r') as f:
    content = f.readlines()[1:]
for line in content:
    line = line.strip()
    data = line.split()
    data[0] = '"%s"' % data[0]
    data = ','.join(data)
    sql = 'INSERT INTO earthquake (name, pga, %s, type, vs30) VALUES (%s)' % (series, data)
    # print sql
    db.execute(sql)