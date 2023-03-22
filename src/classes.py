from dataclasses import dataclass

from src.skills import AbstractSkill, Skewer, CrushingBlow


@dataclass
class UnitClass:
    name: str
    max_health: float
    max_stamina: float
    attack: float
    stamina: float
    armor: float
    skill: AbstractSkill


WarriorClass = UnitClass(
    name='Warrior',
    max_health=60.0,
    max_stamina=10.0,
    attack=0.8,
    armor=1.2,
    stamina=0.9,
    skill=CrushingBlow()
)

ThiefClass = UnitClass(
    name='Thief',
    max_health=50.0,
    max_stamina=10.0,
    attack=1.5,
    armor=1.0,
    stamina=1.2,
    skill=Skewer()
)

unit_classes = {
    ThiefClass.name: ThiefClass,
    WarriorClass.name: WarriorClass
}
