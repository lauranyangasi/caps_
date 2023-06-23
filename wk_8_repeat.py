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

'''Step 1: Create a DataFrame from the list of dictionaries below:

[{'product_id':23, 'name':'computer', 'wholesale_price': 500, 'retail_price':1000, 'sales':100},
{'product_id':96, 'name':'Python Workout', 'wholesale_price': 35,'retail_price':75, 'sales':1000},
{'product_id':97, 'name':'Pandas Workout', 'wholesale_price': 35, 'retail_price':75, 'sales':500},
{'product_id':15, 'name':'banana', 'wholesale_price': 0.5,'retail_price':1, 'sales':200},
{'product_id':87, 'name':'sandwich', 'wholesale_price': 3,'retail_price':5, 'sales':300}]'''

import pandas as pd
data = [{'product_id':23, 'name':'computer', 'wholesale_price': 500, 'retail_price':1000, 'sales':100},
{'product_id':96, 'name':'Python Workout', 'wholesale_price': 35,'retail_price':75, 'sales':1000},
{'product_id':97, 'name':'Pandas Workout', 'wholesale_price': 35, 'retail_price':75, 'sales':500},
{'product_id':15, 'name':'banana', 'wholesale_price': 0.5,'retail_price':1, 'sales':200},
{'product_id':87, 'name':'sandwich', 'wholesale_price': 3,'retail_price':5, 'sales':300}]
df = pd.DataFrame(data)
print(df)

# Calculate the Total Profit for each product using the formula
#net_revenue_per_product = (retail_price - wholesale price) * sales

df["net_revenue_per_product"] = (df["retail_price"] - df["wholesale_price"]) * df["sales"]

#How much total net revenue you received from all of these sales?

total_net_revenue = df["net_revenue_per_product"].sum()

print(f"The total net revenue is: {total_net_revenue:,}")

#What product is product retail price more than twice the wholesale price?

compare = df["retail_price"] > df["wholesale_price"]*2


print(df[compare][["name", "retail_price", "wholesale_price"]])


#How much did the store make from food vs. computers vs. books?

df["category"] = ""

for row, column in df.iterrows():
    if "computer" in column["name"]:
        df.loc[row, "category"] = "computers"
    elif "Workout" in column["name"]:
        df.loc[row, "category"] = "books"
    else:
        df.loc[row, "category"] = "food"

category = df.groupby("category")["net_revenue_per_product"].sum()
print(category)


#Because your store is doing so well, you’re able to negotiate a 30% discount on the
# wholesale price of goods. Calculate the new net revenue

df["discounted_wholesale_price"] = df["wholesale_price"] * 0.7
df["new_net_revenue"] = (df["retail_price"] - df["discounted_wholesale_price"]) * df["sales"]
print(df)

'''In the peer programming project, we created a data frame representing our store’s products and sales. In
this exercise, we’re going to extend that data frame, quite literally.


The backstory for this exercise is as follows: Our local government is thinking about imposing a
sales tax, and is thinking about 15, 20, and 25 percent rates. Show how much less you would net
with each of these tax amounts by adding columns to the data frame for current income, as well.'''

df["tax_15%"] = df["new_net_revenue"] * 0.15
df["tax_20%"] = df["new_net_revenue"] * 0.2
df["tax_25%"] = df["new_net_revenue"] * 0.25

df["income_after_15%_tax"] = df["new_net_revenue"] - df["tax_15%"]
df["income_after_20%_tax"] = df["new_net_revenue"] - df["tax_20%"]
df["income_after_25%_tax"] = df["new_net_revenue"] - df["tax_25%"]

print(df[["name", "income_after_15%_tax", "income_after_20%_tax", "income_after_25%_tax"]])

