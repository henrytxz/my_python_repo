from collections import Counter

def poker(hands):
    return max(hands, key=hand_rank)

def flush(hand):
    suits = [card[0] for card in hand]
    if len(set(suits)) == 1:
        return True
    else:
        return False

def rank(hand):
    ranks = [int(card[1:]) for card in hand]
    return sorted(ranks, reverse=True)

def straight(hand):
    ranks = rank(hand)
    for i in range(4):
        rank_i = ranks[i]
        rank_i_plus_1 = ranks[i+1]
        if rank_i-rank_i_plus_1 != 1:
            return False
    return True

def kind(hand):
    """
    :param hand:
    :return:
    4 for 4 of a kind
    3 for 3 of a kind
    2 for a pair or two pairs
    will return 6 for full house, so kind of do what hand_rank is supposed to do
    """
    ranks = rank(hand)
    c = Counter(ranks)
    most_common_ranks = c.most_common()
    kind_rank, kind_number = most_common_ranks[0]
    if kind_number == 4:
        return (4, kind_rank, [r for r in ranks if r!=kind_rank])
    elif kind_number == 3:
        second_kind_rank, second_kind_number = most_common_ranks[1]
        if second_kind_number == 2: # we got a full house
            return (6, kind_rank, second_kind_rank)
        else:
            return (3, kind_rank, [r for r in ranks if r!=kind_rank])
    elif kind_number == 2:
        second_kind_rank, second_kind_number = most_common_ranks[1]
        if second_kind_number == 2:  # we got 2 pairs
            return (2, (max([kind_rank, second_kind_rank]),
                        min([kind_rank, second_kind_rank])),
                   [r for r in ranks if r!=kind_rank and r!=second_kind_rank])
        else:
            return (1, [r for r in ranks if r!=kind_rank], None)
    else:
        return (0, ranks, None)

def hand_rank(hand):
    n_kind, kind_rank, other_cards = kind(hand)
    if flush(hand) and straight(hand):
        return (8, rank(hand)[0])
    elif n_kind == 4:
        return (7, kind_rank, other_cards)
    elif n_kind == 6:
        return (6, kind_rank, other_cards)


def run():
    sf = 'C11 C10 C9 C8 C7'.split()
    assert flush(sf)
    assert straight(sf)
    assert hand_rank(sf) == (8, 11)

    four_kind = 'S14 H14 D14 C14 H12'.split()   # 4 ACES, AND A QUEEN KICKER!
    assert not flush(four_kind)
    assert not straight(four_kind)
    assert hand_rank(four_kind) == (7, 14, [12])

    fh = 'S8 H8 D8 S13 C13'.split()  # FULL HOUSE, EIGHTS OVER KINGS!
    fl = 'D10 D8 D7 D5 D3'.split()
    str8t = 'C11 S10 D9 C8 C7'.split()  # STRAIGHT, JACK HIGH!
    three_kind = 'H7 D7 C7 C5 C2'.split()  # THREE SEVENS!
    two_pair = 'D11 C11 S3 H3 H13'.split()  # TWO PAIR, JACKS AND THREES!
    pair = 'H2 S2 D11 H6 C3'.split()       # PAIR OF TWOS, JACK HIGH...
    nothing = 'C7 C5 C4 C3 D2'.split()     # SEVEN HIGH

    assert poker([four_kind, fh]) == four_kind
    assert poker([fl, fh]) == fh
    assert poker([fl, str8t]) == fl
    assert poker([three_kind, str8t]) == str8t
    assert poker([three_kind, two_pair]) == three_kind
    assert poker([pair, two_pair]) == two_pair
    assert poker([pair, nothing]) == pair

if __name__ == '__main__':
    run()