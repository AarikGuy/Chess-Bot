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
        
        """
        Every random_move_frequency number of moves, choose a random move if that
        field was populated. This will prevent the bots being stuck in a looping game.
        """
        if (self.random_move_frequency > 0 and self.moves_made % self.random_move_frequency == 0):
            return DoorMatChessBot.choose_move(self, legal_moves, chess_board)
            
        color_to_move = chess_board.turn
        fittest_move_score = -1000000

        if color_to_move == BLACK:
            fittest_move_score = 1000000

        fittest_move = None

        for legal_move in legal_moves:
            chess_board.push(legal_move)

            opponents_legal_moves = self.get_legal_moves_list(chess_board)
            [move, next_move_fitness_score] = self.choose_fittest_move(
                opponents_legal_moves, chess_board, 1, chess_board.turn, self.ply_cutoff
            )

            chess_board.pop()

            if color_to_move == WHITE and fittest_move_score <= next_move_fitness_score:
                fittest_move_score = next_move_fitness_score
                fittest_move = legal_move

            if color_to_move == BLACK and fittest_move_score >= next_move_fitness_score:
                fittest_move_score = next_move_fitness_score
                fittest_move = legal_move

        if (fittest_move is None):
            raise Exception("No fittest move was found!")
        
        return fittest_move

    '''
    Given the state of the board
    and all the available legal moves,
    the method will guess the best legal
    move for the color that's moving
    '''
    def choose_fittest_move(
        self, legal_moves: list, chess_board: Board, ply_count: int, color_to_move, ply_cutoff: int
    ):
        self.call_counter += 1
        fittest_move = None
        color_to_move_fitness_score = self.get_default_fitness_score(color_to_move)

        '''
        For all the possible legal moves
        that this player can make, push
        that move on to the chess board,
        then look at the opponents best response.
        Choose the move where this player's
        fitness score that has the biggest increase 
        (or lowest difference if losing).
        '''
        for legal_move in legal_moves:
            chess_board.push(legal_move)

            '''
            If a checkmate is found, break
            out of the method and indicate
            with indiciation that it's the
            optimal move, no need to continue
            '''
            if (chess_board.is_checkmate()):
              max_fitness = 1000000 if color_to_move == WHITE else -1000000 
              chess_board.pop()
              return [legal_move, max_fitness]

            '''
            Play cutoff makes sure that this function doesn't run forever.
            The base case, grab the fitness state of the game board to 
            assess who's winning in this position.
            '''
            if ply_count >= ply_cutoff:
                [white_fitness_score, black_fitness_score] = self.get_fitness_scores(
                    chess_board
                )

                next_move_fitness_score = white_fitness_score - black_fitness_score

                if (color_to_move == WHITE and next_move_fitness_score >= color_to_move_fitness_score):
                   color_to_move_fitness_score = next_move_fitness_score 
                   fittest_move = legal_move

                if (color_to_move == BLACK and next_move_fitness_score <= color_to_move_fitness_score):
                    color_to_move_fitness_score = next_move_fitness_score
                    fittest_move = legal_move

            else:
                '''
                Recursively finds the best move among all
                the possible moves that could be found 
                '''
                opponents_legal_moves = self.get_legal_moves_list(chess_board)
                next_moves_color = not color_to_move
                
                # Get opponents best response.
                [opponents_best_response, next_move_fitness_score] = (
                    self.choose_fittest_move(
                        opponents_legal_moves,
                        chess_board,
                        ply_count + 1,
                        next_moves_color,
                        ply_cutoff
                    )
                )

                if (color_to_move == WHITE and next_move_fitness_score > color_to_move_fitness_score):
                    color_to_move_fitness_score = next_move_fitness_score
                    fittest_move = legal_move
                
                if (color_to_move == BLACK and next_move_fitness_score < color_to_move_fitness_score):
                    color_to_move_fitness_score = next_move_fitness_score
                    fittest_move = legal_move

            chess_board.pop()

        return [fittest_move, color_to_move_fitness_score]

    '''
    Checks whether or not fitness score
    is deemed better for the side color_to_move
    '''
    def is_move_more_fit(self, color_to_move, color_to_move_fitness_score, next_move_fitness_score):
        if (color_to_move == WHITE and color_to_move_fitness_score >= next_move_fitness_score):
            return True

        if (color_to_move == BLACK and color_to_move_fitness_score <= next_move_fitness_score):
            return True
        
        return False

    def get_default_fitness_score(self, color_to_move):
        if color_to_move == WHITE:
            color_to_move_fitness_score = -1000000
        else:
            color_to_move_fitness_score = 1000000

        return color_to_move_fitness_score
