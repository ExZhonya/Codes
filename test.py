class CutsceneA:
    def __init__(self, grass_quest):
        self.quest_status = grass_quest
        print("Not updated")
    
    def quest_start(self):  # Added 'self' here
        print("test")
    
    def quest_update(self, grass_quest_new):
        self.quest_status = grass_quest_new
        print("Updated")

queststats = CutsceneA(False)
queststats.quest_update(True)
queststats.quest_start()  # Call the method to see "test" output