import requests
from bs4 import BeautifulSoup

# Send a GET request to the website URL
url = "https://www.dotmed.com/webstore/?user=193414&description=-1&manufacturer=-1&mode=all&sort=&order=&type=parts"
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")

print(soup.prettify())

# # Find the container element that holds the listings
# container = soup.find("div", class_="row")


# # Find all the listings within the container
# listings = container.find_all("div", class_="listing")

# # Process the listings
# for listing in listings:
#     # Extract information from each listing
#     title = listing.find("div", class_="listing-title").text.strip()
#     price = listing.find("div", class_="listing-price").text.strip()
#     description = listing.find("div", class_="listing-description").text.strip()

#     # Print or store the extracted information as needed
#     print("Title:", title)
#     print("Price:", price)
#     print("Description:", description)
#     print("----------------------")

# listing part cannot be found. check to catch listing data