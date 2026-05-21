price = float(input('Enter the product price: '))
discount = price - (price * 5 / 100)

print('The product price is ${:.2f} and with a 5% discount it becomes ${:.2f}'.format(price, discount))
