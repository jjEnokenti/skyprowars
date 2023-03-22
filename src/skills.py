from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from unit import BaseUnit


class AbstractSkill(ABC):
    user = None
    target = None

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def stamina(self):
        pass

    @property
    @abstractmethod
    def damage(self):
        pass

    @abstractmethod
    def skill_effect(self):
        pass

    def _is_stamina_enough(self):
        return self.user.stamina >= self.stamina

    def use(self, user: BaseUnit, target: BaseUnit):
        self.user = user
        self.target = target
        if self._is_stamina_enough():
            return self.skill_effect()
        return f'{self.user.name} недостаточно выносливости, чтобы использовать {self.name}. Отдохни!'


class CrushingBlow(AbstractSkill):
    name: str = 'Crushing blow'
    damage: float = 12.0
    stamina: float = 6.0

    def skill_effect(self):
        self.user.stamina -= self.stamina
        self.target.hp -= self.damage

        return f'{self.user.name} применил умение {self.name} и нанес {self.target.name} {self.damage} урона'


class Skewer(AbstractSkill):
    name: str = 'Skewer'
    damage: float = 15.0
    stamina: float = 5

    def skill_effect(self):
        self.user.stamina -= self.stamina
        self.target.hp -= self.damage

        return f'{self.user.name} применил умение {self.name} и нанес {self.target.name} {self.damage} урона'
