class Pastebin(object):
  '''
  Provides a set of functions to interact with pastebin.com
  '''
  def __init__(self, name="pastebin"):
    self.name = name

  def doit(self):
    '''
    Pretends to do work and then returns a string to indicate that the work is done
    Note that we return a string rather than print it. That way the calling function
    can choose to do something other than print
    '''
    return "{0} is done".format(self.name)