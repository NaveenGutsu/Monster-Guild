GUILD_ORIGIN = ("Whispering Peak", 1204)

blaze_dragon_elements = {"Fire", "Flying", "Fire"}

monster_1 = {
    "name": "Ignis the Dragon",
    "level": 12,
    "elements": blaze_dragon_elements,
    "stats": (120, 85),  
}

monster_2 = {
    "name": "Aquaria the Kelpie",
    "level": 9,
    "elements": {"Water", "Ice"},
    "stats": (95, 60),
}

guild_roster = [monster_1, monster_2]


def display_guild_roster(roster):
    print("=" * 40)
    print(f"🏰 GUILD HEADQUARTERS: {GUILD_ORIGIN[0]} (Est. {GUILD_ORIGIN[1]})")
    print("=" * 40)

    for monster in roster:
        hp, atk = monster["stats"]
        elements_str = ", ".join(monster["elements"])

        print(f"👾 {monster['name']} [Lvl {monster['level']}]")
        print(f"   Elements : {elements_str}")
        print(f"   HP / ATK : {hp} HP | {atk} ATK")
        print("-" * 40)


def recruit_monster(roster, name, level, element_list, hp, atk):
    """Adds a new monster to the list."""
    new_monster = {
        "name": name,
        "level": level,
        "elements": set(element_list),  
        "stats": (hp, atk),             
    }
    roster.append(new_monster)
    print(f"✨ Successfully recruited {name} into the guild!\n")


recruit_monster(
    guild_roster,
    name="Terra Golem",
    level=15,
    element_list=["Earth", "Rock", "Earth"],
    hp=200,
    atk=70,
)

display_guild_roster(guild_roster)
