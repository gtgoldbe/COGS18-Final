import functions

snake_1 = functions.Snake()
snake_2 = functions.Snake()
snake_3 = functions.Snake()
manager_1 = functions.game_manager(6)
manager_2 = functions.game_manager(6)


def test_make_move():
    snake_1.make_move('s')
    snake_1.make_move('d')
    assert snake_1.get_head() == [1,1]
    assert snake_1.pos == [[1,1]]
    snake_1.make_move('a')
    snake_1.make_move('w')
    assert snake_1.get_head() == [0,0]
    assert snake_1.pos == [[0,0]]

def test_eat():
    snake_2.make_move('s')
    snake_2.eat()
    snake_2.make_move('d')
    assert snake_2.pos == [[1,1],[0,1]]


def test_check_alive():
    manager_1.player_snake.make_move('w')
    assert manager_1.check_alive() == False
    manager_2.player_snake.make_move('d')
    manager_2.player_snake.eat()
    manager_2.player_snake.make_move('d')
    manager_2.player_snake.eat()
    manager_2.player_snake.make_move('a')
    assert manager_2.check_ate_yourself() == True
     