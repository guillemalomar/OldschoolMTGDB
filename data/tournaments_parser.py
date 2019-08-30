import hashlib
import json

my_file = ''
with open('files/prev_files/os_tournaments.json', 'r') as f:
    for line in f:
        my_file += line
    my_data = my_file.split('}{')

my_fixed_data = []
for ind, entry in enumerate(my_data):
    if ind == 0:
        my_fixed_data.append(entry + '}')
    elif ind == len(my_data) - 1:
        my_fixed_data.append('{' + entry)
    else:
        my_fixed_data.append('{' + entry + '}')

tournaments_data = ''
for entry in my_fixed_data:
    my_dict = json.loads(entry)
    tournament = {}
    tournament['_id'] = hashlib.md5('{}'.format(my_dict['name'].split('\n')[0]).encode('utf-8')).hexdigest()
    tournament['name'] = my_dict['name'].split('\n')[0]
    tournament['date'] = my_dict['date']
    tournament['players'] = int(my_dict['players'].split(' ')[0]) if len(my_dict['players'].split(' ')) == 2 else 0
    for t_deck in my_dict['decks']:
        deck = t_deck
        deck['_id'] = hashlib.md5('{}_{}'.format(my_dict['name'],
                                                 t_deck['player_name']).encode('utf-8')).hexdigest()
        deck['tournament'] = tournament['_id']
        with open('files/os_decks.json', 'a') as outfile:
            json.dump(deck, outfile)

    with open('files/os_tournaments.json', 'a') as outfile:
        json.dump(tournament, outfile)
