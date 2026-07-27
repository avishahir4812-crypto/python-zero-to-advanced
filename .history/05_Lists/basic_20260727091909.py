movies = []

# mov1 = input("enter your movie1:")
# mov2 = input("enter your movie2:")
# mov3 = input("enter your movie3:")

# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)


# print(movies)
# # # movies[2] = "uri"
# # movies.reverse()
# # movies.remove(mov3)
# movies.insert(1,"uri")

# movies= movies[2:3]
# print(movies)



#palidrome

list = [1,2,3,3,2,1]
list1 = [5,4,3,2,1]

copy_list = list.copy()
copy_list.reverse()

if list == copy_list:
    print("palidrome")
else:
    print("not palidrome")

list.sort()

print(list)