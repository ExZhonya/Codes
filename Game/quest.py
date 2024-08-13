class quest_upd:
    def __init__(self, grass_quest):
        self.quest_status = grass_quest

    def quest_update(self, grass_quest_new):
        self.quest_status = grass_quest_new


queststats = quest_upd(False)
queststats.quest_update(True)