#!/usr/bin/env bash

python manage.py makemigrations
python manage.py migrate
mongoimport -d decks -c decks_tournament data/files/os_tournaments.json
mongoimport -d decks -c decks_deck data/files/os_decks.json
mongoimport -d decks -c decks_card data/files/os_cards.json
python manage.py runserver
