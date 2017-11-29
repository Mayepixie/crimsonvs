from django.shortcuts import render, HttpResponse, get_object_or_404

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


def gallery(request):
    return HttpResponse('These are all the cards!: ')
