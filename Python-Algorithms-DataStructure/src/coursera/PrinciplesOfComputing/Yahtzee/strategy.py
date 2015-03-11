'''
Created on 2015-03-02

https://class.coursera.org/principlescomputing1-002/assignment/view?assignment_id=9
'''

"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
"""

# Used to increase the timeout, if necessary
# import codeskulptor
# codeskulptor.set_timeout(20)

def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """
    
    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set

def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: full yahtzee hand

    Returns an integer score 
    """
    # hand is a tuple
    # empty tuple
    if len(hand) == 0:
        return 0
    
    # non-empty tuple
    # Do not assume that the largest value of a single dice is 6
    return max([single_dice * hand.count(single_dice) for single_dice in set(hand)])

def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value based on held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """
    random_rolls = gen_all_sequences(range(1, num_die_sides + 1), num_free_dice)
    result_list = []
    
    for single_roll in random_rolls:
        result_list.append(score(held_dice + single_roll))
    
    return sum(result_list) / float(len(random_rolls))

def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
    
    result_set = set([()])
    # Handle empty condition
    if len(hand) > 0:
        for index in range(0, len(hand)):
            # Do not add the tuple into result_set directly
            # Because this changes the size of the set during interation
            intermediate_result_set = set()
            for every_tuple in result_set:
                new_subset_as_list = list(every_tuple)
                new_subset_as_list.append(hand[index])
                intermediate_result_set.add(tuple(sorted(new_subset_as_list)))
            result_set.update(intermediate_result_set)
    
    return result_set

def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    all_holds = gen_all_holds(hand)
    max_expectation = 0.0
    selected_hold = ()
    for current_hold in all_holds:
        current_expectation = expected_value(current_hold, num_die_sides, len(hand) - len(current_hold))
        if current_expectation > max_expectation:
            max_expectation = current_expectation
            selected_hold = current_hold

    return (max_expectation, selected_hold)

def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    num_die_sides = 6
    hand = (1, 1, 1, 5, 6)
    hand_score, hold = strategy(hand, num_die_sides)
    print("Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score)

if __name__ == '__main__':
    pass