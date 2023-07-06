from my_packages import arithmetic
arithmetic.add(2,3)
arithmetic.sub(2,3)
arithmetic.prod(2,3)
arithmetic.div(2,3)

from my_packages import prime
prime.is_prime(1)
prime.is_prime(2)
prime.is_prime(3)
prime.is_prime(4)

from my_packages import string
string.string.lower()

from my_packages.tuple import *
s=read_data_tuple()
print(s)
print("Max:",max_marks(s))
print("Min:",min_marks(s))
print("Tot:",sum_marks(s))

from my_packages.set import *
s=read_data_set()
print(s)
print("Max:",max_marks(s))
print("Min:",min_marks(s))
print("Tot:",sum_marks(s))

from my_packages.list import *
L=Read_list_values()
print("Max: ",max(L))
print("Min:",min(L))
print("Sum:",sum(L))

from my_packages.strings import *
res0=palindrome(N)
if res0==temp0:
    print("palindrome number")
else:
    print("Not palindrome number")

from my_packages.strings import *
res1=perfect_number(N1)
if res1==temp1:
    print("perfect number ")
else:
    print("Not perfect number ")

from my_packages.strings import *
res2=armstrong(N2)
if res2==(2*N2):
    print("ArmStrong")
else:
    print("Not a ArmStrong")

