
l1=[1,2,1,2,3]
s1 = set(l1)

#ADD & UPDATE
s1.add(4)
s2 = {2,3,4}
s1.update(s2)
# print(s1)

## REMOVE & DISCARD
s1.remove(4) # get error if value doesnt exist
s1.discard(5)

## INTERCECTION
s3 = {4,5,6}
s4 = {5,6,7}
# print(s1.intersection(s3))
# print(s1.intersection(s3, s4))

## DIFERENCE (value in that is _ not in _)
print(s1.difference(s2))
print(s2.difference(s1))
print(s1.difference(s3,s4)) #find the value in s1 that is not in s3 or s4
print(s4.difference(s3,s1))

## SYMETRIC_DIFERENCE (value in that is _ not in _)
print(s1.symmetric_difference(s2))
print(s2.symmetric_difference(s1))
print(s1.symmetric_difference(s3,s4)) #find the value in s1 that is not in s3 or s4
print(s4.symmetric_difference(s3,s1))

## UNION
s5 = s1.union(s2).union(s3)
# print(s5)
