#Write a Python program which accepts a sequence of comma-separated numbers from user and
# generate a list and a tuple with those numbers.

series = input("Enter the series: ")
print(series)
list = series.split(",")
tuple = tuple(list)
print(list)
print(tuple)