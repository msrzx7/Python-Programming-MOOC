# Write your solution here
def add_movie(database: list, name: str, director: str, year: int, runtime: int):
    d  = {"name": name,"director": director,"year": year,"runtime": runtime}
    database.append(d)
if __name__ == "__main__":
    print(add_movie(database,name,director,year,runtime))