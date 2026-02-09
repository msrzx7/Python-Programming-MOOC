# Write your solution here
def find_movies(database: list, search_term: str):
    search_result = []
    for movie in database:
        if search_term.lower() in movie["name"].lower():
           search_result.append(movie)
    return search_result

if __name__ == "__main__":
    print(find_movies(database,search_term))