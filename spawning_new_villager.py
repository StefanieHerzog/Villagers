villager_count = 0


def spawn_new_villager():
    villager_count += 1
    villager_instance = "villager" + str(villager_count)
    "villager" + str(villager_count) = Villager()
    assign_name_to_villager("villager" + str(villager_count))

    print(villager_count)


# creating a function that deletes all villagers

# instances = [obj for obj in globals().values() if isinstance(obj, Villager)]

for i in range(100):
    instances.append(Villager(i))

print(instances)