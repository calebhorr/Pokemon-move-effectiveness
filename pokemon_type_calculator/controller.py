def calculate(attack_type,defense_type_one,defense_type_two,pokemon_types):
    first_multiplier = 0
    second_multiplier = 0
    damage_multiplier = 1
    #0.5 effectiveness 
            
    #normal
    if (attack_type == pokemon_types[0] and (defense_type_one == pokemon_types[12] or defense_type_one == pokemon_types[16])):
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

    
    damage_multiplier = first_multiplier * second_multiplier









        