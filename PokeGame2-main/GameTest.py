from Generators import *
from Game import *
from unittest import TestCase

class GameTests(TestCase):

    trainer1 = Trainer('chey')
    trainer1.add_pokemon(generate_pokemon_from_index(1))
    trainer1.add_pokemon(generate_pokemon_from_index(2))
    trainer1.add_pokemon(generate_pokemon_from_index(3))
    trainer1.current_pokemon = trainer1.pokemon_list[0]

    trainer2 = Trainer('rival')
    trainer2.add_pokemon(generate_pokemon_from_index(4))
    trainer2.add_pokemon(generate_pokemon_from_index(5))
    trainer2.add_pokemon(generate_pokemon_from_index(6))
    trainer2.current_pokemon = trainer2.pokemon_list[0]

    game = Game(trainer1, trainer2)


    '''
          Game tests
    '''

    def test_game_entry(self):
        # assert both players current pokemon have full hp
        assert self.game.player1.current_pokemon.current_hp == self.game.player1.current_pokemon.max_hp, \
            f"Player 1 current pokemon hp is {self.game.player1.current_pokemon.current_hp} but should be {self.game.player1.current_pokemon.max_hp}"
        assert self.game.player2.current_pokemon.current_hp == self.game.player2.current_pokemon.max_hp, \
            f"Player 2 current pokemon hp is {self.game.player2.current_pokemon.current_hp} but should be {self.game.player2.current_pokemon.max_hp}"

        pass


    '''
        Player 1 tests
    '''
    def test_player1_pokemon_select(self):
        temp = self.game.pokemon_select()

        assert temp in self.game.player1.pokemon_list, \
            f"Pokemon {temp} is not in player 1 pokemon list"
        assert temp.current_hp > 0, \
            f"Pokemon {temp} is faint"

        pass

    def test_player1_pokemon_select_faint(self):
        self.game.player1.current_pokemon.current_hp = 0
        temp = self.game.pokemon_select()

        assert temp in self.game.player1.pokemon_list, \
            f"Pokemon {temp} is not in player 1 pokemon list"
        assert temp.current_hp > 0, \
            f"Pokemon {temp} is faint"


    def test_player1_move_select(self):
        temp = self.game.move_select()

        assert temp in self.game.player1.current_pokemon.moves, \
            f"Move {temp} is not in player 1 current pokemon moves"
        assert temp.pp > 0, \
            f"Move {temp} is out of pp"

    def test_player1_move_select_no_pp(self):
        self.game.player1.current_pokemon.moves[0].pp = 0
        temp = self.game.move_select()

        assert temp in self.game.player1.current_pokemon.moves, \
            f"Move {temp} is not in player 1 current pokemon moves"
        assert temp.pp > 0, \
            f"Move {temp} is out of pp"


    def test_pleyer1_turn(self):
        t = self.game.trainer_turn(self.trainer1)

        assert isinstance(t, tuple), \
            f"Player 1 turn is {t} but should be a tuple"

        assert isinstance(t[0], Pokemon), \
            f"Player 1 turn pokemon is {t[0]} but should be a pokemon"
        assert t[0].current_hp > 0, \
            f"Player 1 turn pokemon {t[0]} is faint"

        assert isinstance(t[1], Move), \
            f"Player 1 turn move is {t[1]} but should be a move"
        assert t[1].pp > 0, \
            f"Player 1 turn move {t[1]} is out of pp"

    def test_pleyer1_turn_no_health(self):
        self.game.player1.pokemon_list[0].current_hp = 0
        t = self.game.trainer_turn(self.trainer1)

        assert isinstance(t, tuple), \
            f"Player 1 turn is {t} but should be a tuple"

        assert isinstance(t[0], Pokemon), \
            f"Player 1 turn pokemon is {t[0]} but should be a pokemon"
        assert t[0].current_hp > 0, \
            f"Player 1 turn pokemon {t[0]} is faint"

        assert isinstance(t[1], Move), \
            f"Player 1 turn move is {t[1]} but should be a move"
        assert t[1].pp > 0, \
            f"Player 1 turn move {t[1]} is out of pp"

    def test_pleyer1_turn_no_pp(self):
        #set the pp of all player1 current pokemon moves to 0
        for move in self.game.player1.current_pokemon.moves:
            move.pp = 0
        # a way out of hte test
        self.game.player1.current_pokemon.moves[0].pp = 1

        t = self.game.trainer_turn(self.trainer1)

        assert isinstance(t, tuple), \
            f"Player 1 turn is {t} but should be a tuple"

        assert isinstance(t[0], Pokemon), \
            f"Player 1 turn pokemon is {t[0]} but should be a pokemon"
        assert t[0].current_hp > 0, \
            f"Player 1 turn pokemon {t[0]} is faint"

        assert isinstance(t[1], Move), \
            f"Player 1 turn move is {t[1]} but should be a move"
        assert t[1].pp > 0, \
            f"Player 1 turn move {t[1]} is out of pp"

    '''
        Battle tests
    '''

    #checks to see if the move function is working, and if the damage is correct, contains damage formula
    def test_do_move(self):
        attacker = self.game.player1.current_pokemon
        defender = self.game.player2.current_pokemon
        move = attacker.moves[0]

        initial_health = defender.current_hp

        self.game.do_move(attacker, move, defender=defender)


        if move.category == CATEGORY.PHYSICAL :
            L = attacker.level
            A = attacker.attack# moves will change bd ultimately
            D = defender.defense
            P = move.power
            S = 1.5 if attacker.type == move.type else 1 # STAB
            T = 1 # type effectiveness
            Z = 1 # random number between 0.85 and 1.00

            damage = ((((2 * L) / 5)+2) * P * (A / D)) / 50 + 2 * S * T * Z

            assert initial_health > defender.current_hp, \
                f"Pokemon {defender} did not take damage {initial_health}/{defender.current_hp}"

            assert defender.current_hp == initial_health - damage, \
                f"Pokemon {defender} did not take the correct amount of damage, took {initial_health - defender.current_hp} but should have taken {damage}"

        elif move.category == CATEGORY.SPECIAL:
            L = attacker.level
            A = attacker.special_attack  # moves will change bd ultimately
            D = defender.special_defense
            P = move.power
            S = 1.5 if attacker.type == move.type else 1  # STAB
            T = 1  # type effectiveness
            Z = 1  # random number between 0.85 and 1.00

            damage = ((((2 * L) / 5) + 2) * P * (A / D)) / 50 + 2 * S * T * Z

            assert defender.current_hp == initial_health - damage, \
                f"Pokemon {defender} did not take the correct amount of damage, took {initial_health - defender.current_hp} but should have taken {damage}"

    def test_run(self):
        self.game.Run()



