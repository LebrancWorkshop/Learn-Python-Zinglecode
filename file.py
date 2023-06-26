file = open('player_list.txt')

not_validate_count = 0
for player in file:
  player = player.split('\n')[0]
  if len(player) > 5:
    not_validate_count += 1

report = "Player not validated: {}".format(not_validate_count)
file.close()

file_for_write = open('report.txt', 'w')

file_for_write.write(report)

file_for_write.close()
