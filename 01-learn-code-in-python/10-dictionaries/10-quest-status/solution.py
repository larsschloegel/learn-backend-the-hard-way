def get_quest_status(progress):
    return progress["quests"]["bridge_run"]["status"]

#my solution
def get_quest_status(progress):
    status = progress["quests"]["bridge_run"]     
    return status["status"]