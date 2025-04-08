import requests
from bs4 import BeautifulSoup
import time

# Seznam odkazů na posledních 40 epizod (předpokládám, že je máš již připravený)
episode_urls = [
    "https://www.ceskatelevize.cz/porady/1093836883-na-plovarne/225542152000017/",
    "https://www.ceskatelevize.cz/porady/1093836883-na-plovarne/225542152000016/",
    "https://www.ceskatelevize.cz/porady/1093836883-na-plovarne/225542152000015/",
    "https://www.ceskatelevize.cz/porady/1093836883-na-plovarne/225542152000014/",
    "https://www.ceskatelevize.cz/porady/1093836883-na-plovarne/225542152000013/",
    "https://www.ceskatelevize.cz/porady/1093836883-na-plovarne/225542152000012/",
    "https://www.ceskatelevize.cz/porady/1093836883-na-plovarne/225542152000011/",
    "https://www.ceskatelevize.cz/porady/1093836883-na-plovarne/225542152000010/",
    "https://www.ceskatelevize.cz/porady/1093836883-na-plovarne/225542152000009/",
    "https://www.ceskatelevize.cz/porady/1093836883-na-plovarne/225542152000008/",
    "https://www.ceskatelevize.cz/porady/1093836883-na-plovarne/225542152000007/",
    "https://www.ceskatelevize.cz/porady/1093836883-na-plovarne/225542152000006/",
    "https://www.ceskatelevize.cz/porady/1093836883-na-plovarne/225542152000005/",
    "https://www.ceskatelevize.cz/porady/1093836883-na-plovarne/225542152000004/",
    "https://www.ceskatelevize.cz/porady/1093836883-na-plovarne/225542152000003/",
    "https://www.ceskatelevize.cz/porady/1093836883-na-plovarne/225542152000002/",
    "https://www.ceskatelevize.cz/porady/1093836883-na-plovarne/225542152000001/",
    "https://www.ceskatelevize.cz/porady/1093836883-na-plovarne/225542152000000/",
    "https://www.ceskatelevize.cz/porady/1093836883-na-plovarne/225542151999999/",
    # Přidej další URL k epizodám zde...
]

# Sem uložíme výsledky
data = []

# Funkce pro získání jména, profese a informací o výrobě
def get_guest_info_and_production(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Hledáme <h1> pro jméno hosta
    h1 = soup.find("h1")
    jmeno = h1.get_text(strip=True) if h1 else "N/A"

    # Profesionální informace bývají v následujícím odstavci <p>
    p = h1.find_next("p") if h1 else None
    profese = p.get_text(strip=True) if p else "N/A"

    # Hledáme li s atributem title="Rok výroby"
    rok_vyroby = "N/A"
    li_elements = soup.find_all("li", title=True)
    for li in li_elements:
        if "Rok výroby" in li["title"]:
            # Extrahujeme text, který je mezi <li> a </li>
            rok_vyroby = li.get_text(strip=True)
            break

    return jmeno, profese, rok_vyroby

# Projdeme všechny epizody
for url in episode_urls:
    try:
        jmeno, profese, rok_vyroby = get_guest_info_and_production(url)
        data.append({"Jméno": jmeno, "Profese": profese, "Rok výroby": rok_vyroby})
        print(f"✅ {jmeno} – {profese} – {rok_vyroby}")
        time.sleep(0.5)  # šetrné zpomalení pro server
    except Exception as e:
        print(f"Chyba u {url}: {e}")

# Výpis všech nalezených hostů
print("\n📋 Hosté:")
for idx, osoba in enumerate(data, 1):
    print(f"{idx}. {osoba['Jméno']} – {osoba['Profese']} – {osoba['Rok výroby']}")
