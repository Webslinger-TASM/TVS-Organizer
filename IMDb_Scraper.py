import Utilites as Utils

from bs4 import BeautifulSoup
from lxml.etree import XMLSyntaxError
from requests import get, exceptions
from typing import Tuple
from os.path import join


def get_html(url: str) -> str:
    fake_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"}

    try:
        response = get(url, headers=fake_headers, timeout=5)

        if response.status_code != 200:
            raise Exception(f"An error occurred from the website: Code: {response.status_code}")

        html_content = response.text

    except exceptions.RequestException as err:
        print(f"An error occurred while trying to get the HTML: {err}")

    return html_content


def parser(unparsed_html: str) -> Tuple[list[str], str, str, list[str]]:
    try:
        html = BeautifulSoup(unparsed_html, features="lxml")
        soup = BeautifulSoup.find(html, "section", class_="ipc-page-section ipc-page-section--base ipc-page-section--sp-pageMargin")

        div_seasons = soup.find("div", class_="ipc-tabs ipc-tabs--base ipc-tabs--align-left ipc-tabs--display-chip ipc-tabs--inherit")
        div_ul_seasons = div_seasons.find("ul", class_="ipc-tabs ipc-tabs--base ipc-tabs--align-left")
        links_seasons = [link["href"] for link in div_ul_seasons.find_all('a', href=True)]

        titles = [title.get_text() for title in soup.find_all("div", class_="ipc-title__text")]

        dates = soup.find_all("span", class_="sc-ccd6e31b-10 fVspdm")
        first_date, last_date = dates[0].get_text(), dates[-1].get_text()

    except XMLSyntaxError as err:
        print(f"An error occurred while parsing the HTML: {err}")

    return titles, first_date, last_date, links_seasons


def main(mode) -> Tuple[list[str], list[list[str]], int, list[list[str]]]:
    if input("\nDo you want to automatically get the HTML content by requesting the website? (y/n) ") in ('y', 'yes'):
        source = "Online"
        url = input("What's the link to your show in IMDb? ").split('?')[0]

        if "episodes" not in url:
            url = join(url, "episodes")

    else:
        source = "Offline"

    years: list[str] = []
    sxxexxes: list[list[str]] = []
    ep_names: list[list[str]] = []
    links: list[str] = []

    se_current = 1

    while True:
        if source == "Online":
            if se_current != 1:
                html = get_html(f"https://imdb.com{links[se_current-1]}")
            else:
                html = get_html(url)
        else:
            try:
                with open(f"{input(f"HTML filename for season {se_current}: ")}.html", 'r', encoding="utf-8") as file:
                    html = file.read()

            except FileNotFoundError or OSError as err:
                print(f"An error occured while reading the file. {err}")

        titles, first_date, last_date, links = parser(html)

        years.append(Utils.sort_dates(first_date, last_date))

        tmp_sxxexxes, tmp_titles = Utils.sort_titles(titles, mode)
        sxxexxes.append(tmp_sxxexxes), ep_names.append(tmp_titles)

        if se_current == len(links):
            break

        se_current += 1

    return years, sxxexxes, len(links), ep_names