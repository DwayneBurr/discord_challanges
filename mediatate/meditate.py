def meditate(mana, max_mana, energy, energy_potions):
    while mana < max_mana:
        if energy > 0:
            energy -= 1
            mana += 3
        elif energy == 0 and energy_potions > 0:
            energy_potions -= 1
            energy += 50
        else:
            return "out of energy,out of potions"
        
    if mana > max_mana:
        energy += (mana - max_mana) / 3
        mana = max_mana
    return f"Mana:{mana}\nEnergy:{energy}\nPotions:{energy_potions}"

print(meditate(10,100,3,0))
            

