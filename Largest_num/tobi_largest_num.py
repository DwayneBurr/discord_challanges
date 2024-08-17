def longes(l:list) -> list:
    list1 = sorted([i for i in l])[::-1]
    packets = []
    for i in range(9,-1,-1):
        for j in list1:
            if str(i) in str(j)[0]:
                packets.append(j)
    return "".join([str(i) for i in packets])        
       
print(longes([30,4,9,8,37,0,0]))
