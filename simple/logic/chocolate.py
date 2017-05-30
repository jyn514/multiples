def make_chocolate(small, big, goal):
  mod = goal % 5
  if not mod and big >= goal / 5:
    return 0
  elif small < mod or (big < goal / 5 and small < 5) or small + big * 5 < goal:
    return -1
  elif big <= goal // 5:
    return goal - big * 5
  else:
    return goal - goal // 5 * 5
