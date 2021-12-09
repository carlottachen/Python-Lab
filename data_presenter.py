#########################################
#PART 2

cupcake_invoices = open("CupcakeInvoices.csv")
for line in cupcake_invoices:
    print(line)

cupcake_invoices.seek(0, 0)
for flavor in cupcake_invoices:
    flavor = flavor.split(',')
    print(flavor[2])

cupcake_invoices.seek(0,0)
for total_price in cupcake_invoices:
    total_price = total_price.split(',')
    count = total_price[3]
    price = total_price[4]
    calculated = float(count) * float(price)
    print(calculated)

cupcake_invoices.seek(0,0)
sum_of_all = 0
for total in cupcake_invoices:
    total = total.split(',')
    sum_of_all += float(total[3]) * float(total[4])
    
print("This is the total: " + str(sum_of_all))

cupcake_invoices.close()

##########################################
#PART 3

import matplotlib.pyplot as plt

cupcake_invoices = open("CupcakeInvoices.csv")
vanilla_total = 0
strawberry_total = 0
chocolate_total = 0
y = [] #append flavor totals at end
x = ['Vanilla', 'Strawberry', 'Chocolate']
for line in cupcake_invoices:
  line = line.split(',')
  if(line[2] == 'Vanilla'):
    vanilla_total += float(line[3]) * float(line[4])
  elif(line[2] == 'Strawberry'):
    strawberry_total += float(line[3]) * float(line[4])
  elif(line[2] == 'Chocolate'):
    chocolate_total += float(line[3]) * float(line[4])
#print(vanilla_total, strawberry_total, chocolate_total)
y.append(vanilla_total)
y.append(strawberry_total)
y.append(chocolate_total)
print(y)
plt.bar(x, y)
plt.xlabel('Flavors of Cupcakes')
plt.ylabel('Total income')
plt.title('Cupcake income by flavor')
plt.show()

cupcake_invoices.close()
