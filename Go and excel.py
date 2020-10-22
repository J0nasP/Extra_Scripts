import pandas as pd

# Opening the sheets

customers = pd.read_excel("Customers.xlsx")
calls = pd.read_excel("Calls.xlsx")


# joining the sheets where the chosen value is present in both sheets
def InnerJoin():
    inner_join_df = customers.merge(calls, how="inner", on='Name')
    inner_join_df.to_excel("InnerJoin.xlsx", index = False)


#Taking ALL values from the left table and gets pair up with the right table by the chosen value 
def LeftJoin():
    left_join_df = customers.merge(calls, how = 'left', on = 'Name')
    left_join_df.to_excel ('LeftJoin.xlsx', index = False)
# All the names  in the left table is matched with their "equal" in the right table


#Taking ALL values from the right table and gets pair up with the left table by the chosen value
def RightJoin():
    right_join_df = customers.merge(calls, how = 'right', on = 'Name')
    right_join_df.to_excel('RightJoin.xlsx', index = False)
# All the names  in the right table is matched with their "equal" in the left table


# FULL JOIN
def OuterJoin():
    outer_join_df = customers.merge(calls, how = 'outer', on = 'Name')
    outer_join_df.to_excel('OuterJoin.xlsx', index = False)
