function addCard() {
    var list = getCards();
    var card = getSelectedCard();
    var div = document.getElementById("cardlist");

    var html = "<ul>";

    for (var i = 0; i < list.length; i++) {
        html += "<li class='cardEntry'>" + list[i] + "</li>"
    }

    html += "<li class='cardEntry'>" + card + "</li>";
    html += "</ul>";
    div.innerHTML = html;
}

function getCards() {
    var elements = document.getElementsByClassName("cardEntry")
    var list = [];

    for (var i = 0; i < elements.length; i++) {
        list.push(elements[i].innerHTML);
    }
    return list;
}

function submitGet() {
    var cards = getCards()
    jQuery.getJSON('cards', {
        card_list: JSON.stringify(cards)
    }, null);
}

function getSelectedCard() {
    var cardselector = document.getElementById("cards_selector");
    return cardselector[cardselector.selectedIndex].text;
}