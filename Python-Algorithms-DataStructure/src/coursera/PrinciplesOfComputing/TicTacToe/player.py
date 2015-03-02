'''
Created on 2015-03-02

https://class.coursera.org/principlescomputing1-002/assignment/view?assignment_id=7
'''

"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui  # @UnresolvedImport
import poc_ttt_provided as provided  # @UnresolvedImport

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 100        # Number of trials to run
SCORE_CURRENT = 1.0  # Score for squares played by the current player
SCORE_OTHER = 1.0    # Score for squares played by the other player
    
# Add your functions here.

def mc_trial(board, player):
    """
    Play a game starting with the given player by making random moves alternating between players
    The object of board needs to be changed through reference
    """
    next_player = player
    while True:
        # The trial game should be ended
        if board.check_win() is not None:
            break
        # There is still place to move
        empty_cell_list = board.get_empty_squares()
        cell_index = 0
        if len(empty_cell_list) > 1:
            cell_index = random.randrange(0, len(empty_cell_list))
        board.move(empty_cell_list[cell_index][0], empty_cell_list[cell_index][1], next_player)
        # Change the player
        next_player = provided.switch_player(next_player)

def mc_update_scores(scores, board, player):
    """
    Score the completed board and update the scores grid
    """
    # Here the game must be ended
    # There is something to do only if the game is not a draw
    machine_player = player
    human_player = provided.switch_player(machine_player)
    # Assumes that the machine player wins the game
    machine_player_score_adjustment = SCORE_CURRENT
    human_player_score_adjustment = -SCORE_OTHER
    game_status = board.check_win()
    # The game cannot be a draw if score needs to be modified
    if game_status != provided.DRAW:
        # In case the machine player fails
        if game_status != machine_player:
            machine_player_score_adjustment = -SCORE_CURRENT
            human_player_score_adjustment = SCORE_OTHER
        for row in range(board.get_dim()):
            for col in range(board.get_dim()):
                # The value from square is a number, not a string ("X" or "O" or "")
                cell_value = board.square(row, col)
                if cell_value == machine_player:
                    scores[row][col] += machine_player_score_adjustment
                elif cell_value == human_player:
                    scores[row][col] += human_player_score_adjustment
                else:
                    scores[row][col] += 0.0

def get_best_move(board, scores):
    """
    Find all of the empty squares with the maximum score
    Randomly return one of them as a (row, column) tuple
    """
    empty_cell_list = board.get_empty_squares()
    # Full
    if len(empty_cell_list) == 0:
        return None
    # One available cell
    elif len(empty_cell_list) == 1:
        return empty_cell_list[0]
    # Multiple cells
    else:
        score_recorder = dict()
        max_score = scores[empty_cell_list[0][0]][empty_cell_list[0][1]]
        score_recorder[max_score] = [empty_cell_list[0]]
        # Find max score in O(n)
        for index in range(1, len(empty_cell_list)):
            current_score = scores[empty_cell_list[index][0]][empty_cell_list[index][1]]
            if current_score in score_recorder:
                score_recorder[current_score].append(empty_cell_list[index])
            else:
                score_recorder[current_score] = [empty_cell_list[index]]
            if current_score > max_score:
                max_score = current_score
        max_score_cell_list = score_recorder[max_score]
        # One cell with max score
        if len(max_score_cell_list) == 1:
            return max_score_cell_list[0]
        # Multiple cells with max scores
        else:
            return max_score_cell_list[random.randrange(0, len(max_score_cell_list))]

def mc_move(board, player, trials):
    """
    Use the Monte Carlo simulation
    Return a move for the machine player in the form of a (row, column) tuple
    """
    machine_player = player
    # Create the scores grid
    total_score = [[0.0 for dummy_col in range(board.get_dim())] for dummy_row in range(board.get_dim())]
    # Monte Carlo
    while trials > 0:
        new_board = board.clone()
        mc_trial(new_board, machine_player)
        mc_update_scores(total_score, new_board, machine_player)
        trials -= 1
    return get_best_move(board, total_score)

# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.

# provided.play_game(mc_move, NTRIALS, False)        
# poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)

if __name__ == '__main__':
    pass