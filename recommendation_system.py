movies = {
    "Action": ["KGF", "Pushpa", "War"],
    "Comedy": ["Hera Pheri", "Dhamaal", "Golmaal"],
    "Sci-Fi": ["Interstellar", "Inception", "The Matrix"],
    "Horror": ["The Conjuring", "It", "Annabelle"]
}

print("Movie Categories:")
for category in movies:
    print("-", category)

choice = input("\nEnter a category: ")

if choice in movies:
    print("\nRecommended Movies:")
    for movie in movies[choice]:
        print("-", movie)
else:
    print("Category not found!")
