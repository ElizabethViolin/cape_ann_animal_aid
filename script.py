import requests
from bs4 import BeautifulSoup

# Define the URL of the iframe to check
iframe_url = 'https://ws.petango.com/webservices/adoptablesearch/wsAdoptableAnimals.aspx?species=Dog&gender=A&agegroup=All&location=&site=&onhold=N&orderby=Name&colnum=2&css=http://ws.petango.com/WebServices/adoptablesearch/css/styles.css&authkey=8cyw3mw2bj6lvdg7nxfqmhvq33fvuxnyxotje5j7fkjynq0wio&recAmount=&detailsInPopup=Yes&featuredPet=Include&stageID='

try:
    # Send a GET request to fetch the HTML content of the iframe
    response = requests.get(iframe_url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all <a> elements
        links = soup.find_all('a')
        
        # Check each <a> tag within these <div> elements
        for link in links:
            href = link.get('href', '')
            link_text = link.text.strip()
            
            # Check if the href attribute contains the JavaScript function
            if 'javascript:poptastic' in href:
                # Check if the text contains "Andy"
                if 'Andy' in link_text:
                    print(True)
                    break
        else:
            # If no link with "Andy" is found
            print(False)
    else:
        print('Failed to fetch the iframe content. Status code:', response.status_code)
except Exception as e:
    print('An error occurred:', str(e))
