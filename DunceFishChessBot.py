from IChessBot import IChessBot
from DoorMatChessBot import DoorMatChessBot
from chess import Board, WHITE, BLACK


class DunceFishChessBot(DoorMatChessBot):

    def __init__(self, ply_cutoff: int):
        self.ply_cutoff = ply_cutoff
        pass

    def choose_move(self, legal_moves: list, chess_board: Board):
        [fittest_move, highest_fitness_score] = self.choose_fittest_move(
            legal_moves, chess_board, 1, chess_board.turn
        )

        return fittest_move

    def choose_fittest_move(
        self, legal_moves: list, chess_board: Board, ply_count: int, bot_color
    ):
        highest_fitness_score = -1000000000
        lowest_fitness_score = 100000000000
        fittest_move = None


        for legal_move in legal_moves:
            chess_board.push(legal_move)

            if ply_count >= self.ply_cutoff:
                [fitness_score_white, fitness_score_black] = self.get_fitness_scores(
                    chess_board
                )
                my_fitness_score = 0
                other_fitness_score = 0

                if bot_color == WHITE:
                    my_fitness_score = fitness_score_white
                    other_fitness_score = fitness_score_black
                else:
                    my_fitness_score = fitness_score_black
                    other_fitness_score = fitness_score_black

                move_fitness_score = my_fitness_score - other_fitness_score

                if move_fitness_score > highest_fitness_score:
                    fittest_move = legal_move
                    highest_fitness_score = move_fitness_score

            else:
                sub_legal_moves = self.get_legal_moves_list(chess_board)
                [fittest_sub_move, highest_sub_fitness_score] = (
                    self.choose_fittest_move(
                        sub_legal_moves, chess_board, ply_count + 1, not bot_color
                    )
                )

                if highest_sub_fitness_score > highest_fitness_score:
                    highest_fitness_score = highest_sub_fitness_score
                    fittest_move = legal_move

            chess_board.pop()

        return [fittest_move, highest_fitness_score]
