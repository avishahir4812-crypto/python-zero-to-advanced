movies = []

mov1 = input("enter your movie1:")
mov2 = input("enter your movie2:")
mov3 = input("enter your movie3:")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)


print(movies)
# movies[2] = "uri"
movies.reverse()
movies.remove(mov3)
print(movies)

