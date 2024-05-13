def calculate(attack_type,defense_type_one,defense_type_two,pokemon_types):
    first_multiplier = 0
    second_multiplier = 0
    damage_multiplier = 1
    #0.5 effectiveness 
        
    #python dictonarys
    type = {    'Normal': {'Rock': 0.5, 'Steel': 0.5, 'Ghost': 0},
    'Fighting': {'Normal': 2, 'Flying': 0.5, 'Poison': 0.5, 'Rock': 2, 'Bug': 0.5, 'Ghost': 0,
                 'Steel': 2, 'Psychic': 0.5, 'Ice': 2, 'Dark': 2, 'Fairy': 0.5},
    'Flying': {'Fighting': 2, 'Rock': 0.5, 'Bug': 2, 'Steel': 0.5, 'Grass': 2, 'Electric': 0.5},
    'Poison': {'Poison': 0.5, 'Ground': 0.5, 'Rock': 0.5, 'Ghost': 0.5, 'Steel': 0,
                'Grass': 2, 'Fairy': 2},
    'Ground': {'Flying': 0, 'Poison': 2, 'Rock': 2, 'Bug': 0.5, 'Steel': 2, 'Fire': 2,
                'Grass': 0.5, 'Electric': 2},
    'Rock': {'Flying': 2, 'Ground': 0.5, 'Bug': 2, 'Steel': 0.5, 'Fire': 2, 'Ice': 2},
    'Bug': {'Fighting': 0.5, 'Flying': 0.5, 'Poison': 0.5, 'Ghost': 0.5, 'Steel': 0.5,
             'Fire': 0.5, 'Grass': 2, 'Psychic': 2, 'Dark': 2, 'Fairy': 0.5},
    'Ghost': {'Normal': 0, 'Ghost': 2, 'Psychic': 2, 'Dark': 0.5},
    'Steel': {'Rock': 2, 'Steel': 0.5, 'Fire': 0.5, 'Water': 0.5, 'Electric': 0.5,
               'Ice': 2, 'Fairy': 2},
    'Fire': {'Rock': 0.5, 'Bug': 2, 'Steel': 2, 'Fire': 0.5, 'Water': 0.5, 'Grass': 2,
              'Ice': 2, 'Fairy': 0.5},
    'Water': {'Ground': 2, 'Rock': 2, 'Fire': 2, 'Water': 0.5, 'Grass': 0.5, 'Dragon': 0.5},
    'Grass': {'Flying': 0.5, 'Poison': 0.5, 'Ground': 2, 'Rock': 2, 'Bug': 0.5, 'Steel': 0.5,
               'Fire': 0.5, 'Water': 2, 'Grass': 0.5, 'Dragon': 0.5},
    'Electric': {'Flying': 2, 'Ground': 0, 'Water': 2, 'Grass': 0.5, 'Electric': 0.5, 'Dragon': 0.5},
    'Psychic': {'Fighting': 2, 'Poison': 2, 'Steel': 0.5, 'Psychic': 0.5, 'Dark': 0},
    'Ice': {'Flying': 2, 'Ground': 2, 'Steel': 0.5, 'Fire': 0.5, 'Water': 0.5,
             'Grass': 2, 'Ice': 0.5, 'Dragon': 2},
    'Dragon': {'Steel': 0.5, 'Dragon': 2, 'Fairy': 0},
    'Dark': {'Fighting': 0.5, 'Ghost': 2, 'Psychic': 2, 'Dark': 0.5, 'Fairy': 0.5},
    'Fairy': {'Fighting': 2, 'Poison': 0.5, 'Steel': 0.5, 'Fire': 0.5, 'Dragon': 2, 'Dark': 2}}

    """"
    #normal
    if  (attack_type == pokemon_types[0]and (defense_type_one == pokemon_types[12] or defense_type_one == pokemon_types[16])):
        first_multiplier = 0.5

        
    #fighting
    if (attack_type == pokemon_types[6] and (defense_type_one == pokemon_types[9] or defense_type_one == pokemon_types[7] or 
                                             defense_type_one == pokemon_types[11] or defense_type_one == pokemon_types[10] 
                                             or defense_type_one == pokemon_types[17])):
        pass

    #flying
    if (attack_type == pokemon_types[9] and (defense_type_one == pokemon_types[12] or defense_type_one == pokemon_types[16]
                                              or defense_type_one == pokemon_types[3])):
        pass

    #poison
    if (attack_type == pokemon_types[7] and (defense_type_one == pokemon_types[7] or defense_type_one == pokemon_types[8] 
                                             or defense_type_one == pokemon_types[12] or defense_type_one == pokemon_types[13])):
        pass

    #ground
    if (attack_type == pokemon_types[8] and (defense_type_one == pokemon_types[11] or defense_type_one == pokemon_types[4])):
        pass

    #rock
    if (attack_type == pokemon_types[12] and (defense_type_one == pokemon_types[6] or defense_type_one == pokemon_types[8]
                                                or defense_type_one == pokemon_types[16])):
        pass

    #bug
    if (attack_type == pokemon_types[11] and (defense_type_one == pokemon_types[6] or defense_type_one == pokemon_types[9]
                                               or defense_type_one == pokemon_types[7] or defense_type_one == pokemon_types[13]
                                               or defense_type_one == pokemon_types[16] or defense_type_one == pokemon_types[1]
                                               or defense_type_one == pokemon_types[17])):
        pass

    #ghost
    if (attack_type == pokemon_types[13] and (defense_type_one == pokemon_types[15])):
        pass

    #steel
    if (attack_type == pokemon_types[16] and (defense_type_one == pokemon_types[16] or defense_type_one == pokemon_types[1] 
                                                  or defense_type_one == pokemon_types[2] or defense_type_one == pokemon_types[3])):
        pass  

    #fire
    if (attack_type == pokemon_types[1] and (defense_type_one == pokemon_types[12] or defense_type_one == pokemon_types[1]
                                                  or defense_type_one == pokemon_types[2] or defense_type_one == pokemon_types[14])):
        pass

    #water
    if (attack_type == pokemon_types[2] and (defense_type_one == pokemon_types[2] or defense_type_one == pokemon_types[4]
                                             or defense_type_one == pokemon_types[14])):
        pass

    #grass
    if (attack_type == pokemon_types[4] and (defense_type_one == pokemon_types[9] or defense_type_one == pokemon_types[7]
                                             or defense_type_one == pokemon_types[11] or defense_type_one == pokemon_types[16]
                                             or defense_type_one == pokemon_types[1] or defense_type_one == pokemon_types[4]
                                             or defense_type_one == pokemon_types[14])):
        pass

    #electric
    if (attack_type == pokemon_types[3] and (defense_type_one == pokemon_types[4] or defense_type_one == pokemon_types[3]
                                             or defense_type_one == pokemon_types[14])):
        pass

    #psychic
    if (attack_type == pokemon_types[10] and (defense_type_one == pokemon_types[16] or defense_type_one == pokemon_types[10])):
        pass

    #ice
    if (attack_type == pokemon_types[5] and (defense_type_one == pokemon_types[16] or defense_type_one == pokemon_types[1]
                                             or defense_type_one == pokemon_types[2] or defense_type_one == pokemon_types[5])):
        pass

    #dragon
    if (attack_type == pokemon_types[14] and (defense_type_one == pokemon_types[16])):
        pass

    #dark
    if (attack_type == pokemon_types[15] and (defense_type_one == pokemon_types[6] or defense_type_one == pokemon_types[15]
                                              or defense_type_one == pokemon_types[17])):
        pass

    #fairy
    if (attack_type == pokemon_types[17] and (defense_type_one == pokemon_types[7] or defense_type_one == pokemon_types[16]
                                              or defense_type_one == pokemon_types[1])):
        pass

    if defense_type_two == False:
        pass
    else:
        pass

        """
    if defense_type_one in type[attack_type].keys():
        pass
    
    damage_multiplier = first_multiplier * second_multiplier









        