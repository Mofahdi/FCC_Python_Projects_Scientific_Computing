import copy
import random
# Consider using the modules imported above.


class Hat:

  def __init__(self, **kwargs):
    self.contents = list()
    for key, val in kwargs.items():
      for i in range(val):
        self.contents.append(key)

  def draw(self, num_balls):
    if num_balls > len(self.contents):
      return self.contents
    #contents = self.contents
    drawn=list()
    contents=self.contents
    for process in range(num_balls):
      ind = random.randint(0, len(contents)-1)
      drawn.append(self.contents.pop(ind))
      
    return drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  success_nums=[val for key, val in expected_balls.items()]
  success=0
  for i_exper in range(num_experiments):
    hat_copied = copy.deepcopy(hat)
    drawn_balls=hat_copied.draw(num_balls_drawn)
    #print(drawn_balls)
    balls_drawn_list=list()
    for key in expected_balls.keys():
      balls_drawn_list.append(drawn_balls.count(key))
    #print(success_nums, balls_drawn_list)
    if balls_drawn_list>=success_nums:
      success+=1
  return success/num_experiments