def CharRange(start, end):
    L = ''
    s = ord(start)
    e = ord(end)
    if s <= e:
        e = e + 1
        for i in range(s,e):
            L = L + chr(i)
    else:
        e = e - 1
        for i in range(s,e,-1):
            L = L + chr(i)
    return iter(L)

# For judging purpose
instantiate_generator1 = input()
exec(instantiate_generator1)
instantiate_generator2 = input()
exec(instantiate_generator2)
for i in range(4):
    test_code = input()
    exec(test_code)