# classify a given amount of money into smaller monetary units

amount = eval(input('Enter amount of money: ')) #get amount

remainingAmount = int(amount * 100) # money in cents

dollars = remainingAmount // 100 # money in dollars
remainingAmount = remainingAmount % 100 # how many cants you have left after dollars

quarters = remainingAmount // 25
remainingAmount = remainingAmount % 25

dimes = remainingAmount // 10
remainingAmount = remainingAmount % 10

nickels = remainingAmount // 5
remainingAmount = remainingAmount % 5

pennies = remainingAmount #just for pretty

print('You have ', amount, 'dollars. \nThis means you have '
      , dollars, ' dollars, ', 
      quarters, ' quarters, ', 
      dimes, ' dimes,', 
      nickels, ' nickels and ', 
      pennies, ' pennies.')

print(f"You have {amount} dollars")

