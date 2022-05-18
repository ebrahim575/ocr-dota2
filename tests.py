mymap = {
    'hi' : 'hello',
    1 : 2
}

mymap2 = {
    3: 4,
    'hi' : 'hello'
}
set1 = set(mymap.items())
set2 = set(mymap2.items())
a = set1 ^ set2
print(a)
print(set1 ^ set2)