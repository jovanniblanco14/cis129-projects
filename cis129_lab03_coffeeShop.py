#Starting with constant
TAX = .06
COFFEE = 5
MUFFINS = 4

#I will start with welcome message and a prompt for the user
print('***************************************')
print('My Coffee and Muffin Shop')
print('Number of coffees bought?')
coffeesPurchased = int(input())
print('Number of muffins bought?')
muffinsPurchased = int(input())
print('***************************************')
#
#
print('***************************************')
#I had difficulty figuring out how to properly set the variables
#through trial and error I eventually figured it out
coffeeAmount = coffeesPurchased * COFFEE
muffinAmount = muffinsPurchased * MUFFINS
orderTotal = coffeeAmount + muffinAmount
afterTax = orderTotal * TAX
totalAfterTax = orderTotal + afterTax

#The main issue I had at this point was mixing up coffeeAmount and
#coffeesPurchased. In hindsight it is more obvious
print(str(coffeesPurchased) + ' Coffee at $5 each: $ ' + str(coffeeAmount))
print(str(muffinsPurchased) + ' Muffins at $4 each: $ ' + str(muffinAmount))
print('6% Tax: $' + str(afterTax))
print('---------')
print('Total: $ ' + str(totalAfterTax))
print('***************************************')

