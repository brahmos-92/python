# Write a Python program to display the examination schedule (extract the date from exam_st_date).
# exam_st_date = (11, 12, 2014)
# Sample Output: The examination will start from : 11 / 12 / 2014

exam_st_date = (11, 12, 2014)
print(f"The examination will start from %d/%d/%d"%exam_st_date)

# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn

n = int(input("Enter a number: "))
comp_val= n + (n*n) + (n*n*n)
print(f"the value is: {comp_val}")

# 
print(abs.__doc__)