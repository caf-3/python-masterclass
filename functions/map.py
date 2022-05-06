store = [('T-shirt', 60.00), ('Pats', 120.00), ('Socks', 10.00), ('Cap', 15.00), ('Jewelry', 200.00)]

to_mzn = lambda item: (item[0], '{:,.2f} MZN'.format(item[1] * 63.83))

converted_tore = list(map(to_mzn, store))

for i in converted_tore:
    print(i)