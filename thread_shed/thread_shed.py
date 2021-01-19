with open("thread_shed_input.txt") as input:
    daily_sales = input.read()

# cleaning data - removal of ;,; between values
daily_sales_replaced = daily_sales.replace(";,;", "-")



# cleaning data - split at , which seperates each transaction.
daily_transactions = daily_sales_replaced.split(',')

daily_transactions_split = []
for transaction in daily_transactions:
  daily_transactions_split.append(transaction.split('-'))



# cleaning data - removing white space
transactions_clean = []
for transactions in daily_transactions_split:
  transaction_clean = []
  for transaction in transactions:
    transaction_clean.append(transaction.replace("\n", "").strip(" "))
  transactions_clean.append(transaction_clean)



# seperating data into categories
customers = []
sales = []
thread_sold = []

for transaction in transactions_clean:
  customers.append(transaction[0])
  sales.append(transaction[1])
  thread_sold.append(transaction[2])



# how much money is made per day
total_sales = 0
for sale in sales:
  total_sales += float(sale.replace("$", ""))

print(total_sales)


# how much of each color is sold per day
thread_sold_split = []
for thread in thread_sold:
  for color in thread.split("&"):
    thread_sold_split.append(color)

def color_count(color):
  count = 0
  for thread in thread_sold_split:
    if thread == color:
      count += 1 
  return count

colors = ['red', 'yellow', 'green', 'white', 'black', 'blue', 'purple']

for color in colors:
  print("Thread Shed sold {0} threads of {1} thread today"
  .format(color_count(color), color))
