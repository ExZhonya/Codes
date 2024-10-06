import time, os, random, sys
from player import Player
import monster_pick as monster

player = Player()

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
	def __init__(self):
		self.player = player
		self.current_monster = None

	def hp_bar(self, entity):
		hp = entity.hp
		max_hp = entity.max_hp
		max_hp_bar_length = 10

		hp_perc = hp / max_hp

		filled_bars = int(hp_perc * max_hp_bar_length)

		health_bar = "[{}{}]".format('▆' * filled_bars, ' ' * (max_hp_bar_length - filled_bars))
		return health_bar

	def start(self, current_monster):
		self.current_monster = current_monster
		while self.player.hp > 0:
			enemy_hp = self.hp_bar(self.current_monster)
			player_hp = self.hp_bar(self.player)

			os.system('cls;clear')
			print(f"{'='*30}")
			print(f"{'Monster Stats':<10}")
			print(f"{'-'*30}")
			print(f"{'Name':<10}| {current_monster.name}")
			print(f"{'Health':<10}| {enemy_hp}{int(self.current_monster.hp)}/{int(self.current_monster.max_hp)}")
			print(f"{'Level':<10}| {self.current_monster.level}")
			print(f"{'='*30}")
			print(f"{'Player Stats':<10}")
			print(f"{'-'*30}")
			print(f"{'HP':<10}| {player_hp}{int(self.player.hp)}/{int(self.player.max_hp)}")
			print(f"{'MP':<10}| {self.player.mp}/{self.player.max_mp}")
			print(f"{'Level':<10}| {self.player.level}")
			print(f"{'-'*30}")
			print(f"{'[1]Fight, [2]Defend, [3]Run':<10}")
			print(f"{'='*30}")

			option = getch()

			match option:
				case '1':
					monster_dead = self.enemy_response(self.attack())
				case '2':
					monster_dead = self.enemy_response(self.defend())
				case '3':
					monster_dead = self.enemy_response(self.flee())
			
			if monster_dead:
				monster_dead = False
				# reset player stats
				self.player.hp = self.player.max_hp
				self.player.hp = self.player.max_mp

				# give monster exp reward
				self.player.get_exp(self.current_monster.exp)
				time.sleep(1)
				return True

		if self.player.hp < 0:
			print("You died, and got nothing, you wake up in the nearest village...")
			time.sleep(2)
			return False

	def attack(self):
		damage = int(self.player.strength // 2)
		return damage

	def defend(self):
		print(f"You defend the next attack...")
		time.sleep(1)
		return -1

	def flee(self):
		flee_chance = random.random()
		evasion = 0.30
		if flee_chance < evasion:
			print("You successfully escaped!")
			time.sleep(1)
			return True
		else:
			print("You failed to escape.")
			time.sleep(1)
			enemy_response(0)

			
	def enemy_response(self, damage):
		name = self.current_monster.name

		if damage >= self.current_monster.hp:
			print(f"{name} took too much dmg, it cannot fight anymore.")
			time.sleep(1)
			return True

		move = random.random()
		if move >= 0.30 or damage < 0: # Attack

			monster_dmg = self.current_monster.dmg

			# checks if player is attacking (damage > 0)
			if damage > 0: 
				self.current_monster.hp -= damage
				print(f"You dealt {damage} dmg!")
				time.sleep(1)

			# checks if player is defending (damage = -1)
			if damage < 0: 
				monster_dmg = monster_dmg // 3 # cuts the monster dmg by 3

			final_dmg = random.randint(int(0.25 * self.current_monster.damage), self.current_monster.damage)
			player.hp -= final_dmg
			print(f"{name} dealt {final_dmg} dmg!")
			time.sleep(1)

		elif move <= 0.30: # Defense
			
			# checks if player is attacking ( damage > 0)
			if damage > 0:
				self.current_monster.hp -= damage // 2
				print(f"{name} blocked and took {damage // 2} dmg!")
				time.sleep(1)

if __name__ == '__main__':
	fight = Fight()
	monster = monster.rabbit
	monster.spawn()
	fight.start(monster)