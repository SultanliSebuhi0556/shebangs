import requests
from datetime import datetime, timedelta

class GameInfo:
    def __init__(self, title, end_date, image_url=None):
        self.title = title
        self.end_date = end_date
        self.image_url = image_url

def get_free_games():
    games = []

    headers = {
        "Accept": "application/json",
        "User-Agent": "Mozilla/5.0"
    }

    try:
        url = "https://store-site-backend-static-ipv4.ak.epicgames.com/freeGamesPromotions?locale=en-US&country=AZ&allowCountries=AZ"
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()

        elements = data["data"]["Catalog"]["searchStore"]["elements"]
        for item in elements:
            # if item.get("expiryDate") is None:
            #     continue
                
            promotions = item.get("promotions")
            if not promotions:
                continue

            promo_offers = promotions.get("promotionalOffers")
            if not promo_offers or len(promo_offers) == 0:
                continue

            first_promo = promo_offers[0].get("promotionalOffers")
            if not first_promo or len(first_promo) == 0:
                continue

            offer = first_promo[0]
            start_str = offer["startDate"]
            end_str = offer["endDate"]

            end_date = (datetime.fromisoformat(end_str.replace("Z", "+00:00")) + timedelta(hours=4)).strftime("%d-%m-%Y %I:%M %p")

            title = item.get("title")
            image_url = item.get("keyImages")[0]["url"] if item.get("keyImages") else None

            games.append(GameInfo(title, end_date, image_url))

    except Exception as e:
        print(f"Error fetching games: {e}")

    return games

def main():
    games = get_free_games()

    if not games:
        print("No free games available at the moment.")
        return
    else:
        for i in range(len(games)):
            print(f"{games[i].title}§{games[i].end_date}§{games[i].image_url}")
            
if __name__ == "__main__":
    main()
