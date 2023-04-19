from Generators import *
from Game import *
from unittest import TestCase


class GeneratorTest(TestCase):

    '''
        Generator Tests
    '''
    def test_pokemon(self):
        index = random.randint(1, 807)
        pokemon = generate_pokemon_from_index(index)

        index = pokemon.index
        name = pokemon.name
        _type = pokemon.type.name.lower()
        hp = pokemon.base_hp
        attack = pokemon.base_attack
        defense = pokemon.base_defense
        sp_attack = pokemon.base_special_attack
        sp_defense = pokemon.base_special_defense
        speed = pokemon.base_speed

        # Check values against data frames
        p = global_pokemon_frame.loc[global_pokemon_frame['id'] == index]
        s = global_stat_frame.loc[global_stat_frame['pokemon_id'] == index]
        #m = moveset_list.loc[moveset_list['pokemon_id'] == index]
        #m = move_list.loc[move_list['id'].isin(m['move_id'])]



        assert name == p['identifier'].values[0]
        assert _type == TYPES(global_type_frame.loc[global_type_frame['pokemon_id'] == index]['type_id'].values[0]).name.lower()
        assert hp == int(s.loc[s['stat_id'] == STATS.HP.value]['base_stat'].values[0])
        assert attack == int(s.loc[s['stat_id'] == STATS.ATTACK.value]['base_stat'].values[0])
        assert defense == int(s.loc[s['stat_id'] == STATS.DEFENSE.value]['base_stat'].values[0])
        assert sp_attack == int(s.loc[s['stat_id'] == STATS.SPECIAL_ATTACK.value]['base_stat'].values[0])
        assert sp_defense == int(s.loc[s['stat_id'] == STATS.SPECIAL_DEFENSE.value]['base_stat'].values[0])
        assert speed == int(s.loc[s['stat_id'] == STATS.SPEED.value]['base_stat'].values[0])
    def test_move(self):
        # Test valid index
        index = random.randint(1, 100)
        move = generate_move_from_index(index)
        assert isinstance(move, Move), f"Move is {move} but should be a Move object"
        assert move.index == index, f"Move index is {move.index} but should be {index}"
        assert move.name == global_move_frame.loc[global_move_frame['id'] == index, 'identifier'].iloc[0] , \
            f"Move name is {move.name} but should be {global_move_frame.loc[global_move_frame['id'] == index, 'identifier'].iloc[0]}"
        assert move.type == TYPES(global_move_frame.loc[global_move_frame['id'] == index, 'type_id'].iloc[0]) , \
            f"Move type is {move.type} but should be {TYPES(global_move_frame.loc[global_move_frame['id'] == index, 'type_id'].iloc[0])}"
        assert move.power == global_move_frame.loc[global_move_frame['id'] == index, 'power'].iloc[0] , \
            f"Move power is {move.power} but should be {global_move_frame.loc[global_move_frame['id'] == index, 'power'].iloc[0]}"
        assert move.accuracy == global_move_frame.loc[global_move_frame['id'] == index, 'accuracy'].iloc[0] , \
            f"Move accuracy is {move.accuracy} but should be {global_move_frame.loc[global_move_frame['id'] == index, 'accuracy'].iloc[0]}"
        assert move.pp == global_move_frame.loc[global_move_frame['id'] == index, 'pp'].iloc[0] , \
            f"Move pp is {move.pp} but should be {global_move_frame.loc[global_move_frame['id'] == index, 'pp'].iloc[0]}"
        assert move.category == CATEGORY(global_move_frame.loc[global_move_frame['id'] == index, 'damage_class_id'].iloc[0]) , \
            f"Move category is {move.category} but should be {CATEGORY(global_move_frame.loc[global_move_frame['id'] == index, 'damage_class_id'].iloc[0])}"
        pass
    def test_new_player(self):
        name = 'chey'
        player = new_player(name)
        assert player.name == name, f"Player name is {player.name} but should be {name}"

        assert player.current_pokemon == player.pokemon_list[0], \
        f"Player current pokemon is {player.current_pokemon} but should be {player.pokemon_list[0]}"

        assert len(player.pokemon_list) <= BAG_SIZE, \
            f"Player pokemon list size is {len(player.pokemon_list)} but should be less than or equal to {BAG_SIZE}"

        for pokemon in player.pokemon_list:

            index = pokemon.index
            p = global_pokemon_frame.loc[global_pokemon_frame['id'] == index]
            s = global_stat_frame.loc[global_stat_frame['pokemon_id'] == index]

            assert pokemon.name == p['identifier'].values[0], \
                f"Pokemon name is {pokemon.name} but should be {p['identifier'].values[0]}"
            assert pokemon.type.name.lower() == TYPES(global_type_frame.loc[global_type_frame['pokemon_id'] == index]['type_id'].values[0]).name.lower(), \
                f"Pokemon type is {pokemon.type} but should be {TYPES(global_type_frame.loc[global_type_frame['pokemon_id'] == index]['type_id'].values[0]).name.lower()}"
            assert pokemon.base_hp == int(s.loc[s['stat_id'] == STATS.HP.value]['base_stat'].values[0]), \
                f"Pokemon hp is {pokemon.hp} but should be {int(s.loc[s['stat_id'] == STATS.HP.value]['base_stat'].values[0])}"
            assert pokemon.base_attack == int(s.loc[s['stat_id'] == STATS.ATTACK.value]['base_stat'].values[0]), \
                f"Pokemon attack is {pokemon.attack} but should be {int(s.loc[s['stat_id'] == STATS.ATTACK.value]['base_stat'].values[0])}"
            assert pokemon.base_defense == int(s.loc[s['stat_id'] == STATS.DEFENSE.value]['base_stat'].values[0]), \
                f"Pokemon defense is {pokemon.defense} but should be {int(s.loc[s['stat_id'] == STATS.DEFENSE.value]['base_stat'].values[0])}"
            assert pokemon.base_special_attack == int(s.loc[s['stat_id'] == STATS.SPECIAL_ATTACK.value]['base_stat'].values[0]), \
                f"Pokemon sp_attack is {pokemon.sp_attack} but should be {int(s.loc[s['stat_id'] == STATS.SPECIAL_ATTACK.value]['base_stat'].values[0])}"
            assert pokemon.base_special_defense == int(s.loc[s['stat_id'] == STATS.SPECIAL_DEFENSE.value]['base_stat'].values[0]), \
                f"Pokemon sp_defense is {pokemon.sp_defense} but should be {int(s.loc[s['stat_id'] == STATS.SPECIAL_DEFENSE.value]['base_stat'].values[0])}"
            assert pokemon.base_speed == int(s.loc[s['stat_id'] == STATS.SPEED.value]['base_stat'].values[0]), \
                f"Pokemon speed is {pokemon.speed} but should be {int(s.loc[s['stat_id'] == STATS.SPEED.value]['base_stat'].values[0])}"






