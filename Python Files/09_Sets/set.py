a={10,20,30,50,70}
print(a)

a.add(89)
print("after adding" ,a)

a.update([94, 100])
print("After updating")
print(a)

a.remove(100)
print("after removing ",a)

a.discard(10)
print("after discarding: ",a)

a.clear()

#union
set1={34,56,78,92,10}
set2={56,78,90,10,101}

print(set1.union(set2))



