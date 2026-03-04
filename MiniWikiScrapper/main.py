import requests

def get_json(url):
    try:
        response = requests.get(url, headers={"User-Agent": "my-python-app/1.0 (your_email@example.com)"}, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error: {e}")
        return None

def search():
    query = input("Search: ").strip()
    if not query: return print("Search term required.")

    data = get_json(f"https://en.wikipedia.org/w/rest.php/v1/search/title?q={query}&limit={10}")
    return data.get('pages', []) if data else []

def display_summary(results):
    if not results: return print("No results found.")

    for i, page in enumerate(results):
        print(f"{i}) {page['title']}")

    try:
        idx = int(input(f"Select (0-{len(results)-1}): "))
        if not 0 <= idx < len(results): raise ValueError
    except ValueError: return print("Invalid selection.")

    data = get_json(f"https://en.wikipedia.org/api/rest_v1/page/summary/{results[idx]['key']}")
    if data: print(f"\n{data.get('extract', 'No summary available.')}\n")

if __name__ == "__main__":
    res = search()
    display_summary(res)