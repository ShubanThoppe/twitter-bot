import json as _json
import scraper as _scraper

if __name__ == "__main__":
    info = _scraper.scrape_data()
    with open("info.json", mode="w") as info_file:
        _json.dump(info, info_file, ensure_ascii=True)