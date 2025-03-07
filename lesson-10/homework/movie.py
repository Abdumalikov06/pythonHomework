import requests
import random

api_key='8668967239e2e18a9ac62273510a41e7'
genre=input("Enter a movie genre: ").lower()
genre_map = {
    "action": 28,
    "adventure": 12,
    "animation": 16,
    "comedy": 35,
    "crime": 80,
    "documentary": 99,
    "drama": 18,
    "family": 10751,
    "fantasy": 14,
    "history": 36,
    "horror": 27,
    "music": 10402,
    "mystery": 9648,
    "romance": 10749,
    "science fiction": 878,
    "tv movie": 10770,
    "thriller": 53,
    "war": 10752,
    "western": 37
}


if genre in genre_map:
    genre_id=genre_map[genre]
else:
    print('invalid genre, please try again.')
    exit()


url=f'https://api.themoviedb.org/3/discover/movie?api_key={api_key}&with_genres={genre_id}'

res=requests.get(url)


if res.status_code == 200:
    data=res.json()
    movies = data.get("results", [])
    if movies:
        random_movie = random.choice(movies)
        print(f"Title: {random_movie['title']}")
        print(f"Original title: {random_movie['original_title']}")
        print(f"Released year: {random_movie['release_date']}")
        print(f"Popularity: {random_movie['popularity']}")
        print(f"Overview: {random_movie['overview']}")
    else:
        print("There is not any movie in this genre")
else:
    print("Failed to retrive data. Check you API key")

