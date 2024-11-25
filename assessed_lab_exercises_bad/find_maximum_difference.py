def find_maximum_difference(a, b):
#   #code implementation here...
    maximum = 0
    for i in a:
        for k in b:
            diff = i - k
            diff_2 = k - i
            #print(diff)
            ##=print(diff_2)
            diff_3 = max(diff, diff_2)
            print(F"DIFF_3: {diff_3}")
            if maximum <= diff_3:
                maximum = diff_3    
            print(f"MAX: {maximum}")
    
    
    return maximum
print(find_maximum_difference([1,5,600],[100,7,3,29, 39]))
print(find_maximum_difference([1,5,600],[100,7,3,602, 39]))