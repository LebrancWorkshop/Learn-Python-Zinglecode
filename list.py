quests = ['Finding New Star', 'Friend with Star and Fire']

max_quests = 10

def add_quest(quest: str):
  if len(quests) < max_quests:
    quests.append(quest)
    print('Add Quest Success')
  else:
    print("You cannot add a new quest, Please cancel at least one of your quest before.")

def cancel_quest(quest: str):
  if quest in quests:
    quests.remove(quest)
    print('Cancel Quest Success')
  else:
    print("You don't have this quest in your list.")

def list_quest():
  print('Quest List:')
  for i in range(len(quests)):
    print('{}. {}'.format(i+1, quests[i])) 
