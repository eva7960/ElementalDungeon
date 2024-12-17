import sqlite3
from Model.Element import Element
con = sqlite3.connect('../Assets/character.db')
cur = con.cursor()
# Create monster table
cur.execute("CREATE TABLE IF NOT EXISTS monster(name, image, hit_image, dead_image, element UNIQUE, max_health, agility)")
data = [
    ('Earth Monster', 'earth_monster.png', 'earth_monster_hit.png','earth_monster_dead.png',Element.EARTH.value, 50, 4),
    ('Air Monster', 'air_monster.png', 'air_monster_hit.png','air_monster_dead.png',Element.AIR.value, 20, 16),
    ('Water Monster', 'water_monster.png', 'water_monster_hit.png','water_monster_dead.png',Element.WATER.value, 30, 8),
    ('Fire Monster', 'fire_monster.png', 'fire_monster_hit.png','fire_monster_dead.png',Element.FIRE.value, 40, 12),
]
cur.executemany("INSERT INTO monster VALUES(?, ?, ? ,?, ?, ?, ?)", data)
con.commit()
# Create Hero table
cur.execute("CREATE TABLE IF NOT EXISTS hero(image, hit_image, dead_image, element UNIQUE, max_health, agility)")
data = [
    ('earth_hero.png', 'earth_hero_hit.png','earth_hero_dead.png',Element.EARTH.value, 100, 4),
    ('air_hero.png', 'air_hero_hit.png','air_hero_dead.png',Element.AIR.value, 40, 16),
    ('water_hero.png', 'water_hero_hit.png','water_hero_dead.png',Element.WATER.value, 80, 8),
    ('fire_hero.png', 'fire_hero_hit.png','fire_hero_dead.png',Element.FIRE.value, 60, 12),
]
cur.executemany("INSERT INTO hero VALUES(?, ?, ?, ?, ?, ?)", data)
con.commit()
con.close()