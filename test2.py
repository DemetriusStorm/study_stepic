from matplotlib import pyplot as plt

# Add your code below:
import random
numbers_a = range(1,13)
numbers_b = random.sample(range(1000), 12)
plt.plot(numbers_a, numbers_b)
print(plt.show())
#=============================================================
# Import Decimal below:
from decimal import Decimal

# Fix the floating point math below:
three_decimal_points = Decimal('0.2') + Decimal('0.69')
print(three_decimal_points)

four_decimal_points =Decimal('0.53') * Decimal('0.65')
print(four_decimal_points)
#=============================================================
