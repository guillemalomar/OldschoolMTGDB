from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import UpdateView, ListView
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.urls import reverse

from .forms import NewDeckForm, CardForm
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
        queryset = self.tournament.decks.order_by('-last_updated').annotate(replies=Count('cards') - 1)
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


@login_required
def new_deck(request, pk):
    tournament = get_object_or_404(Tournament, pk=pk)
    if request.method == 'POST':
        form = NewDeckForm(request.POST)
        if form.is_valid():
            deck = form.save(commit=False)
            deck.tournament = tournament
            deck.starter = request.user
            deck.save()
            Card.objects.create(
                message=form.cleaned_data.get('message'),
                deck=deck,
                created_by=request.user
            )
            return redirect('deck_cards', pk=pk, deck_pk=deck.pk)
    else:
        form = NewDeckForm()
    return render(request, 'new_deck.html', {'tournament': tournament, 'form': form})


@login_required
def reply_deck(request, pk, deck_pk):
    deck = get_object_or_404(Deck, tournament__pk=pk, pk=deck_pk)
    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            card = form.save(commit=False)
            card.deck = deck
            card.created_by = request.user
            card.save()

            deck.last_updated = timezone.now()
            deck.save()

            deck_url = reverse('deck_cards', kwargs={'pk': pk, 'deck_pk': deck_pk})
            deck_card_url = '{url}?page={page}#{id}'.format(
                url=deck_url,
                id=card.pk,
                page=deck.get_page_count()
            )

            return redirect(deck_card_url)
    else:
        form = CardForm()
    return render(request, 'reply_deck.html', {'deck': deck, 'form': form})


@method_decorator(login_required, name='dispatch')
class CardUpdateView(UpdateView):
    model = Card
    fields = ('message', )
    template_name = 'edit_card.html'
    pk_url_kwarg = 'card_pk'
    context_object_name = 'card'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(created_by=self.request.user)

    def form_valid(self, form):
        card = form.save(commit=False)
        card.updated_by = self.request.user
        card.updated_at = timezone.now()
        card.save()
        return redirect('deck_cards', pk=card.deck.tournament.pk, deck_pk=card.deck.pk)
