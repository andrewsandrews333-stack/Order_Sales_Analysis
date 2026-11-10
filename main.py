import json
with open("sales.json","r") as file:
    sales=json.load(file)


def analys_sales(sales):
    unique_cus=[]

    order_details={}
    status_revenue={} 
    category_revenue={}
    product_quantity={}  

    completed_cus_spending={}

    highest_spending=0
    highest_spending_cus=[]

    highest_revenue=0
    highest_revenue_category=[]

    most_sold_quantity=0
    most_sold_product=[]

    highest_order_id=[]
    highest_order_amount=0
    highest_order_cus=[]

    cus_category={
        "VIP":[],
        "Regular":[],
        "Normal":[]
    }

    total_orders=len(sales)
    
    for i in sales:
        order_id=i["id"]
        cus=i["customer"]
        category=i["category"]
        product=i["product"]
        amount=i["amount"]
        quantity=i["quantity"]
        status=i["status"]

        #findind unique cus...
        if cus not in unique_cus:
            unique_cus.append(cus)

        #finding order details
        if status in order_details:
            order_details[status]+=1
        else:
            order_details[status]=1

        #findinng status revenue
        if status in status_revenue:
            status_revenue[status]+=amount
        else:
            status_revenue[status]=amount

        if status=="completed":
            #finding category revenue
            if category in category_revenue:
                category_revenue[category]+=amount
            else:
                category_revenue[category]=amount

            #finding product quantity
            if product in product_quantity:
                product_quantity[product]+=quantity
            else:
                product_quantity[product]=quantity

            #finding cus spending amout in completed status...
            if cus in completed_cus_spending:
                completed_cus_spending[cus]+=amount
            else:
                completed_cus_spending[cus]=amount

            #finding highest order in completed status..
            if amount>highest_order_amount:
                highest_order_amount=amount
                highest_order_id=[order_id]
                highest_order_cus=[cus]
            elif amount==highest_order_amount:
                highest_order_id.append(order_id)
                highest_order_cus.append(cus)


    #finding highest amount spending cus in completed status
    for cus,amount in completed_cus_spending.items():
        if amount>highest_spending:
            highest_spending=amount
            highest_spending_cus=[cus]
        elif amount==highest_spending:
            highest_spending_cus.append(cus)

    #finding highest revenue category in completed status..
    for category,amount in category_revenue.items():
        if amount>highest_revenue:
            highest_revenue=amount
            highest_revenue_category=[category] 
        elif amount==highest_revenue:
            highest_revenue_category.append(category)

    #finding most sold product in completed status..
    for product,quantity in product_quantity.items():
        if quantity>most_sold_quantity:
            most_sold_quantity=quantity
            most_sold_product=[product]
        elif quantity==most_sold_quantity:
            most_sold_product.append(product)

    #finding customer category...
    for cus,amount in completed_cus_spending.items():
        if amount>=10000:
            cus_category["VIP"].append(cus)

        elif amount>=3000:
            cus_category["Regular"].append(cus)

        else:
            cus_category["Normal"].append(cus)

    return(unique_cus,
           total_orders,
           order_details,
           status_revenue,
           category_revenue,
           product_quantity,
           completed_cus_spending,
           highest_spending_cus,
           highest_spending,
           highest_revenue_category,
           highest_revenue,
           most_sold_product,
           most_sold_quantity,
           highest_order_id,
           highest_order_cus,
           highest_order_amount,
           cus_category)

result=analys_sales(sales)

print("Unique Customers:")
for index,i in enumerate(result[0],start=1):
    print(index,":",i)
print(" ")
print("Toal Orders:",result[1])
print(" ")
print("Order Details:")
for index,(status,count) in enumerate(result[2].items(),start=1):
    print(index,":",status,"->",count)
print(" ")
print("Status Revenue:")
for index,(status,amount) in enumerate(result[3].items(),start=1):
    print(index,":",status,"->",amount)
print(" ")
print("       COMPLETED STATUS DETAILS      ")
print("....x....x....x....x....x....x....x....x....x....")
print(" ")
print("Category Revenue:")
for index,(category,amount) in enumerate(result[4].items(),start=1):
    print(index,":",category,"->",amount)
print(" ")
print("Product Quantity:")
for index,(product,quantity) in enumerate(result[5].items(),start=1):
    print(index,":",product,"->",quantity)
print(" ")
print("Customers Spending:")
for index,(cus,amount) in enumerate(result[6].items(),start=1):
    print(index,":",cus,"->",amount)
print(" ")
print("Highest Spending Customer:",result[7])
print("Highest Spending Amount:",result[8])
print(" ")
print("Highest Revenue Category:",result[9])
print("highest Revnue Amount:",result[10])
print(" ")
print("Most Sold Product:",result[11])
print("Most Sold Product Quantity:",result[12])
print("")
print("....x....x....x....x....x....x....x....x....x....")
print(" ")
print("Highset Order Details:")
print("ID",":",result[13])
print("NAME",":",result[14])
print("AMOUNT",":",result[15])
print(" ")
print("Customer Category:")
for category,cus in result[16].items():
    print(category,":",cus)
