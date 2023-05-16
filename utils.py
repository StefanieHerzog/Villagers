def get_villager_by_name(villagers, name):
    for villager in villagers:
        if villager.name.lower() == name.lower():
            return villager


