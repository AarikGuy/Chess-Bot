from IChessBot import IChessBot
from DoorMatChessBot import DoorMatChessBot
from chess import Board, WHITE, BLACK


class DunceFishChessBot(DoorMatChessBot):
    def __init__(self, ply_cutoff: int, color=WHITE, random_move_frequency=0):
        DoorMatChessBot.__init__(self)

        self.ply_cutoff = ply_cutoff
        self.color = color
        self.call_counter = 0
        self.moves_made = 0
        self.random_move_frequency = random_move_frequency

    def choose_move(self, legal_moves: list, chess_board: Board):
        self.moves_made += 1
        
        # Every random_move_frequency number of moves
        if (self.random_move_frequency > 0 and self.moves_made % self.random_move_frequency == 0):
            return DoorMatChessBot.choose_move(self, legal_moves, chess_board)
            
        color_to_move = chess_board.turn
        fittest_move_score = -1000000

        if color_to_move == BLACK:
            fittest_move_score = 1000000
        for legal_move in legal_moves:
            chess_board.push(legal_move)
            opponents_legal_moves = self.get_legal_moves_list(chess_board)
            [move, fitness_score] = self.choose_fittest_move(
                opponents_legal_moves, chess_board, 1, chess_board.turn
            )
            chess_board.pop()

            if color_to_move == WHITE and fittest_move_score <= fitness_score:
                fittest_move_score = fitness_score
                fittest_move = legal_move

            if color_to_move == BLACK and fittest_move_score >= fitness_score:
                fittest_move_score = fitness_score
                fittest_move = legal_move

        return fittest_move

    def choose_fittest_move(
        self, legal_moves: list, chess_board: Board, ply_count: int, color_to_move
    ):
        self.call_counter += 1
        color_to_move_fitness_score = 0

        if color_to_move == WHITE:
            color_to_move_fitness_score = -1000000
        else:
            color_to_move_fitness_score = 1000000
        fittest_move = None

        for legal_move in legal_moves:
            chess_board.push(legal_move)
            if ply_count >= self.ply_cutoff:
                [white_fitness_score, black_fitness_score] = self.get_fitness_scores(
                    chess_board
                )
                white_fitness_score = white_fitness_score - black_fitness_score
                if (
                    color_to_move == WHITE
                    and white_fitness_score >= color_to_move_fitness_score
                ):
                    color_to_move_fitness_score = white_fitness_score
                    fittest_move = legal_move

                if (
                    color_to_move == BLACK
                    and white_fitness_score <= color_to_move_fitness_score
                ):
                    color_to_move_fitness_score = white_fitness_score
                    fittest_move = legal_move

            else:
                opponents_legal_moves = self.get_legal_moves_list(chess_board)
                sub_move_color = not color_to_move
                [opponents_best_response, white_fitness_score] = (
                    self.choose_fittest_move(
                        opponents_legal_moves,
                        chess_board,
                        ply_count + 1,
                        sub_move_color,
                    )
                )

                if (
                    color_to_move == WHITE
                    and white_fitness_score >= color_to_move_fitness_score
                ):
                    color_to_move_fitness_score = white_fitness_score
                    fittest_move = legal_move

                if (
                    color_to_move == BLACK
                    and white_fitness_score <= color_to_move_fitness_score
                ):
                    color_to_move_fitness_score = white_fitness_score

            chess_board.pop()

        return [fittest_move, color_to_move_fitness_score]
