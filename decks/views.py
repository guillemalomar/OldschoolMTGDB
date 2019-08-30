from django.db.models import Count
from django.shortcuts import get_object_or_404
from django.views.generic import ListView

from .models import Tournament, Card, Deck


class TournamentsListView(ListView):
    model = Tournament
    context_object_name = 'tournaments'
    template_name = 'home.html'


class DeckListView(ListView):
    model = Deck
    context_object_name = 'decks'
    template_name = 'decks.html'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        kwargs['tournament'] = self.tournament
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        self.tournament = get_object_or_404(Tournament, pk=self.kwargs.get('pk'))
        queryset = self.tournament.decks
        return queryset


class CardListView(ListView):
    model = Card
    context_object_name = 'cards'
    template_name = 'deck_cards.html'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        session_key = 'viewed_deck_{}'.format(self.deck.pk)
        if not self.request.session.get(session_key, False):
            self.deck.views += 1
            self.deck.save()
            self.request.session[session_key] = True
        kwargs['deck'] = self.deck
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        self.deck = get_object_or_404(Deck, tournament__pk=self.kwargs.get('pk'), pk=self.kwargs.get('deck_pk'))
        queryset = self.deck.cards.order_by('created_at')
        return queryset
