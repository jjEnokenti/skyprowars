from src.unit import BaseUnit


class BaseSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Arena(metaclass=BaseSingleton):
    STAMINA_PER_ROUND = 1
    player = None
    enemy = None
    game_is_running = False
    battle_result = None

    def start_game(self, player: BaseUnit, enemy: BaseUnit):
        self.player = player
        self.enemy = enemy
        self.game_is_running = True

    def _check_players_hp(self):
        if self.player.hp > 0 and self.enemy.hp > 0:
            return None

        if self.player.hp <= 0 and self.enemy.hp <= 0:
            self.battle_result = 'Ничья'
        elif self.player.hp <= 0:
            self.battle_result = f'{self.player.name} проиграл битву'
        else:
            self.battle_result = f'{self.player.name} выиграл битву'

        return self._end_game()

    def _stamina_regeneration(self):
        units = (self.player, self.enemy)

        for unit in units:
            if unit.stamina + self.STAMINA_PER_ROUND * unit.unit_class.stamina <= unit.unit_class.max_stamina:
                unit.stamina += self.STAMINA_PER_ROUND * unit.unit_class.stamina
            else:
                unit.stamina = unit.unit_class.max_stamina

    def next_turn(self):
        result = self._check_players_hp()
        if result is not None:
            return result

        enemy_hit = self.enemy.hit(target=self.player)
        self._stamina_regeneration()
        return enemy_hit

    def _end_game(self):
        self._instances = {}
        self.game_is_running = False
        return self.battle_result

    def player_hit(self):
        hit_result = self.player.hit(target=self.enemy)
        enemy_result = self.next_turn()
        return f'{hit_result}<br>{enemy_result}'

    def player_use_skill(self):
        skill_used_result = self.player.use_skill(target=self.enemy)
        enemy_result = self.next_turn()
        return f'{skill_used_result}<br>{enemy_result}'
