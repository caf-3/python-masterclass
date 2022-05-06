friends = [("Rachel",19),
           ("Monica",18),
           ("Phoebe",17),
           ("Joey",16),
           ("Chandler",21),
           ("Ross",20)]

can_drink = lambda friend: friend[1] >= 18

drinking_buddies = list(filter(can_drink, friends))

for i in drinking_buddies:
    print(i)