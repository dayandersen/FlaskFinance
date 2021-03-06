import json
from database import create_database
from flask import request, render_template
from forms.login import LoginForm
from forms.calculators import CardsForm
from Finance import site_name, cards_dict


def index():
    form = LoginForm()
    return render_template('index.html',
                           name=site_name,
                           form=form)


def cards():
    form = CardsForm()
    json_cards = request.args.get('card_list')
    # If credit cards have been collected
    if json_cards is not None:
        card_list = json.loads(json_cards)
        reverse_card_dict = dict((v, k) for k, v in cards_dict.items())
        # Access the finance site database and the cards collection!
        finance_db = create_database("finance")
        card_col = finance_db['cards']
        benefits = []
        # Retrieve the benefits and cards from the database as selected by the user.
        for card in card_list:
            card_abbr = reverse_card_dict[card]
            print(card_col.find_one({'card': card_abbr}))

    return render_template('cards.html',
                           name=site_name,
                           form=form,
                           benefits=[])
