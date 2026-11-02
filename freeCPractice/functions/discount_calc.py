def apply_discount(price, discount):

    if not isinstance(price, (int, float)):
        return 'The price should be a number'

    if not isinstance(discount, (int, float)):
        return 'The discount should be a number'

    if price <= 0:
        return 'The price should be greater than 0'

    if discount < 0 or discount > 100:
        return 'The discount should be between 0 and 100'

    discount = price * discount / 100
    final_Price = price - discount

    return final_Price

a = apply_discount(100, 20) # returns 80.0
b = apply_discount(74.5, 20.0) # returns 59.6

print(a)
print(b)