from django.db import models


class Tournament(models.Model):
    _id = models.CharField(max_length=30, unique=True, primary_key=True, null=False)
    name = models.CharField(max_length=30, unique=True)
    date = models.DateField(auto_now_add=True)
    players = models.PositiveIntegerField(default=0, null=True)

    def __str__(self):
        return self.name

    def get_decks_count(self):
        return Deck.objects.filter(tournament=self).count()


class Deck(models.Model):
    _id = models.CharField(max_length=30, unique=True, primary_key=True, null=False)
    player_name = models.CharField(max_length=30)
    position = models.PositiveIntegerField(default=0)
    deck_name = models.CharField(max_length=30)
    date = models.DateField(auto_now_add=True)
    num_players = models.PositiveIntegerField(default=0, null=True)
    tournament = models.ForeignKey(Tournament, related_name='decks', on_delete=models.CASCADE)
    cards = models.CharField(max_length=30)

    def __str__(self):
        return self.deck_name


class Card(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
