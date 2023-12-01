
# HOW TO READ FROM FILES

def readlistfromfile(file_name):

    with open(file_name, "r") as file_list:
        file_lines = file_list.readlines()

    returnlist = []

    for file_line in file_lines:
        returnlist.append(file_line[0:-1])
        # first number in square bracket shows where it starts from
        # last number in square bracket shows how much characters to get rid of

    return returnlist


countries = readlistfromfile("countries.txt")
capitals = readlistfromfile("capitals.txt")

countries_capitals = dict(zip(countries, capitals))
# zip creates columns, separates the dictionary

value = input("Enter a country name to get it's captial:")
value = value.capitalize()
print("Captial of", value, "is", countries_capitals[value])


# with open("countries.txt", "r") as country_list:
#     country_lines = country_list.readlines()

# countries = []

# for country in country_lines:
#     countries.append(country[0:-1])

# #for country in countries:
# #    print(country)



# with open("capitals.txt", "r") as capital_list:
#     capital_lines = capital_list.readlines()

# capitals = []

# for capital in capital_lines:
#     capitals.append(capital[0:-1])

# #for capital in capitals:
# #    print(capital)
