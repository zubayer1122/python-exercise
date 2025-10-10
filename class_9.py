# myfamily = {
#   "child1" : {"name" : "Emil","year" : 2004},
#   "child2" : {"name" : "Tobias","year" : 2007},
#   "child3" : {"name" : "Linus","year" : 2011}
# }

# x = myfamily["child1"]["name"]

# print(x)

# students = {
#     "S001": {
#         "name": "Alice",
#         "age": 21,
#         "courses": {
#             "math": {"grade": "A", "credits": 3},
#             "physics": {"grade": "B+", "credits": 4},
#         }
#     },
#     "S002": {
#         "name": "Bob",
#         "age": 22,
#         "courses": {
#             "math": {"grade": "B", "credits": 3},
#             "chemistry": {"grade": "A-", "credits": 4},
#         }
#     },
#     "S003": {
#         "name": "Charlie",
#         "age": 20,
#         "courses": {
#             "biology": {"grade": "A", "credits": 4},
#             "physics": {"grade": "B", "credits": 4},
#         }
#     }
# }

# x = students["S003"]["courses"]["physics"]["grade"]["credits"]

# print("The credits of physics is")
# print(x)

import camelcase

c = camelcase.CamelCase()

txt = "hello world"

print(c.hump(txt))