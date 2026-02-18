from bs4 import BeautifulSoup
import requests

# Fetch the content of the page
URL = 'https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2'
response = requests.get(URL)

# Check if the request was successful
print(f" Response code of request {response.status_code}")
if response.status_code == 200:
     page_content = response.content
else:
    print("Failed to retrieve the page")
    exit()



# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(page_content, 'html.parser')


# Find all the title elements
# Extract the article title and link
# print(soup.find_all(name="span", class_="titleline"))
all_titles = soup.find_all(name="h3" , class_="title")

# print(all_titles)

movie_titles = [movie.getText() for movie in all_titles]
# Reverse the list
movies = movie_titles[::-1]
# Saving the data into the file
with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")