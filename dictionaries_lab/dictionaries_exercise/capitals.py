countries = input().split(", ")
capitals = input().split(", ")
my_dict = {}

for i in range(len(countries)):
    my_dict[countries[0]] = capitals[0]
    countries.pop(0)
    capitals.pop(0)

for k,v in my_dict.items():
    print(f"{k} -> {v}")
