MONGODB_AUTH= --authenticationDatabase admin --username root --password mongoadmin

.PHONY: build
build:
	docker-compose up --build
.PHONY: run
run:
	docker-compose up

.PHONY: fixtures
# Load database fixtures
fixtures:
	docker-compose exec mongodb /usr/bin/mongoimport --db decks --collection decks_tournament $(MONGODB_AUTH) /tmp/os_tournaments.json --jsonArray
	docker-compose exec mongodb /usr/bin/mongoimport --db decks --collection decks_deck $(MONGODB_AUTH) /tmp/os_decks.json --jsonArray
	docker-compose exec mongodb /usr/bin/mongoimport --db decks --collection decks_card $(MONGODB_AUTH) /tmp/os_cards.json --jsonArray
