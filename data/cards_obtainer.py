import json
import requests

header = {'content-type': 'application/json',
          'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
sets_endpoint = "https://api.scryfall.com/sets"
cards_endpoint = "https://api.scryfall.com/cards/collection"
coll_sets = ["lea", "leb", "drk", "leg", "arn", "atq", "2ed", "3ed", "4ed", "fbb", "4bb", "sum", "chr", "ced", "cei"]


def obtain_sets():
    r = requests.get(sets_endpoint)
    if r.status_code == 200:
        sets = json.loads(r.content)
        sets_names = [(x["name"], x["code"]) for x in sets["data"]]
        print(sets_names)


def obtain_all_cards():
    cards = {}
    for coll_set in coll_sets:
        cards[coll_set] = []
        for i in range(1, 600):
            if i % 10 == 0:
                print('{} - {}'.format(coll_set, i))
            to_ask = {
              "identifiers": [
                {
                  "set": coll_set,
                  "collector_number": str(i)
                }
              ]
            }
            r = requests.post(cards_endpoint, data=json.dumps(to_ask), headers=header)
            if r.status_code == 200:
                card_response = json.loads(r.content)
                if card_response["data"]:
                    cards[coll_set].append([x for x in card_response["data"]])
                else:
                    print('{} - {}'.format(coll_set, i))
                    break
            else:
                print('{} - {}'.format(coll_set, i))
                break
    with open("os_cards.json", "w") as outfile:
        json.dump(cards, outfile)


def obtain_cards_from_fallen():
    coll_set = 'fem'
    cards = {}
    cards[coll_set] = []
    for i in range(1, 200):
        if i % 10 == 0:
            print('{} - {}'.format(coll_set, i))
        to_ask = {
          "identifiers": [
            {
              "set": coll_set,
              "collector_number": str(i)
            }
          ]
        }
        r = requests.post(cards_endpoint, data=json.dumps(to_ask), headers=header)
        if r.status_code == 200:
            card_response = json.loads(r.content)
            if card_response["data"]:
                cards[coll_set].append([x for x in card_response["data"]])
            else:
                for version in ['a', 'b', 'c', 'd']:
                    to_ask = {
                        "identifiers": [
                            {
                                "set": coll_set,
                                "collector_number": str(i) + version
                            }
                        ]
                    }
                    r = requests.post(cards_endpoint, data=json.dumps(to_ask), headers=header)
                    if r.status_code == 200:
                        card_response = json.loads(r.content)
                        if card_response["data"]:
                            cards[coll_set].append([x for x in card_response["data"]])
                        else:
                            print('{} - {}'.format(coll_set, i))
                            break
        else:
            print('{} - {}'.format(coll_set, i))
            break
    with open("os_cards_{}.json".format(coll_set), "w") as outfile:
        json.dump(cards, outfile)


def obtain_cards_from_uncomplete_set(coll_set):
    cards = {}
    cards[coll_set] = []
    for i in range(1, 400):
        if i % 10 == 0:
            print('{} - {}'.format(coll_set, i))
        to_ask = {
          "identifiers": [
            {
              "set": coll_set,
              "collector_number": str(i)
            }
          ]
        }
        r = requests.post(cards_endpoint, data=json.dumps(to_ask), headers=header)
        if r.status_code == 200:
            card_response = json.loads(r.content)
            if card_response["data"]:
                cards[coll_set].append([x for x in card_response["data"]])
        else:
            print('{} - {}'.format(coll_set, i))
            break
    with open("os_cards_{}.json".format(coll_set), "w") as outfile:
        json.dump(cards, outfile)


# obtain_all_cards()
# obtain_cards_from_fallen()
obtain_cards_from_uncomplete_set('rin')
obtain_cards_from_uncomplete_set('ren')
