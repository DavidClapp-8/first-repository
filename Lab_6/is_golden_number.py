def is_golden_number(n):
#   function implementation ...
    boolean = False
    for i in range(n):
        for k in range(n):
            if i + k == n:
                if i*k % 1000 == 0:
                    boolean = True
                    print(f"K: {k}")
                    print(f"i: {i}")
                    break
    return boolean
print(is_golden_number(70))
print(is_golden_number(10))
print(is_golden_number(65))



