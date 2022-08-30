# url = f'https://www.fruityvice.com/api/fruit/all' 
# print(f"""{'-'*93}
# {'Name':<20}{'Genus':<20}{'family':<16}{'calories':<10}{'carbohydrates':<15}{'protein':<9}{'fat':<20}
# {'-'*93}""")
# for response in requests.get(url).json():
#     tableFruit = f"{response['name']:<20}"
#     tableFruit += f"{response['genus']:<20}"
#     tableFruit += f"{response['family']:<16}"
#     tableFruit += f"{response['nutritions']['calories']:<10}"
#     tableFruit += f"{response['nutritions']['carbohydrates']:<15}"
#     tableFruit += f"{response['nutritions']['protein']:<9}"
#     tableFruit += f"{response['nutritions']['fat']:<20}"
#     print(tableFruit)