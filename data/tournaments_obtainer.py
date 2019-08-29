import json
import re
from bs4 import BeautifulSoup
from http.cookiejar import CookieJar
from urllib import request

card_types = ['Creatures', 'Instants', 'Sorceries', 'Enchantments', 'Artifacts', 'Lands']
main_url = 'http://tcdecks.net/'


def obtain_page(url):
    cj = CookieJar()
    cp = request.HTTPCookieProcessor(cj)
    try:
        opener = request.build_opener(cp)
        with opener.open(url, timeout=1000) as response:
            soup = BeautifulSoup(response.read())
    except:
        soup = None
    return soup


def process_deck(deck_page):
    found_deck = {
        'player_name': '',
        'position': 0,
        'deck_name': '',
        'date': '',
        'num_players': '',
        'cards': {
            'maindeck': [],
            'sideboard': []
        }
    }
    top_header = deck_page.find('h5').get_text()
    date = top_header.split(' | Date: ')[1].strip()
    found_deck['date'] = date
    num_players = top_header.split('| Number of Players: ')[1].split(' | ')[0].strip()
    found_deck['num_players'] = num_players

    table_headers = deck_page.find_all('th')
    player_name = table_headers[0].get_text().split(' playing')[0].strip()
    found_deck['player_name'] = player_name
    position = table_headers[1].get_text().split('Position: ')[1].strip()
    found_deck['position'] = int(position)
    deck_name = table_headers[2].get_text().split('Deck Name: ')[1].strip()
    found_deck['deck_name'] = deck_name

    all_tables = deck_page.find('table', {'class': 'table_deck'}).findAll('td')
    main_deck_data = ''
    sideboard_deck_data = ''
    for table in all_tables:
        if table.has_attr('id') and table['id'] == 'sideboard':
            sideboard_deck_data += table.get_text().strip().replace('\n', '').replace('\r', '')
        elif (table.has_attr('scope') and table['scope'] != "side_movil") or not table.has_attr('scope'):
            main_deck_data += table.get_text().strip().replace('\n', '').replace('\r', '')
    for card_type in card_types:
        main_deck_data = main_deck_data.replace(card_type + ' ', '')
        sideboard_deck_data = sideboard_deck_data.replace(card_type + ' ', '')
    main_deck_data = re.sub(r"\[[0-9]*\]", "", main_deck_data)
    sideboard_deck_data = re.sub(r"\[[0-9]*\]", "", sideboard_deck_data)
    card_num = 0
    card_name = ''
    for ind, letter in enumerate(main_deck_data):
        if ind == 0:
            card_num = letter
        else:
            try:
                new_card_num = int(letter)
                if card_name != '':
                    found_deck['cards']['maindeck'].append((card_name, int(card_num)))
                card_num = new_card_num
                card_name = ''
            except ValueError:
                card_name += letter
    found_deck['cards']['maindeck'].append((card_name, int(card_num)))
    card_num = 0
    card_name = ''
    for ind, letter in enumerate(sideboard_deck_data):
        if ind == 0:
            card_num = letter
        else:
            try:
                new_card_num = int(letter)
                if card_name != '':
                    found_deck['cards']['sideboard'].append((card_name, int(card_num)))
                card_num = new_card_num
                card_name = ''
            except ValueError:
                card_name += letter
    found_deck['cards']['sideboard'].append((card_name, int(card_num)))
    return found_deck


def obtain_info():
    num_decks = 0
    for i in range(1, 4):
        home_page = obtain_page('https://www.tcdecks.net/format.php?format=Vintage%20Old%20School&page={}'.format(i))
        tournaments = home_page.find('table', {'class': 'tourney_list'}).find_all('tr')[1:]
        for tournament in tournaments:
            found_tournament = {}
            found_tournament['name'] = tournament.find('td', {'data-th': 'Tournament Name'}).get_text().strip()
            found_tournament['players'] = tournament.find('td', {'data-th': 'Players'}).get_text().strip()
            found_tournament['date'] = tournament.find('td', {'data-th': 'Date'}).get_text().strip()
            found_tournament['decks'] = {}
            tournament_url = tournament.find('td', {'data-th': 'Tournament Name'}).find('a')['href']
            tournament_page = obtain_page('https://www.tcdecks.net/{}'.format(tournament_url))
            tournament_decks = tournament_page.find('table', {'class': 'tourney_list'}).find_all('tr')[1:]
            for deck in tournament_decks:
                num_decks += 1
                deck_url = deck.find('a')['href']
                deck_position = deck.find('td', {'data-th': 'Position'}).get_text().strip()
                deck_page = obtain_page('https://www.tcdecks.net/{}'.format(deck_url))
                found_tournament['decks'][deck_position] = process_deck(deck_page)
                print(deck_url)
                print('{}%'.format((num_decks/644)*100))
            with open('os_tournaments.json', 'a') as outfile:
                json.dump(found_tournament, outfile)
    print('Total number of decks analyzed: {}'.format(num_decks))


obtain_info()
