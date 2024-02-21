"""
    Compare the times of excuting code examples
"""

import time



# ------------ Dinamic Storage -------------
start = time.time()

my_list = []
for num in range(30_000_000):
    my_list.append(num)

end = time.time()
print(f"Time taken to execute the code [Dinamic Storage]: {end - start} seconds")



# ----------- Pre-allocation ---------------
start = time.time()

my_list2 = [0]*30_000_000

for num in range(30_000_000):
    my_list2[num] = num


end = time.time()
print(f"Time taken to execute the code [Pre-allocated]: {end - start} seconds\n")


# ---------- Pure python way ------------------
start = time.time()

my_list3 = list(range(30_000_000))  

end = time.time()
print(f"Time taken to execute the code [Python list]: {end - start} seconds\n")
