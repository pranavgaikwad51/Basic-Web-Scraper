import requests
from bs4 import BeautifulSoup

def scrape_hacker_news():
    """
    Scrapes the top headlines and links from the Hacker News homepage.
    """
    # Define the URL of the news site to scrape
    url = 'https://news.ycombinator.com/'

    try:
        # 1. Send an HTTP GET request to the URL
        response = requests.get(url)
        # Raise an exception if the request was unsuccessful (e.g., 404 Not Found)
        response.raise_for_status()

        # 2. Parse the HTML content of the page with BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # 3. Find all the headline elements
        # On Hacker News, headlines are in <span> tags with the class 'titleline'
        headlines = soup.find_all('span', class_='titleline')

        if not headlines:
            print("No headlines found. The site's HTML structure may have changed.")
            return

        print(f"--- Top Headlines from Hacker News --- 📰\n")

        # 4. Loop through the found elements and extract the text and link
        for index, headline in enumerate(headlines, 1):
            title_element = headline.find('a')
            if title_element:
                title = title_element.get_text()
                link = title_element['href']
                print(f"{index}. {title}")
                print(f"   Link: {link}\n")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")

# Run the scraper
scrape_hacker_news()
