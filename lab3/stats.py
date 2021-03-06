import constants.settings as settings


class Stats():

    def __init__(self, name):
        """Init statistic"""
        self.name = name
        self.reset_stats()
        self.run_game = True
        self.new_record=False
        with open(settings.HIGH_SCORE, 'r') as f:
            self.high_score = int(f.readline())

    def reset_stats(self):
        """Change in time"""
        self.guns_left = 2
        self.score = 0
        self.new_level = 1
