from main import *

class Game():

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.turn = 1

    def trainer_turn(self, trainer):

        while trainer.current_pokemon.is_fainted():
            trainer.current_pokemon = self.pokemon_select()
        m = self.move_select()

        return trainer.current_pokemon, m

    '''
        Player 1 turn
    '''

    def pokemon_select(self):
        for i, pokemon in enumerate(self.player1.pokemon_list):
            print(i, pokemon, pokemon.type.name, pokemon.current_hp,'/', pokemon.max_hp, pokemon.status.name,
                  'A: ', pokemon.attack, ' D: ', pokemon.defense, ' SpA: ', pokemon.special_attack,' SpD: ',pokemon.special_defense,
                  'Speed: ', pokemon.speed)

            for move in pokemon.moves:
                print('    ', move.name,' | ','Type: ', move.type.name,' Power: ', move.power,' PP:',  move.pp)

        try:
            option = int(input('player1 input: '))
            if option not in range(len(self.player1.pokemon_list)):
                raise ValueError
        except ValueError:
            print('invalid input')
            return self.pokemon_select()

        if self.player1.pokemon_list[option].is_fainted():
            print('pokemon is fainted')
            return self.pokemon_select()

        return self.player1.pokemon_list[option]
    def move_select(self):
        for i, move in enumerate(self.player1.current_pokemon.moves):
            print('    ', move.name,' | ','Type: ', move.type.name,' Power: ', move.power,' PP:',  move.pp)

        try:
            option = int(input('player1 input: '))
            if option not in range(len(self.player1.current_pokemon.moves)):
                raise ValueError
        except ValueError:
            print('invalid input')
            return self.move_select()

        if not self.player1.current_pokemon.moves[option].can_use():
            print('move is out of pp')
            return self.move_select()

        return self.player1.current_pokemon.moves[option]


    '''
        Player 2 turn
    '''
    def get_player2_input(self):
        pass


    '''
        Game logic
    '''
    def check_game(self):
        # check if either player has no pokemon left
        if self.player1.is_out_of_pokemon():
            print('Player 2 wins!')
            exit()
        elif self.player2.is_out_of_pokemon():
            print('Player 1 wins!')
            exit()
    def do_move(self, *move, defender):
        attacker = move[0][0]
        move = move[0][1]

        if move.category == CATEGORY.PHYSICAL :
            L = attacker.level
            A = attacker.attack# moves will change bd ultimately
            D = defender.defense
            P = move.power
            S = 1.5 if attacker.type == move.type else 1 # STAB
            T = 1 # type effectiveness
            Z = 1 # random number between 0.85 and 1.00

            damage = ((((2 * L) / 5)+2) * P * (A / D)) / 50 + 2 * S * T * Z

        elif move.category == CATEGORY.SPECIAL:
            L = attacker.level
            A = attacker.special_attack  # moves will change bd ultimately
            D = defender.special_defense
            P = move.power
            S = 1.5 if attacker.type == move.type else 1  # STAB
            T = 1  # type effectiveness
            Z = 1  # random number between 0.85 and 1.00

            damage = ((((2 * L) / 5) + 2) * P * (A / D)) / 50 + 2 * S * T * Z

        defender.current_hp -= int(damage)


    def Run(self):
        while True:
            Trainer1 = self.player1
            Trainer2 = self.player2

            # fastest current pokemon goes first
            if Trainer1.current_pokemon.speed > Trainer2.current_pokemon.speed:
                player1_move = self.trainer_turn(Trainer1)
                #player2_move = self.trainer_turn(Trainer2)

                self.do_move(player1_move,defender=Trainer2.current_pokemon)
                #self.do_move(player2_move,defender=self.player1.current_pokemon)
            else:
                #player2_move = self.trainer_turn(Trainer2)
                player1_move = self.trainer_turn(Trainer1)

                #self.do_move(player2_move,defender=self.player1.current_pokemon)
                self.do_move(player1_move,defender=Trainer2.current_pokemon)

            self.check_game()
            self.turn += 1