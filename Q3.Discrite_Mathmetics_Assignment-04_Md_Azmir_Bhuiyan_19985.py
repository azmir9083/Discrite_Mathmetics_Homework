m = 5
n = 3
def is_number_composite(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return True
    return False

even_check = (6 * m + 8 * n) % 2 == 0
odd_check = (10 * m * n + 7) % 2 == 1
composite_check = m > n > 0 and is_number_composite(m**2 - n**2)

print(f"6m + 8n is even: {even_check}")
print(f"10mn + 7 is odd: {odd_check}")
print(f"m^2 - n^2 is composite when m > n > 0: {composite_check}")



