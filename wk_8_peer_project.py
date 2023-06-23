'''Step 1: Create a DataFrame from the list of dictionaries below:

[{'product_id':23, 'name':'computer', 'wholesale_price': 500, 'retail_price':1000, 'sales':100},
{'product_id':96, 'name':'Python Workout', 'wholesale_price': 35,'retail_price':75, 'sales':1000},
{'product_id':97, 'name':'Pandas Workout', 'wholesale_price': 35, 'retail_price':75, 'sales':500},
{'product_id':15, 'name':'banana', 'wholesale_price': 0.5,'retail_price':1, 'sales':200},
{'product_id':87, 'name':'sandwich', 'wholesale_price': 3,'retail_price':5, 'sales':300}]


Step 2:  Calculate the Total Profit for each product using the formula

```

net_revenue_per_product = (retail_price - wholesale price) * sales
```

Step 3: Determine the following

- How much total net revenue you received from all of these sales?

- What product is product retail price more than twice the wholesale price?

- How much did the store make from food vs. computers vs. books?

- Because your store is doing so well, you’re able to negotiate a 30% discount on the wholesale price of goods. Calculate the new net revenue'''


import numpy as np
import pandas as pd

sales_list = [{'product_id':23, 'name':'computer', 'wholesale_price': 500, 'retail_price':1000, 'sales':100},
{'product_id':96, 'name':'Python Workout', 'wholesale_price': 35,'retail_price':75, 'sales':1000},
{'product_id':97, 'name':'Pandas Workout', 'wholesale_price': 35, 'retail_price':75, 'sales':500},
{'product_id':15, 'name':'banana', 'wholesale_price': 0.5,'retail_price':1, 'sales':200},
{'product_id':87, 'name':'sandwich', 'wholesale_price': 3,'retail_price':5, 'sales':300}]

df = pd.DataFrame(sales_list)

print(df)

#Calculate the Total Profit for each product using the formula

#net_revenue_per_product = (retail_price - wholesale price) * sales

df["net_revenue_per_product"] = (df["retail_price"] - df["wholesale_price"]) * df["sales"]

print(df[["name", "net_revenue_per_product"]])

#How much total net revenue you received from all of these sales?

total_net_revenue = sum(df["net_revenue_per_product"])
print(f"The total net revenue is: {total_net_revenue}")

#What product is product retail price more than twice the wholesale price?

product = df["retail_price"] > (df["wholesale_price"] * 2)
print(df[product][["name", "retail_price", "wholesale_price"]])

#How much did the store make from food vs. computers vs. books?
df["category"] = ""
for row, column in df.iterrows():
    if "computer" in column["name"]:
        df.loc[row, "category"] = "computers"
    elif "Workout" in column["name"]:
        df.loc[row, "category"] = "books"
    else:
        df.loc[row, "category"] = "food"

category_sum = df.groupby("category")["net_revenue_per_product"].sum()
print(category_sum)

'''Because your store is doing so well, you’re able to negotiate a 30% discount on 
the wholesale price of goods. Calculate the new net revenue'''

df["new_net_revenue_per_product"] = (df.retail_price - (df.wholesale_price - (0.3 * df.wholesale_price))) * df.sales

print(df[["name", "new_net_revenue_per_product"]])