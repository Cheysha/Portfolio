from Classes import *
from Util import *
from main import *


def generate_pokemon_from_index(index):
    if type(index) == str:
        index = index.lower()
        index = int(global_pokemon_frame.loc[global_pokemon_frame['identifier'] == index]['id'].values[0])

    index = int(index)

    '''
            data frames for our pokemon
    '''
    p = global_pokemon_frame.loc[global_pokemon_frame['id'] == index]

    s = global_stat_frame.loc[global_stat_frame['pokemon_id'] == index]

    m = global_moveset_frame.loc[global_moveset_frame['pokemon_id'] == index]

    m = global_move_frame.loc[global_move_frame['id'].isin(m['move_id'])]

    '''
        setting up our pokemon
    '''
    level = 100
    name = p['identifier'].values[0]
    _type = TYPES(global_type_frame.loc[global_type_frame['pokemon_id'] == index]['type_id'].values[0])

    hp = int(s.loc[s['stat_id'] == STATS.HP.value]['base_stat'].values[0])
    attack = int(s.loc[s['stat_id'] == STATS.ATTACK.value]['base_stat'].values[0])
    defense = int(s.loc[s['stat_id'] == STATS.DEFENSE.value]['base_stat'].values[0])
    sp_attack = int(s.loc[s['stat_id'] == STATS.SPECIAL_ATTACK.value]['base_stat'].values[0])
    sp_defense = int(s.loc[s['stat_id'] == STATS.SPECIAL_DEFENSE.value]['base_stat'].values[0])
    speed = int(s.loc[s['stat_id'] == STATS.SPEED.value]['base_stat'].values[0])

    '''
        creating our pokemon
    '''
    generated_pokemon = Pokemon(name=name, index=index, type=_type, level=level, base_attack=attack, base_special_attack=sp_attack,
                   base_defense=defense, base_special_defense=sp_defense, base_speed=speed, base_hp=hp)

    '''
        adding moves to our pokemon, will need completly redone to use get_move
    '''
    #gets 4 random moves #
    for i in range(4):
        move = generate_move_from_index(m.iloc[i]['id'])
        generated_pokemon.add_move(move)


    ''' 
        returning our pokemon
    '''

    return generated_pokemon
def generate_move_from_index(index):
    # Check if index is a string that can be converted to an integer
    if isinstance(index, str) and index.isdigit():
        index = int(index)

    # Look up move data from move_list
    move_data = global_move_frame.loc[global_move_frame['id'] == index].iloc[0]

    # Create move object
    move = Move(
        name=move_data['identifier'],
        index=move_data['id'],
        type=TYPES(move_data['type_id']),
        power=move_data['power'],
        accuracy=move_data['accuracy'],
        pp=move_data['pp'],
        category=CATEGORY(move_data['damage_class_id'])
    )

    return move
def gen_random_trainer():
        player = Trainer(name='random')
        for i in range(BAG_SIZE):
            player.add_pokemon(generate_pokemon_from_index(random.randint(1, 340)))

        player.set_current_pokemon(player.pokemon_list[0])
        return player
def new_player(name):

    if name == 'random':
        return gen_random_trainer()

    ''' 
        creating a new player
    '''
    player = Trainer(name=name)

    '''
        asking for input
    '''
    i = 0
    while i < BAG_SIZE:
        player_input = input('Enter a Pokemon name: ')

        if player_input.isdigit():
            player_input = int(player_input)

        if player_input == 'random':
            player.add_pokemon(generate_pokemon_from_index(random.randint(1, 340)))
            i += 1

        elif is_valid_pokemon_entry(player_input):
            player.add_pokemon(generate_pokemon_from_index(player_input))
            i += 1

        else:
            print('Invalid Pokemon')

    '''
        return the player
    '''
    player.set_current_pokemon(player.pokemon_list[0])
    return player

