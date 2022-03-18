def define_suit(card):
    suit = card[-1]

    if suit == "S":
        return "spades"
    if suit == "D":
        return "diamonds"
    if suit == "H":
        return "hearts"
    if suit == "C":
        return "clubs"
