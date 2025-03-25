# Pandas_08

# 1741. Find Total Time Spent by Each Employee_Solution_Q1

import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    dict={}
    for i in range (len(employees)):
        e_id = employees['emp_id'][i]
        day= employees['event_day'][i]
        in_time= employees['in_time'][i]
        out_time= employees['out_time'][i]
        if (day, e_id) in dict:
            dict[(day, e_id)] += out_time - in_time
        else:
            dict[(day, e_id)] = out_time - in_time
    result =[]

    for key, value in dict.items():
        result.append([key[0], key[1], value])

    return pd.DataFrame(result, columns=['day', 'emp_id', 'total_time'])

#Alternative1

import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['total_time']= employees['out_time']- employees['in_time']
    employees= employees.groupby(['event_day', 'emp_id'])['total_time'].sum().reset_index()
    employees.rename({'event_day':'day'}, axis=1, inplace= True)
    return employees

______________________________________________________________________________________________________________________________________

# 2356. Number of Unique Subjects Taught by Each Teacher_Solution_Q2

import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    dict={}
    for i in range(len(teacher)):
        t_id= teacher['teacher_id'][i]
        sub_id= teacher['subject_id'][i]
        if t_id not in dict:
            dict[t_id]= set()
        dict[t_id].add(sub_id)
    
    result= []
    for key, value in dict.items():
        result.append([key, len(value)])
    return pd.DataFrame(result, columns= ['teacher_id','cnt'])

#Alternative1

import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    df= teacher.groupby(['teacher_id'])['subject_id'].nunique().reset_index()
    return df.rename(columns= {'subject_id': 'cnt'})
______________________________________________________________________________________________________________________________________

# 596. Classes More Than 5 Students_Solution_Q3

import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:

    df = orders.groupby('customer_number')['order_number'].count().reset_index()
    df.sort_values(by='order_number', ascending=False, inplace=True)
    return df[['customer_number']][0:1]

______________________________________________________________________________________________________________________________________