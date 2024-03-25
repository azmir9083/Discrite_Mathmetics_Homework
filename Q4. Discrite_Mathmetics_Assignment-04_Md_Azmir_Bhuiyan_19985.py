def is_number_composite(number):
    if number <= 1:
        return False
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return True
    return False

def check_composite_in_expression(k_value):
    expression_result = k_value**2 + 2*k_value + 1
    return is_number_composite(expression_result)

for k_value in range(5, 30):
    is_composite = check_composite_in_expression(k_value)
    print(f"k = {k_value}: Expression is composite? {is_composite}")


