# ╭──────────────╮
# │ [FrenchDeck] │
# ╰──────────────╯
import collections
import random
Card = collections.namedtuple('Card',['rank','suit'])
# rank (القيمة الرقمية): مثل (2، 3، J، Q، K، A).
# suit (شكل الكارت): مثل (البستوني/spades، الديناري/diamonds، الكُبّة/hearts، السباتي/clubs)
class Frenchdeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
    def __repr__(self):
        return repr(self._cards)
    def __len__(self):
        return len(self._cards)
    def __iter__(self):
        return iter(self._cards)
    def __getitem__(self,position):
        return self._cards[position]
    def __setitem__(self, position, value):
        self._cards[position] = value
# NOTE: __getitem__ delegates to the [] operator of self._cards, our deck automatically supports slicing. Here’s how we look at the top three cards from abrand-new deck, and then pick just the aces by starting at index 12 and skipping 13 cards at a time:
deck = Frenchdeck()
# print(deck[:13])
# print(Card('Q', 'hearts') in deck)
# print(deck)
# random.shuffle(deck)
# print(deck)
# ────────────────────────────────── SECTION ───────────────────────────────────
# الترتيب
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
# ودي معناها spades > hearts > diamonds > clubs لان الترتيب المطلوب هو 2 < 3 < 4 < ... < 10 < J < Q < K < A
def spades_high(card):
    rank_value = Frenchdeck.ranks.index(card.rank) #--> هنا لما يدخل رقم الكارت هيجبله مكانه مثلا FrenchDeck.ranks.index('2') = 0 و FrenchDeck.ranks.index('A')
    return rank_value * len(suit_values) + suit_values[card.suit]
    #  نختار رقم وليكن 2 clup 
    # 0*4+0=0
    # 3 كلوب 
    # 1*4+0=4
    # Rank 2
# 0  1  2  3
# ♣  ♦  ♥  ♠

# Rank 3
# 4  5  6  7
# ♣  ♦  ♥  ♠

# Rank 4
# 8  9 10 11
# ♣  ♦  ♥  ♠
kotshina = []

for n, card in enumerate(sorted(deck, key=spades_high), start=1):
    kotshina.append((n,card))

print(kotshina)
