import sublime, sublime_plugin
import os

class DetectFileTypeCommand(sublime_plugin.EventListener):

  def on_load(self, view):
    filename = view.file_name()
    if not filename: # buffer has never been saved
      return

    name = os.path.basename(filename.lower())
    
    if name[-2:] == "rb":
      set_syntax(view, "Ruby on Rails", "Rails")
    elif name[-7:] == "gemfile":
      set_syntax(view, "Ruby", "Ruby")
    elif name[-9:] == "guardfile":
      set_syntax(view, "Ruby", "Ruby")
    elif name[-2:] == "ru":
      set_syntax(view, "Ruby", "Ruby")
    elif name[-9:] == "coffeekup":
      set_syntax(view, "CoffeeKup", "CoffeeKup")

def set_syntax(view, syntax, path=None):
  if path is None:
    path = syntax
  view.settings().set('syntax', 'Packages/'+ path + '/' + syntax + '.tmLanguage')
  print "Switched syntax to: " + syntax
