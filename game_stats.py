class GameStats:
	"""Track statistics for alien invasion game"""

	def __init__(self, ai_game):
		"""Initialize statistics"""
		self.settings = ai_game.settings
		self.reset_stats()

		# Start alien invasion in active state
		self.game_active = False

	def reset_stats(self):
		""" Initialize statistics that change during the game"""
		self.ships_left = self.settings.ship_limit