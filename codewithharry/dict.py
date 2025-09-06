cities = {"delhi", "mumbai", "pune"}
cities2 = {"akola", "amritsar", "mumbai"}
cities.update(cities2)
print(cities)
cities.pop()
print(cities)


dic = {
    "name" : 'sayema',
    "age" : 45,
    "degree" : "B.Tech"
}
print(dic["name"])
print(dic.popitem())
print(dic.keys())
print(dic.values())

tup = ("hello","sayema", "qureshi", [1, 2, 3])
tup[3][2] = 5
print(tup)
print(tup[0])
print(type(tup))
a, b, c, d = tup
print(a,b,c)

makrs = {}
print(type(makrs))


tup2 = "hello", "sayema", "period"
tup3 = 1, 2, 3,4,1
print(max(tup3))
print(tup3.sort())
print(len(tup2))
print(tup2 + tup3)
print(tup2[2])
print( 1 in tup3)
list1 = list(tup2)
list1[2] = "qureshi"
tup4 = tuple(list1)
print(tup4)
print(list1[0])
string1 = str(tup3)
print(type(string1))
print(tup2.index("sayema"))