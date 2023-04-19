from enum import Enum
from math import floor


import pandas as pd

'''
    Global lists of all pokemon, moves, movesets, types, and stats, used to create pokemon
'''

BAG_SIZE = 3

# a list of all available pokemon, contains Index, Name #height, weight,base_xp
global_pokemon_frame = pd.read_csv('Files/Pokemon/pokemon.csv')

# a list of all avalible moves
global_move_frame = pd.read_csv('Files/Moves/moves.csv')

# a list of all movesets, pokeid to be crossed with move id in move_list
global_moveset_frame = pd.read_csv('Files/Pokemon/pokemon_moves.csv')

# a list of Pokemon and their types
global_type_frame = pd.read_csv('Files/Pokemon/pokemon_types.csv')

# a list of pokemons stats by id, with effort, base
global_stat_frame = pd.read_csv('Files/Pokemon/pokemon_stats.csv')

def is_valid_pokemon_entry(pokemon): # this can probaly be refacotred out
    if isinstance(pokemon, int):
        if 0 < int(pokemon) < 802:
            return True

    if pokemon.lower() in global_pokemon_frame['identifier'].values:
        return True

    return False


'''
    Enumerations for the different types of moves, and the different stats
'''

class STATUS(Enum):
    BURN = 1
    FREEZE = 2
    PARALYSIS = 3
    POISON = 4
    SLEEP = 5
    CONFUSION = 6
    FROZEN_SOLID = 7
    PARALYZED = 8
    POISONED = 9
    ASLEEP = 10
    CONFUSED = 11
    NORMAL = 12
class STATS(Enum):
    HP = 1
    ATTACK = 2
    DEFENSE = 3
    SPECIAL_ATTACK = 4
    SPECIAL_DEFENSE = 5
    SPEED = 6
    ACCURACY = 7
    EVASION = 8
class TYPES(Enum):
    NORMAL = 1
    FIGHTING = 2
    FLYING = 3
    POISON = 4
    GROUND = 5
    ROCK = 6
    BUG = 7
    GHOST = 8
    STEEL = 9
    FIRE = 10
    WATER = 11
    GRASS = 12
    ELECTRIC = 13
    PSYCHIC = 14
    ICE = 15
    DRAGON = 16
    DARK = 17
    FAIRY = 18
class CATEGORY(Enum):
    STATUS = 1
    PHYSICAL = 2
    SPECIAL = 3

'''
    Pokemon class, contains all the information about a pokemon, and the methods to interact with it
'''

class Pokemon():
    def __init__(self, name, index, type,level, base_attack, base_special_attack, base_defense, base_special_defense,
                 base_speed, base_hp):
        self.name = name
        self.index = index
        self.level = level
        self.base_attack = base_attack
        self.base_special_attack = base_special_attack
        self.base_defense = base_defense
        self.base_special_defense = base_special_defense
        self.base_speed = base_speed
        self.base_hp = base_hp
        self.type = type

        self.status = STATUS.NORMAL

        self.IV, self.EV, self.N = 1, 1, 1 # i think ev may actually come from the move itself, n is nature

        self.max_hp = floor(0.01 * (2 * self.base_hp + self.IV + floor(0.25 * self.EV)) * self.level) + self.level + 10.
        self.attack = floor(floor((2 * self.base_attack + self.IV + self.EV) * self.level / 100 + 5) * self.N)
        self.special_attack = floor(floor((2 * self.base_special_attack + self.IV + self.EV) * self.level / 100 + 5) * self.N)
        self.defense = floor(floor((2 * self.base_defense + self.IV + self.EV) * self.level / 100 + 5) * self.N)
        self.special_defense = floor(floor((2 * self.base_special_defense + self.IV + self.EV) * self.level / 100 + 5) * self.N)
        self.speed = floor(floor((2 * self.base_speed + self.IV + self.EV) * self.level / 100 + 5) * self.N)

        self.current_hp = self.max_hp
        self.moves = []

    def is_fainted(self):
        if self.current_hp <= 0:
            return True
        return False

    def add_move(self, move):
        self.moves.append(move)

    def __str__(self):
        return self.name

    def __print__(self):
        print('Name: ' + self.name, 'Index: ' + str(self.index), 'Level: ' + str(self.level), 'Type: ' + str(self.type),
                'HP: ' + str(self.current_hp) + '/' + str(self.max_hp), 'Attack: ' + str(self.attack),
                'Special Attack: ' + str(self.special_attack), 'Defense: ' + str(self.defense),
                'Special Defense: ' + str(self.special_defense), 'Speed: ' + str(self.speed), 'Status: ' + str(self.status))
        print(str(self.moves[0]),'Type : ', str(self.moves[0].type), 'Power: ' + str(self.moves[0].power),
                'Accuracy: ' + str(self.moves[0].accuracy), 'PP: ' + str(self.moves[0].pp), 'Category: ' + str(self.moves[0].category),
                str(self.moves[1]),'Type : ', str(self.moves[1].type), 'Power: ' + str(self.moves[1].power),
                'Accuracy: ' + str(self.moves[1].accuracy), 'PP: ' + str(self.moves[1].pp), 'Category: ' + str(self.moves[1].category),
                str(self.moves[2]),'Type : ', str(self.moves[2].type), 'Power: ' + str(self.moves[2].power),
                'Accuracy: ' + str(self.moves[2].accuracy), 'PP: ' + str(self.moves[2].pp), 'Category: ' + str(self.moves[2].category),
                str(self.moves[3]),'Type : ', str(self.moves[3].type), 'Power: ' + str(self.moves[3].power),
                'Accuracy: ' + str(self.moves[3].accuracy), 'PP: ' + str(self.moves[3].pp), 'Category: ' + str(self.moves[3].category))
class Move():
    def __init__(self, name, index, type, power, accuracy, pp, category):
        self.name = name
        self.index = index
        self.type = type
        self.power = power
        self.accuracy = accuracy
        self.pp = pp
        self.category = category
            # target, effect, priority, flags

    def can_use(self):
        if self.pp > 0:
            return True
        return False

    def __str__(self):
        return self.name
class Trainer():
    def __init__(self, name):
        self.name = name
        self.pokemon_list = []
        self.current_pokemon = Pokemon
        #self.potions
        #self.pokeballs
        #self.money

    def is_out_of_pokemon(self):
        for pokemon in self.pokemon_list:
            if not pokemon.is_fainted():
                return False
        return True


    '''
        menu for selecting pokemon, sets current pokemon to the selected pokemon
    '''

    def add_pokemon(self, pokemon):
        self.pokemon_list.append(pokemon)
    def set_current_pokemon(self, pokemon):
        # pokemon must be in the list of pokemon
        if pokemon in self.pokemon_list:
            self.current_pokemon = pokemon
        else:
            return False
    def __str__(self):
        return self.name



