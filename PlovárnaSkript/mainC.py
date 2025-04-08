import requests
from bs4 import BeautifulSoup
import time

# Seznam odkazů na posledních 40 epizod (předpokládám, že je máš již připravený)
episode_urls = [
"https://www.ceskatelevize.cz/porady/1093836883-na-plovarne/224542152000034/",
"https://www.ceskatelevize.cz/porady/1093836883-na-plovarne/224542152000033/",
"https://www.ceskatelevize.cz/porady/1093836883-na-plovarne/224542152000032/",
"https://www.ceskatelevize.cz/porady/1093836883-na-plovarne/224542152000031/",
"https://www.ceskatelevize.cz/porady/1093836883-na-plovarne/224542152000030/",
"https://www.ceskatelevize.cz/porady/1093836883-na-plovarne/224542152000029/",
"https://www.ceskatelevize.cz/porady/1093836883-na-plovarne/224542152000028/",
"https://www.ceskatelevize.cz/porady/1093836883-na-plovarne/224542152000027/",
"https://www.ceskatelevize.cz/porady/1093836883-na-plovarne/224542152000026/",
"https://www.ceskatelevize.cz/porady/1093836883-na-plovarne/224542152000025/",
"https://www.ceskatelevize.cz/porady/1093836883-na-plovarne/224542152000024/",
"https://www.ceskatelevize.cz/porady/1093836883-na-plovarne/224542152000023/",
"https://www.ceskatelevize.cz/porady/1093836883-na-plovarne/224542152000022/",
"https://www.ceskatelevize.cz/porady/1093836883-na-plovarne/224542152000021/",
"https://www.ceskatelevize.cz/porady/1093836883-na-plovarne/224542152000020/",
"https://www.ceskatelevize.cz/porady/1093836883-na-plovarne/224542152000019/",
"https://www.ceskatelevize.cz/porady/1093836883-na-plovarne/224542152000018/",
"https://www.ceskatelevize.cz/porady/1093836883-na-plovarne/224542152000017/",
"https://www.ceskatelevize.cz/porady/1093836883-na-plovarne/224542152000016/",
"https://www.ceskatelevize.cz/porady/1093836883-na-plovarne/224542152000015/",
"https://www.ceskatelevize.cz/porady/1093836883-na-plovarne/224542152000014/",
"https://www.ceskatelevize.cz/porady/1093836883-na-plovarne/224542152000013/",
"https://www.ceskatelevize.cz/porady/1093836883-na-plovarne/224542152000012/",
"https://www.ceskatelevize.cz/porady/1093836883-na-plovarne/224542152000011/",
"https://www.ceskatelevize.cz/porady/1093836883-na-plovarne/224542152000010/",
"https://www.ceskatelevize.cz/porady/1093836883-na-plovarne/224542152000009/",
"https://www.ceskatelevize.cz/porady/1093836883-na-plovarne/224542152000008/",
"https://www.ceskatelevize.cz/porady/1093836883-na-plovarne/224542152000007/",
"https://www.ceskatelevize.cz/porady/1093836883-na-plovarne/224542152000006/",
"https://www.ceskatelevize.cz/porady/1093836883-na-plovarne/224542152000005/",
"https://www.ceskatelevize.cz/porady/1093836883-na-plovarne/224542152000004/",
"https://www.ceskatelevize.cz/porady/1093836883-na-plovarne/224542152000003/",
"https://www.ceskatelevize.cz/porady/1093836883-na-plovarne/224542152000002/",
"https://www.ceskatelevize.cz/porady/1093836883-na-plovarne/224542152000001/",



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
            li_text = li.get_text(strip=True)

            # Získáme poslední čtyři znaky a ověříme, zda jsou číslice
            last_four = li_text[-4:]
            if last_four.isdigit():
                rok_vyroby = last_four
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
print("\n Hosté:")
for idx, osoba in enumerate(data, 1):
    print(f"{idx}. {osoba['Jméno']} – {osoba['Profese']} – {osoba['Rok výroby']}")
