from collections import Counter

""" Problem 1 
In Camel Cards, you get a list of hands, and your goal is to order them based on the strength of each hand. A hand consists of five cards labeled one of A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2. The relative strength of each card follows this order, where A is the highest and 2 is the lowest.

Every hand is exactly one type. From strongest to weakest, they are:

Five of a kind, where all five cards have the same label: AAAAA
Four of a kind, where four cards have the same label and one card has a different label: AA8AA
Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
High card, where all cards' labels are distinct: 23456
Hands are primarily ordered based on type; for example, every full house is stronger than any three of a kind.

If two hands have the same type, a second ordering rule takes effect. Start by comparing the first card in each hand. If these cards are different, the hand with the stronger first card is considered stronger. If the first card in each hand have the same label, however, then move on to considering the second card in each hand. If they differ, the hand with the higher second card wins; otherwise, continue with the third card in each hand, then the fourth, then the fifth.

So, 33332 and 2AAAA are both four of a kind hands, but 33332 is stronger because its first card is stronger. Similarly, 77888 and 77788 are both a full house, but 77888 is stronger because its third card is stronger (and both hands have the same first and second card).

To play Camel Cards, you are given a list of hands and their corresponding bid (your puzzle input). For example:

32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
This example shows five hands; each hand is followed by its bid amount. Each hand wins an amount equal to its bid multiplied by its rank, where the weakest hand gets rank 1, the second-weakest hand gets rank 2, and so on up to the strongest hand. Because there are five hands in this example, the strongest hand will have rank 5 and its bid will be multiplied by 5.

So, the first step is to put the hands in order of strength:

32T3K is the only one pair and the other hands are all a stronger type, so it gets rank 1.
KK677 and KTJJT are both two pair. Their first cards both have the same label, but the second card of KK677 is stronger (K vs T), so KTJJT gets rank 2 and KK677 gets rank 3.
T55J5 and QQQJA are both three of a kind. QQQJA has a stronger first card, so it gets rank 5 and T55J5 gets rank 4.
Now, you can determine the total winnings of this set of hands by adding up the result of multiplying each hand's bid with its rank (765 * 1 + 220 * 2 + 28 * 3 + 684 * 4 + 483 * 5). So the total winnings in this example are 6440.

Find the rank of every hand in your set. What are the total winnings?
"""

""" Problem 2
To make things a little more interesting, the Elf introduces one additional rule. Now, J cards are jokers - wildcards that can act like whatever card would make the hand the strongest type possible.

To balance this, J cards are now the weakest individual cards, weaker even than 2. The other cards stay in the same order: A, K, Q, T, 9, 8, 7, 6, 5, 4, 3, 2, J.

J cards can pretend to be whatever card is best for the purpose of determining hand type; for example, QJJQ2 is now considered four of a kind. However, for the purpose of breaking ties between two hands of the same type, J is always treated as J, not the card it's pretending to be: JKKK2 is weaker than QQQQ2 because J is weaker than Q.

Now, the above example goes very differently:

32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
32T3K is still the only one pair; it doesn't contain any jokers, so its strength doesn't increase.
KK677 is now the only two pair, making it the second-weakest hand.
T55J5, KTJJT, and QQQJA are now all four of a kind! T55J5 gets rank 3, QQQJA gets rank 4, and KTJJT gets rank 5.
With the new joker rule, the total winnings in this example are 5905.

Using the new joker rule, find the rank of every hand in your set. What are the new total winnings?
"""

with open("inputs/7.txt", "r") as file:
    hands = file.read().splitlines()


def tiebreaker(hand: str, card_values: str):
    return tuple(card_values.index(c) for c in hand)


def hand_to_value(hand: str, with_joker: bool = False):
    hand_values = sorted(Counter(hand).values())
    if with_joker and (num_j := hand.count("J")) and num_j < 5:
        hand_values.remove(num_j)
        hand_values[-1] += num_j

    match hand_values:
        case [5]:  # 5 of a kind
            return 7
        case [1, 4]:  # 4 of a kind
            return 6
        case [2, 3]:  # full house
            return 5
        case [1, 1, 3]:  # 3 of a kind
            return 4
        case [1, 2, 2]:  # 2 pair
            return 3
        case [1, 1, 1, 2]:  # 1 pair
            return 2
        case [1, 1, 1, 1, 1]:  # high card
            return 1
        case _:
            raise ValueError(f"unknown hand: {hand} ({sorted(Counter(hand).values())})")


def solve(with_joker) -> int:
    card_values = "J23456789TQKA" if with_joker else "23456789TJQKA"

    scored_hands: list[tuple[int, tuple[int, ...], int]] = []
    for line in hands:
        hand, bid = line.split()
        scored_hands.append(
            (
                hand_to_value(hand, with_joker=with_joker),
                tiebreaker(hand, card_values),
                int(bid),
            )
        )

    return sum((idx + 1) * bid for idx, (_, _, bid) in enumerate(sorted(scored_hands)))


solution_1 = solve(with_joker=False)
solution_2 = solve(with_joker=True)
print("Solution 1:", solution_1)
print("Solution 2:", solution_2)


# Old solution

cards_map = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}


def count_letters(string, cards_map=cards_map):
    letters = {}
    for letter in string:
        letter_mapped = cards_map[letter]
        if letter_mapped in letters:
            letters[letter_mapped] += 1
        else:
            letters[letter_mapped] = 1

    return letters


# return True if hand1 is stronger than hand2 otherwise False
def hand_compare(hand1, hand2):
    letters_1 = count_letters(hand1)
    letters_2 = count_letters(hand2)
    # find the maximum number of letters
    max_1 = max(letters_1.values())
    max_2 = max(letters_2.values())

    # check max letters wins
    if max_1 > max_2:
        return True
    elif max_1 < max_2:
        return False

    # check length of letters. if minor means more cards of the same type
    elif len(letters_1) < len(letters_2):
        return True
    elif len(letters_1) > len(letters_2):
        return False

    # It means they have the same type of hand. Check the highest card starting from 0
    for h1, h2 in zip(hand1, hand2):
        if cards_map[h1] > cards_map[h2]:
            return True
        elif cards_map[h1] < cards_map[h2]:
            return False

    print("ERROR", hand1, hand2)


def order_hands(hands):
    """Orders the hands from strongest to weakest"""
    result = []
    for hand in hands:
        mano, bid = hand.strip().split(" ")
        i = 0
        actual_result_len = len(result)
        while i < len(result) and actual_result_len == len(result):
            if hand_compare(mano, result[i][0]):
                result.insert(i, (mano, bid))
            i += 1

        if actual_result_len == len(result):
            result.append((mano, bid))

    return result


# result = order_hands(hands)

# solution1 = 0
# max_mul = len(result)
# for i, hand in enumerate(result):
#     solution1 += int(hand[1]) * (max_mul - i)

# print("Solution 1:", solution1)
