fixtures:
	#docker-compose exec mongodb /usr/bin/mongoimport --db decks --collection decks_tournament --authenticationDatabase admin --username root --password mongoadmin /tmp/os_tournaments.json --jsonArray
	#docker-compose exec mongodb /usr/bin/mongoimport --db decks --collection decks_deck --authenticationDatabase admin --username root --password mongoadmin /tmp/os_decks.json --jsonArray
	docker-compose exec mongodb /usr/bin/mongoimport --db decks --collection decks_card --authenticationDatabase admin --username root --password mongoadmin /tmp/os_cards.json --jsonArray
	