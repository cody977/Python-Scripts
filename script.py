import requests
from bs4 import BeautifulSoup

def get_html_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        return response.text
    except requests.exceptions.RequestException as e:
        print("Error fetching URL: {e}")
        return None

def main():
    #website url
    url = "https://google.com"
    html_content = get_html_content(url)

    if html_content:
        print("HTML Content:")
        print(html_content)

    else:
        print("Failed to retrieve HTML content.")

if __name__ == "__main__":
    main()
