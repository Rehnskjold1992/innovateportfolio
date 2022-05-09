# dict_of_films = {
#     "Sicario": 2008,
#     "Arrival": 2011,
#     "Dune": 2020,
#     "Enemy": 2005,
#     "Blade Runner 2049": 2018
# }

# list_of_films = [
#     "Sicario",
#     "Arrival",
#     "Dune",
#     "Enemy",
#     "Blade Runner 2049"
# ]

# print(list_of_films[0])

# will_todo_dict = {
#     "tired": True,
#     "hungry": False,
#     "exercise_time_day": 20,
#     "homework": "Look at PEP 0484",
#     "chores": "clean kitchen",
#     6: 3.14152,

# }

# print(will_todo_dict)

# will_todo_dict["chores"] = "None! All finished"

# will_todo_dict["exercise_time_day"] = 110

# print(will_todo_dict)

# dict_of_dicts = {
#     "dict1": {
#         "key1": "value1",
#         "key2": "value2"
#     },
#     "dict2": {
#         "key3": "value3",
#         "key4": "value4"
#     }
# }

# print(dict_of_dicts["dict1"]["key1"])

# dict_of_list = {
#     "list1": [1, 2, 3, 4, 5],
#     "list2": [6, 7, 8, 9, 10]
# }

# print(dict_of_list["list2"][-2])

# my_cat_dict = {
#     "name" : "Greg",
#     "colour" : "Grey",
#     "breed" : "Ragdoll",
#     "temperament" : "playful",
#     "sleeping" : True,
#     "sleeping_spot" : "sofa"
# }
# print(my_cat_dict)

# my_cat_dict["temperament"] = "hangry"
# my_cat_dict["sleeping"] = False


# print(my_cat_dict)

country_dict = {
    "United Kingdom": "London",
    "France": "Paris",
    "Germany": "Berlin",
    "Spain": "Madrid",
    "Italy": "Rome"
}
country_dict.setdefault("Ireland", "Dublin")
country_dict.setdefault("Ukraine", "Kyiv")
for i, value in country_dict.items():
    print(i, ' : ', value)