class Player:
  def __init__(self, name: str, race: str, type: str, level: int, exp: int = 0):
    self.name = name
    self.race = race
    self.type = type
    self.level = level
    self.exp = exp

  def level_up(self):
    if(self.exp > 30):
      self.level += 1
    else:
      print("You don\'t have enough exp to up your level")

