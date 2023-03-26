class Rectangle:
  def __init__(self, width, height):
    self.width=width
    self.height=height
	
  def __str__(self):
    return 'Rectangle(width={}, height={})'.format(self.width, self.height)
  
  def set_width(self, width):
    self.width=width
  def set_height(self, height):
    self.height=height
    
  def get_area(self):
    return self.width * self.height
  def get_perimeter(self):
    return 2*self.height+2*self.width
  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5
  
  def get_picture(self):
    if self.height>50 or self.width>50:
      return "Too big for picture."
    pic_format=str()
    for i in range(self.height):
      pic_format+=''.center(self.width, '*')+'\n'
    return pic_format

  def get_amount_inside(self, smaller):
    small=smaller.get_area()
    big=self.get_area()
    return big//small
    
class Square(Rectangle):
  def __init__(self, side):
    self.width=side; self.height=side
  def __str__(self):
    return 'Square(side={})'.format(self.width)
  def set_side(self, side):
    self.width=side; self.height=side
  
