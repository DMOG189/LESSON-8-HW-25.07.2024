# LESSON 8 HOMEWORK EX 2


# START

import py_return_with_func as rwf

# Exercise a: Call avg_my with 90 and 99, store in avg1, then print avg1
avg1 = rwf.avg_my(90, 99)
print(f"The average of 90 and 99 is: {avg1}")

# Exercise b: Call headline_my with "python has concurred the world", store in head1, then print head1 twice
head1 = rwf.headline_my("python has conquered the world")
print(head1)
print(head1)

# Exercise c: Call list_concat with three lists, store in con_res, then print con_res and its length
con_res = rwf.list_concat([9, 8, 7], [6, 5, 4, 3], [2, 1])
print(f"Concatenated list: {con_res}")
print(f"Length of concatenated list: {len(con_res)}")

# Exercise d: Print help for each function
help(rwf.avg_my)
help(rwf.headline_my)
help(rwf.list_concat)

# END