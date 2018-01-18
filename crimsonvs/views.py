from django.shortcuts import render, HttpResponse, get_object_or_404, get_list_or_404

# Create your views here.


def index(request):
    from crimsonvs.models import Card

    five_cards = Card.objects.order_by('id')[:5]
    context = {'five_cards': five_cards}
    return render(request, 'index.html', context)


def card(request, card_id):
    from crimsonvs.models import Card

    selected_card = get_object_or_404(Card, id=card_id)
    return render(request, 'card.html', {'card': selected_card})


def deck(request, user_id, deck_id):
    from crimsonvs.models import Deck

    deck = get_list_or_404(Deck, user_id=user_id, deck_id=deck_id)
    return render(request, 'deck.html', {'deck': deck})


def decks(request, user_id):
    from crimsonvs.models import Deck

    decks = get_list_or_404(Deck, user_id=user_id)
    return render(request, 'decks.html', {'decks': decks})


def gallery(request, user_id):
    from crimsonvs.models import Gallery

    user_gallery = get_list_or_404(Gallery, user_id=user_id)
    return render(request, 'gallery.html', {'gallery': user_gallery})
