'''
Created on 2015-04-18

https://class.coursera.org/principlescomputing2-002/assignment/view?assignment_id=15
'''

"""
Mini-max Tic-Tac-Toe Player
"""

import poc_ttt_provided as provided # @UnresolvedImport

# Set timeout, as mini-max can take a long time
import codeskulptor # @UnresolvedImport
codeskulptor.set_timeout(60)

# SCORING VALUES - DO NOT MODIFY
SCORES = {provided.PLAYERX: 1,
          provided.DRAW: 0,
          provided.PLAYERO: -1}

def mm_move(board, player):
    """
    Make a move on the board.
    
    Returns a tuple with two elements.  The first element is the score
    of the given board and the second element is the desired move as a
    tuple, (row, col).
    """
    # board is currect board
    # player is the player to move next
    # if player is PLAYERX then maximize
    # if player is PLAYERX then minimize
    
    # base case
    status_of_current_board = board.check_win()
    if status_of_current_board is not None:
        return SCORES[status_of_current_board], (-1, -1)
    else:
        # all right my lord we need to do dfs here
        score_card_for_ccurent_level = []
        for every_move in board.get_empty_squares():
            new_board = board.clone()
            new_board.move(every_move[0], every_move[1], player)
            temp_score = mm_move(new_board, provided.switch_player(player))[0], every_move
            if (player == provided.PLAYERX) and (temp_score[0] == SCORES[provided.PLAYERX]):
                return temp_score
            elif (player == provided.PLAYERO) and (temp_score[0] == SCORES[provided.PLAYERO]):
                return temp_score
            score_card_for_ccurent_level.append(temp_score)
        # post-order process
        if player == provided.PLAYERX:
            max_score = -2
            max_move = (-1, -1)
            for every_score in score_card_for_ccurent_level:
                if every_score[0] > max_score:
                    max_score = every_score[0]
                    max_move = every_score[1]
            return max_score, max_move
        else:
            min_score = 2
            min_move = (-1, -1)
            for every_score in score_card_for_ccurent_level:
                if every_score[0] < min_score:
                    min_score = every_score[0]
                    min_move = every_score[1]
            return min_score, min_move

def move_wrapper(board, player, trials):
    """
    Wrapper to allow the use of the same infrastructure that was used
    for Monte Carlo Tic-Tac-Toe.
    """
    move = mm_move(board, player)
    assert move[1] != (-1, -1), "returned illegal move (-1, -1)"
    return move[1]

# Test game with the console or the GUI.
# Uncomment whichever you prefer.
# Both should be commented out when you submit for
# testing to save time.

# provided.play_game(move_wrapper, 1, False)        
# poc_ttt_gui.run_gui(3, provided.PLAYERO, move_wrapper, 1, False)

if __name__ == '__main__':
    pass