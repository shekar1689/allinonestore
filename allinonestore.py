no_of_items = int(input())
cart = []
for i in range(no_of_items):
    data = {}
    data["item"] = input()
    data["itemCategory"] = input()
    data["quantity"] = int(input())
    data["price"] = int(input())
    
#print(data)
    cart.append(data)
#print(cart)

#Defining Taxes
taxes = []
for i in cart:
    #print(i.get("itemCategory"))
    if i.get("itemCategory") == "Medicine" or i.get("itemCategory") == "Food" :
        tax = 5
    #print(tax)
    if i.get("itemCategory") == "Clothes":
        if i.get("price") <= 1000 :
            tax = 10
        else:
            tax = 12
    #print(tax)
    if i.get("itemCategory") == "Groceries" or i.get("itemCategory") == "Book" :
        tax = 0
        #print(tax)
    if i.get("itemCategory") == "Music":
        tax = 3
        #print(tax)
    if i.get("itemCategory") == "Imported":
        tax = 18
        #print(tax)
    taxes.append(tax)
#print(taxes)
#print("taxes: " +  str(taxes))

quantity = []
for i in cart:
    No = i.get("quantity")
    quantity.append(No)
#print("quantity: " + str(quantity))

prices = []
for i in cart:
    p = i.get("price")
    prices.append(p)
#print("prices: "+ str(prices))
    
finalprices = []
for i in range(len(quantity)):
    #print(i)
    #print(quantity[i])
    t = quantity[i]*prices[i]
    finalprices.append(int(t))
#print("finalprices= " + str(finalprices))

taxamounts = []
for i in range(len(prices)):
    a = int(finalprices[i]*(taxes[i]/100))
    taxamounts.append(a)
#print("taxamount=" + str(taxamounts))

total = sum(finalprices) + sum(taxamounts)
if total>2000:
    total = int(total * 0.95)
else:
    total = total
#print(total)

from datetime import datetime

purchase_time = datetime.now().strftime('%d-%b-%Y\nTime: %H:%M')
print(purchase_time)
print()

result = []
for i in range(len(cart)):
    result .append(cart[i].get("item") + " " + str(finalprices[i])+ " TaxAmount "+ str(taxamounts[i]) + " " + str(taxes[i])+"%")

result = sorted(result)
for i in result:
    print(i)

print("\n" + "Total bill: " + str(total))
print()
print("** THANK YOU **")
print("** ALL IN ONE STORE **")
