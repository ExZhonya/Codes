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
	def __init__(self):
		self.player = player
		self.current_monster = None
		self.player_name = None
		self.monster_name = None

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
		self.player_name = 'Test'
		self.monster_name = self.current_monster.name
		self.fleed = False

		while True:
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
			print(f"{'[1]Fight, [2]Defend, [3]Items(Coming soon) [4]Run':<10}")
			print(f"{'='*30}")

			self.input_process(int(getch()))

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

	def input_process(self, getch):
		if getch == 1:
			self.monster_retaliate('attacking')
		elif getch == 2:
			self.monster_retaliate('defending')
		elif getch == 3:
			# acesses items
			pass
		elif getch == 4:
			fleed_chance = random.random()
			print("You tried to leave the battle..")
			time.sleep(1)
			if fleed_chance <= 0.35:
				self.fleed = True
				return
			else:
				print("You failed.")
				self.monster_retaliate('')

	def monster_retaliate(self, type):
		damage_fluctuation = random.uniform(self.current_monster.dmg * 0.25, self.current_monster.dmg)
		if type == 'defending':
			damage_reduction_fluctuation = random.uniform(0.50, 0.99)
			damage = damage_fluctuation * damage_reduction_fluctuation
			
			print("You steeled your body..")
			time.sleep(1)
			print(f"Blocked! {self.monster_name} dealt {int(damage)} dmg")
			self.player.hp -= int(damage)
			time.sleep(1)
			return
		elif type == 'attacking':
			player_damage = self.player.strength / 2 
			print(f"Attacked for {int(player_damage)}.")
			self.current_monster.hp -= player_damage
			time.sleep(1)

		print(f"{self.monster_name} attacked for {int(damage_fluctuation)}.")
		self.player.hp -= int(damage_fluctuation)
		time.sleep(1)

	def reset(self):
		self.player.hp = self.player.max_hp
		self.player.mp = self.player.max_mp

fight = Fight()

if __name__ == '__main__':
	monster = monster.rabbit
	player.strength += 100
	monster.spawn()
	fight.start(monster)