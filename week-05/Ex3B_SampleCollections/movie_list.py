movies = ["I'm", "not", "into", "movies"]

print(f'The list movies includes my top {(len(movies))} favorite movies')
print(sorted(movies))
#sorted
movies.sort()
print(movies)

movies.append('Less movies')
print(f'I added another movie, the list is now {movies}')