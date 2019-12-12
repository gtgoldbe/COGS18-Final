import random
import time
import sys
from IPython.display import clear_output

#Dictionary for all constants
const = {
    'head_char' : '@', 
    'body_char' : '0', 
    'grid_char' : '*',
    'food_char' : 'F',
    'up'        : 'w',
    'down'      : 's',
    'left'      : 'a',
    'right'     : 'd',
    'invalid'   : 'Not Valid',
    'half_divisor' : 2,
    'time'      : 0.3,
    'wait_time' : 0.5,
    '6*6_board' : 6,
    '8*8_board' : 8,
    'win_message' : 'You Win!',
    'AI_win_message' : 'AI Won!',
    'input_message' : 'Enter w,a,s,d to move: ',
    'invalid_message' : 'Enter a valid command...',
    'death_message' : 'You Died... Final Score: ',
    'death_condition1' : 'From running into top/left...',
    'death_condition2' : 'From running into bottom/right...',
    'death_condition3' : 'From eating yourself...', 
    }

#Below are the Hamiltonian Cycles the AI follows to beat Snake


#For a 16x16 board
hamiltonian_cycle_16 = [const['down'],const['down'],const['right'],
                    const['right'],const['right'],const['down'],const['left'],
                    const['left'],const['left'],const['down'],const['right'],
                    const['right'],const['right'],const['down'],const['left'],
                    const['left'],const['left'],const['down'],const['down'],
                    const['right'],const['up'],const['right'],const['right'],
                    const['down'],const['left'],const['down'],const['left'],
                    const['left'],const['down'],const['right'],const['right'],
                    const['right'],const['up'],const['right'],const['down'],
                    const['down'],const['left'],const['left'],const['left'],
                    const['left'],const['down'],const['right'],const['right'],
                    const['right'],const['right'],const['down'],const['left'],
                    const['left'],const['left'],const['left'],const['down'],
                    const['down'],const['down'],const['right'],const['up'],
                    const['up'],const['right'],const['down'],const['down'],
                    const['right'],const['up'],const['up'],const['right'],
                    const['down'],const['down'],const['right'],const['up'],
                    const['up'],const['up'],const['up'],const['up'],
                    const['up'],const['up'],const['up'],const['left']
                    ,const['up'],const['up'],const['up'],const['up'],
                    const['up'],const['right'],const['down'],const['down'],
                    const['down'],const['down'],const['right'],const['down'],
                    const['right'],const['right'],const['down'],const['left'],
                    const['left'],const['down'],const['right'],const['right'],
                    const['down'],const['left'],const['left'],const['down'],
                    const['down'],const['right'],const['up'],const['right'],
                    const['down'],const['down'],const['left'],const['left'],
                    const['down'],const['down'],const['right'],const['up'],
                    const['right'],const['down'],const['right'],const['up'],
                    const['up'],const['up'],const['up'],const['up'],
                    const['up'],const['up'],const['up'],const['right'],
                    const['right'],const['right'],const['down'],const['left'],
                    const['left'],const['down'],const['right'],const['right'],
                    const['down'],const['left'],const['left'],const['down'],
                    const['right'],const['right'],const['down'],const['left'],
                    const['left'],const['down'],const['down'],const['down'],
                    const['right'],const['up'],const['up'],const['right'],
                    const['down'],const['down'],const['right'],const['right'],
                    const['right'],const['up'],const['left'],const['left'],
                    const['up'],const['right'],const['right'],const['up'],
                    const['up'],const['left'],const['down'],const['left'],
                    const['up'],const['up'],const['right'],const['right'],
                    const['up'],const['up'],const['left'],const['down'],
                    const['left'],const['up'],const['up'],const['right'],
                    const['right'],const['up'],const['up'],const['left'],
                    const['down'],const['left'],const['up'],const['left'],
                    const['down'],const['left'],const['left'],const['left'],
                    const['left'],const['left'],const['up'],const['left'],
                    const['up'],const['up'],const['up'],const['right'],
                    const['down'],const['down'],const['right'],const['down'],
                    const['right'],const['right'],const['right'],const['up'],
                    const['right'],const['right'],const['right'],
                    const['right'],const['up'],const['left'],const['left'],
                    const['left'],const['left'],const['left'],const['down'],
                    const['left'],const['up'],const['left'],const['up'],
                    const['right'],const['right'],const['right'],
                    const['right'],const['right'],const['right'],
                    const['right'],const['up'],const['up'],const['left'],
                    const['down'],const['left'],const['up'],const['left'],
                    const['down'],const['left'],const['up'],const['left'],
                    const['down'],const['left'],const['up'],const['left'],
                    const['down'],const['left'],const['up'],const['left'],
                    const['down'],const['left'],const['up'],const['left'],
                    const['down'],const['left'],const['up'],const['left'],
                    const['down'],const['left'],const['up'],const['left']]

class Snake():
    """Creates the player and contains all utility for player.

    Attributes:
        previous_tail    previous location of the end of the snake.
    """
        
    previous_tail = [0,0]

    def __init__(self):
        """Constructor for player, initializes starting position as top left
        of the board.
        """

        start = [0,0]
        self.pos = [start]

    def make_move(self, direct):
        """Contains logic for moving snake.

            Parameters:
            direct (String): direction to move.

            Returns:
            String: If move was invalid.
        """

        next_move = self.get_move(direct)

        #Checks if move was invalid
        if next_move == const['invalid']:
            return next_move

        else:
            #moves snake in direction of direct and removes end of snake
            self.pos.insert(0, next_move)
            self.previous_tail = self.pos.pop()
            return

    def eat(self):
        """Contains logic for growing snake when eating food."""

        copy = self.pos[len(self.pos) - 1]
        self.pos.append(copy)

    def get_head(self):
        """Accesses position of snake head.
           
           Returns:
           list: head position.
        """

        return self.pos[0]

    def get_tail(self):
        """Accesses position of snake tail.

           Returns:
           list: tail position.
        """

        return self.previous_tail

    def get_neck(self):
        """Accesses position of second position of snake.
           
           Returns:
           list: neck position.
        """

        if len(self.pos) > 1:
            return self.pos[1]

        return

    def get_move(self, direction):
        """Contains logic for moving snake in inputted direction.

            Parameters:
            direction (String): direction to move snake.

            Returns:
            List: new coordinate for snake head.
            String: if move was invalid.
        """

        #Copy current head position to temp value
        new_cord_x = self.get_head()[0]
        new_cord_y = self.get_head()[1]

        new_cord = [new_cord_x, new_cord_y]

        #change new_cord to reflect inputted movement
        if direction == const['up']:
            new_cord[1] -= 1

        elif direction == const['down']:
            new_cord[1] += 1

        elif direction == const['left']:
            new_cord[0] -= 1

        elif direction == const['right']:
            new_cord[0] += 1

        else:
            return const['invalid']

        return new_cord

    def print_snake(self):
        """Prints out all coordinates snake currently occupies."""

        for i in self.pos:
            print(i[0])
            print(i[1])
    
class Grid():
    """Contains all logic for creating and changing values of the game grid.

        Attributes:
            size    The size of the board.
            game_grid   List of List of chars for board.
    """

    size = 0
    game_grid = []

    def __init__(self, board_size):
        """Creates game board and initializes player and food starting positions.

            Parameters:
            board_size (int): size of the game board.
        """

        size = 0
        self.game_grid = []

        #Outer while loop creates columns of the grid
        while size < board_size:
            row = []
            self.size = 0

            #Inner loop creates rows for each column
            while self.size < board_size:
                row.append(const['grid_char'])
                self.size += 1

            self.game_grid.append(row)
            size += 1

        #Initialize starting locations of player(top left) and food(middle)
        self.game_grid[0][0] = const['head_char']
        self.game_grid[int(board_size / const['half_divisor'])][int(board_size 
        / const['half_divisor'])] = const['food_char']

    def print_grid(self):
        """Prints grid in readable format."""

        print('\n'.join([' '.join(it) for it in self.game_grid]))

    def change_char_h(self, x, y):
        """Changes value of grid to snake head.

            Parameters:
            x (int): x-coordinate of new head.
            y (int): y-coordinate of new head.
        """

        self.game_grid[y][x] = const['head_char']
    
    def change_char_b(self, x, y):
        """Changes value of grid to snake body.

            Parameters:
            x (int): x-coordinate of new body.
            y (int): y-coordinate of new body.
        """

        self.game_grid[y][x] = const['body_char']

    def change_char_g(self, x, y):
        """Changes value of grid to empty space.

            Parameters:
            x (int): x-coordinate of new empty space.
            y (int): y-coordinate of new empty space.
        """

        self.game_grid[y][x] = const['grid_char']

    def change_char_f(self, x, y):
        """Changes value of grid to food.

            Parameters:
            x (int): x-coordinate of new food.
            y (int): y-coordinate of new food.
        """

        self.game_grid[y][x] = const['food_char']

class game_manager():
    """Contains all logic for running the game.

        Atributes:
        game_size (int): size of the board.
        player_snake (Snake): initializes player
        wait_time (int): Turns until next food spawns
        player_score (int): Tracks length of snake
        hamilton_counter (int): Tracks position of AI in board
        s_time (float): starting time of AI
        hamiltonian_cycle (list): AI behavior
    """

    game_size = 0
    player_snake = Snake()
    food_coord = []
    wait_time = -1
    player_score = 0
    hamilton_counter = 0
    s_time = time.time()
    hamiltonian_cycle = []

    def __init__(self, game_size):
        """game_manager constructor, initializes starting food position and
        grid size based on input.

            Parameters:
                game_size (int): the size of the game board
        """
        self.game_size = game_size

        self.food_coord = [int(self.game_size / const['half_divisor']),
        int(self.game_size / const['half_divisor'])]

        self.game_board = Grid(game_size)

    def play_game(self):
        """Runs Game for human player. Conitninually runs until death of
           player or victory.
        """

        #initializes variable to check if input is valid
        was_valid = True

        #Initializes variable to determine if game is over
        game_over = False

        

        #To prevent Jupyter Notebook from crashing
        time.sleep(.5)
        
        #print and update score and game board each turn
        clear_output(True)
        print(self.player_score)
        self.update_board()
        self.game_board.print_grid()
        
        move = input(const['input_message'])

        #used for delaying food spawns
        if self.wait_time > 0:
            self.wait_time -= 1
    
        #move snake and check if move was valid
        if self.player_snake.make_move(move) == const['invalid']:
            print(const['invalid_message'])
            time.sleep(1)
            was_valid = False
        
        #following conditions only run if move was valid...
        if was_valid and not self.check_alive():
            print(const['death_message'], self.player_score)
            return            

        if was_valid and self.check_ate_food():
            self.player_score += 1

            #delay next food spawn by 1 turn
            self.wait_time = 1
        
        if was_valid and self.wait_time == 0:
            #reset wait time and create next food
            self.wait_time = -1
            self.spawn_food()
            self.game_board.change_char_f(self.food_coord[0], 
                self.food_coord[1])

        #Checks if player won
        if self.player_score >= self.game_size**const['half_divisor'] -1:
            print(const['win_message'])
            game_over = True
        
        #Continue to next turn if game is not over
        if not game_over:
            self.play_game()

    def play_ai_game(self):
        """Runs game for AI player."""

        #Runs until AI has won, AI will never lose
        while not self.player_score == self.game_size**const[
            'half_divisor'] - 1:
            #time.sleep(.03)
            self.play_the_game()
            
        #Update/print board last time to reflect last move of game
        clear_output(True)
        print('\n')
        self.update_board()
        self.game_board.print_grid()

        #End of game actions
        print(const['AI_win_message'])
        f_time = time.time()

        #determine speed of AI in winning game
        print(f_time - self.s_time)
        
    def play_the_game(self):
        """Similar to play_game, instead of asking for input, determines next 
           move based on hamiltonian cycle used by AI.
        """

        #Update/print board each turn
        print('\n')
        clear_output(True)
        self.update_board()
        self.game_board.print_grid()
        
        #checks whether to reset hamiltonianCounter
        if self.hamilton_counter >= self.game_size**const['half_divisor']:
            self.hamilton_counter = 0

        #gets move from AI
        move = hamiltonian_cycle_16[self.hamilton_counter]

        if self.wait_time > 0:
            self.wait_time -= 1
    
        self.player_snake.make_move(move) 
           
        #Check if AI has died, should never occur with proper 
        #hamiltonian cycle
        if not self.check_alive():
            print(const['death_message'], self.player_score)
            return            

        #Following is same as play_game...
        if self.check_ate_food():
            self.player_score += 1
            self.wait_time = 1
        
        if self.wait_time == 0:
            self.wait_time = -1
            self.spawn_food()
            self.game_board.change_char_f(self.food_coord[0], 
                self.food_coord[1])
       
       #update AI position in cycle
        self.hamilton_counter += 1

    def check_alive(self):
        """Checks if player is still alive.

            Returns:
            boolean: If player is still alive.
        """
        head = self.player_snake.get_head()

        #check if player ran into top or left walls
        if head[0] < 0 or head[1] < 0:
            print(const['death_condition1'])
            return False

        #check if player ran into bottom or right walls
        elif head[1] >= self.game_board.size or head[
            0] >= self.game_board.size:
            print(const['death_condition2'])
            return False

        #check if player ate themselves
        elif self.check_ate_yourself():
            print(const['death_condition3'])
            return False

        return True

    def check_ate_yourself(self):
        """Checks if the player moved into a part of their body, thus kiling
        themselves.

            Returns:
            boolean: whether any position in snake overlapps another part 
                     of snake.
        """
        #check count of all snake coordinates
        for i in self.player_snake.pos:

            if self.player_snake.pos.count(i) > 1:
                return True

        return False

    def check_ate_food(self):
        """Checks if player ate food and updates snake to eat food and grow
        by one length.

            Returns:
            boolean: if player moved into food.
        """

        if self.player_snake.get_head() == self.food_coord:
            self.player_snake.eat()
            return True

        return False

    def spawn_food(self):
        """Spawns a new food at an unoccupied location."""

        valid = False

        #keeps generating a random coordinate until it finds an 
        #unoccupied position
        while not valid:
            new_loc_X = random.randint(0,self.game_size - 1)
            new_loc_Y = random.randint(0,self.game_size - 1)
            new_loc = [new_loc_X, new_loc_Y]

            if not self.player_snake.pos.count(new_loc) > 0:
                valid = True

        self.food_coord = new_loc

    def update_board(self):
        """Updates all aspects of board and changes board chars to reflect new
        positions.
        """

        face = self.player_snake.get_head()
        tail = self.player_snake.get_tail()

        self.game_board.change_char_h(face[0],face[1])
        self.game_board.change_char_g(tail[0],tail[1])
        
        if len(self.player_snake.pos) > 1:
            second = self.player_snake.get_neck()
            self.game_board.change_char_b(second[0],second[1])
