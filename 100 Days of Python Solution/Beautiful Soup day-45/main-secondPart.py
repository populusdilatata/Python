from bs4 import BeautifulSoup
import requests

# Fetch the content of the page
url = 'https://news.ycombinator.com/front'
response = requests.get(url)

# Check if the request was successful
print(f" Response code of request {response.status_code}")
if response.status_code == 200:
     page_content = response.content
else:
    print("Failed to retrieve the page")
    exit()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(page_content, 'html.parser')


article_titles = []
article_links = []
# Find all the title elements
# Extract the article title and link
# print(soup.find_all(name="span", class_="titleline"))
articles = soup.find_all(name="span", class_="titleline")
for article_tag in articles:
    article_titles.append(article_tag.getText())
    article_links.append(article_tag.find("a")["href"])
    # article_links.append(article_tag.get("href"))

print(article_links)
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)

print(article_titles[largest_index])
print(article_links[largest_index])