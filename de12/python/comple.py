import requests

response = requests.get("https://www.quotefancy.com/api/quotes/random")
if response.status_code == 200:
    data = response.json()
    quote = data['quote']
    author = data['author']
    print(quote)
    print(f"- {author}")

