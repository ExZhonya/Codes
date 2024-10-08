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
			print(f"{'[1]Fight, [2]Defend, [3]Run':<10}")
			print(f"{'='*30}")

			option = int(getch())

			fleed = False

			match option:
				case 1:
					chance = random.randint(0, 100)
					if chance >= 20:
						# Enemy Retaliates
						self.attack('player')
						time.sleep(1)
						self.attack('enemy')
						time.sleep(1)
					else:
						# Enemy Blocks
						self.attack('player (blocked)')
						time.sleep(1)
				
				case 2:
					self.block('player')
					time.sleep(1)
					self.attack('enemy (blocked)')
					time.sleep(1)
				
				case 3:
					fleed = self.flee()
					time.sleep(1)

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

			elif fleed:
				print('You narrowly fled the scene...')
				time.sleep(1)
				self.reset()
				return 'fled'

	def attack(self, turn):
		if turn == 'player':
			player = int(self.player.strength / 2)
			self.current_monster.hp -= player
			print(f'{self.player_name} attacked for {player} dmg!')

		elif turn == 'player (blocked)':
			player = int(self.player.strength / 4)
			self.current_monster.hp -= player
			print(f'{self.player_name} attacked,')
			time.sleep(1)
			print(f'but got deflected for only {player} dmg!')

		elif turn == 'enemy':
			monster = int(self.current_monster.dmg)
			self.player.hp -= monster 
			print(f'{self.monster_name} attacked for {monster} dmg!')

		elif turn == 'enemy (blocked)':
			monster = int(self.current_monster.dmg / 2)
			self.player.hp -= monster 
			print(f'And {self.monster_name} attacked for {monster} dmg')	

		elif turn == 'enemy (fled)':
			monster = int(self.current_monster.dmg)
			self.player.hp -= monster 
			print(f'{self.monster_name} caught up and dealt {monster} dmg!')

	def block(self, turn):
		if turn == 'player':
			print(f'{self.player_name} anticipates the next attack')

	def flee(self):
		flee = random.random()
		print('You tried to flee...')
		time.sleep(1)
		if flee > 0.20:
			return True
		else:
			self.attack('enemy (fled)')

	def reset(self):
		self.player.hp = self.player.max_hp
		self.player.mp = self.player.max_mp

if __name__ == '__main__':
	fight = Fight()
	monster = monster.rabbit
	monster.spawn()
	fight.start(monster)