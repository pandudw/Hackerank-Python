def sum(x, y):
    return x + y 

count = 0
kumpulan = [] 
while count < 5:
    one = int(input("masukan nilai ke-1:"))
    two = int(input("masukan nilai ke-2:"))

    result = sum(one, two)
    
    print(kumpulan)
    print("=====")
    kumpulan.append(result)
    #print(kumpulan)
    #print(result)

    count += 1

print(kumpulan)
    # if one != 0:
    #     break

    # stop = input("mau stop ga? (yes or no)")
    # if stop == "yes":
    #     print("udahan ya")
    #     break



