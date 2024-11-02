import time, os, random, sys
import monster_pick as monster
from player import player

#=====================NO INPUT TECHNIQUE===============================
if sys.platform == "win32":
	import msvcrt

	def getch():
		return msvcrt.getch().decode('utf-8')

else:
	import tty
	import termios

	def getch():
		fd = sys.stdin.fileno()
		old_settings = termios.tcgetattr(fd)
		try:
			tty.setraw(fd)
			ch = sys.stdin.read(1)
		finally:
			termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
		return ch
#=====================================================================

class Fight:
	def __init__(self, player) -> None:
		self.player = player
		self.current_monster = None
		self.fleed = False

	def hp_bar(self, entity) -> str:
		""" Returns a visual representation of the HP bar for any entity """
		hp_perc = entity.hp / entity.max_hp
		max_hp_bar_length = 10
		filled_bars = int(hp_perc * max_hp_bar_length)
		return f"[{'▆' * filled_bars}{' ' * (max_hp_bar_length - filled_bars)}]"

	def display_entity_stats(self, entity, hp_bar: str, is_player: bool = False) -> None:
		""" Displays stats for player or monster """
		print(f"{'Player Stats' if is_player else 'Monster Stats':<10}")
		print(f"{'-'*30}")
		if not is_player:
			print(f"{'Name':<10}| {entity.name}")
		print(f"{'Health':<10}| {hp_bar} {int(entity.hp)}/{int(entity.max_hp)}")
		if is_player:
			print(f"{'MP':<10}| {entity.mp}/{entity.max_mp}")
		print(f"{'Level':<10}| {entity.level}")
		print(f"{'-'*30}")

	def game_state(self) -> None:
		os.system('cls' if os.name == 'nt' else 'clear')
		print(f"{'='*30}")
		enemy_hp = self.hp_bar(self.current_monster)
		player_hp = self.hp_bar(self.player)
		self.display_entity_stats(self.current_monster, enemy_hp)
		self.display_entity_stats(self.player, player_hp, is_player=True)
		print(f"{'[1] Fight, [2] Defend, [3] Items (Coming soon), [4] Run':<10}")
		print(f"{'='*30}")

	def start(self, current_monster):
		self.current_monster = current_monster
		self.fleed = False

		while True:
			self.game_state()
			action = int(getch())
			self.process_input(action)

			# Outcome conditions
			if self.player.hp <= 0:
				print('You died! Respawning...')
				time.sleep(3)
				self.reset()
				return 'dead'
			elif self.current_monster.hp <= 0:
				print('You win!')
				time.sleep(1)
				self.player.get_exp(self.current_monster.exp)
				return 'win'
			elif self.fleed:
				print('You narrowly fled the scene...')
				time.sleep(1)
				return 'fled'

	def process_input(self, action: int) -> None:
		""" Process player input during fight """
		if action == 1:
			self.monster_retaliate('attacking')
		elif action == 2:
			self.monster_retaliate('defending')
		elif action == 3:
			# Implement item functionality here
			pass
		elif action == 4:
			self.try_flee()

	def try_flee(self) -> None:
		""" Attempt to flee from the fight """
		fleed_chance = random.random()
		print("You tried to leave the battle..")
		time.sleep(1)
		if fleed_chance <= 0.35:
			self.fleed = True
		else:
			print("You failed.")
			self.monster_retaliate('')

	def monster_retaliate(self, action_type: str) -> None:
		""" Monster retaliates based on player action """
		monster_damage = random.uniform(self.current_monster.dmg * 0.25, self.current_monster.dmg)
		if action_type == 'defending':
			damage_reduction = random.uniform(0.50, 0.99)
			damage_taken = monster_damage * damage_reduction
			print("You steeled your body..")
			time.sleep(1)
			print(f"Blocked! {self.current_monster.name} dealt {int(damage_taken)} dmg")
		else: #PLAYER ATTACK
			base_dmg = 3
			player_damage = base_dmg + self.player.strength // 2
			damage_fluctuation = random.randint(-2, 2)
			player_damage += damage_fluctuation
			print(f"Attacked for {int(player_damage)}.")
			self.current_monster.hp -= player_damage

		print(f"{self.current_monster.name} attacked for {int(monster_damage)}.")
		self.player.hp -= int(monster_damage)
		time.sleep(1)

	def reset(self) -> None:
		""" Reset player health and mana """
		self.player.hp = self.player.max_hp
		self.player.mp = self.player.max_mp


fight = Fight(player)

if __name__ == '__main__':
	monster = monster.rabbit
	player.name = "Joe"
	player.strength += 100
	monster.spawn()
	fight.start(monster)