from enums.GameOutcomes import GameOutcomes
from bots.DoorMatChessBot import DoorMatChessBot
from bots.DunceFishChessBot import DunceFishChessBot 
from ChessGame import ChessGame


def test_given_a_white_dunce_fish_and_a_black_door_mat_bot_when_the_two_bots_play_a_game_then_white_should_win_the_game():
    # arrange
    white_bot = DunceFishChessBot(1)
    black_bot = DoorMatChessBot()
    game = ChessGame(white_bot, black_bot)

    # act
    game_outcome = game.have_bots_play()

    # assert
    assert game_outcome == GameOutcomes.WHITE_WON

def test_given_a_white_door_mat_and_a_black_dunce_fish_when_the_two_bots_play_then_black_should_win():
    # arrange
    white_bot = DoorMatChessBot() 
    black_bot = DunceFishChessBot(1)
    
    game = ChessGame(white_bot, black_bot)
    
    # act
    game_outcome = game.have_bots_play()

    # assert
    assert game_outcome == GameOutcomes.BLACK_WON

def test_when_given_a_stronger_white_dunce_fish_and_a_black_dunce_fish_when_the_bots_play_a_game_white_should_win():
    # arrange
    white_bot = DunceFishChessBot(ply_cutoff=2)
    black_bot = DunceFishChessBot(ply_cutoff=1)
    game = ChessGame(white_bot, black_bot)

    # act
    game_outcome = game.have_bots_play()    

    # assert
    assert game_outcome == GameOutcomes.WHITE_WON

def test_given_a_white_dunce_fish_and_a_stronger_black_dunce_fish_when_the_bots_play_a_game_black_should_win():
    # arrange
    white_bot = DunceFishChessBot(ply_cutoff=1)
    black_bot = DunceFishChessBot(ply_cutoff=2) 
    game = ChessGame(white_bot, black_bot)

    # act
    game_outcome = game.have_bots_play()

    # assert
    assert game_outcome == GameOutcomes.BLACK_WON

