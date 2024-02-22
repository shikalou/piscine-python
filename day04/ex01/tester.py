from in_out import outer, outer2
from in_out import square
from in_out import pow


my_counter = outer(3, square)
print(my_counter())
print(my_counter())
print(my_counter())
print("---")
another_counter = outer(1.5, pow)
print(another_counter())
print(another_counter())
print(another_counter())


counter = outer2(3, square)
for c, _ in zip(counter, range(3)):
    print(c)
