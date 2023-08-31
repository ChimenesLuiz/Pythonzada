from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class First(App):
    
    def build(self):
        self.box = BoxLayout(orientation = 'vertical')
        self.box_top = BoxLayout()
        self.box_bot = GridLayout(cols = 5)
        self.result = str(0)
        
        self.screen = Label(text = str(self.result), font_size = "50")
        self.bot_0 = Button(text = '0', font_size = 50, on_press = self.writeZero)
        self.bot_1 = Button(text = '1', font_size = 50, on_press = self.writeOne)
        self.bot_2 = Button(text = '2', font_size = 50, on_press = self.writeTwo)
        self.bot_3 = Button(text = '3', font_size = 50, on_press = self.writeThree)
        self.bot_4 = Button(text = '4', font_size = 50, on_press = self.writeFour)
        self.bot_5 = Button(text = '5', font_size = 50, on_press = self.writeFive)
        self.bot_6 = Button(text = '6', font_size = 50, on_press = self.writeSix)
        self.bot_7 = Button(text = '7', font_size = 50, on_press = self.writeSeven)
        self.bot_8 = Button(text = '8', font_size = 50, on_press = self.writeEight)
        self.bot_9 = Button(text = '9', font_size = 50, on_press = self.writeNine)
        self.bot_virgula = Button(text = ',', font_size = 50)
        self.bot_resto = Button(text = '%', font_size = 50)
        self.bot_pare_left = Button(text = '(', font_size = 50)
        self.bot_pare_right = Button(text = ')', font_size = 50)
        self.bot_pare_equal = Button(text = '=', font_size = 50)
        self.bot_add = Button(text = '+', font_size = 50)
        self.bot_sub = Button(text = '-', font_size = 50)
        self.bot_mult = Button(text = 'x', font_size = 50)
        self.bot_div = Button(text = '/', font_size = 50)
        self.bot_clear = Button(text = 'AC', font_size = 50)
        self.bot_equal = Button(text = '=', font_size = 50)
        
        
        
        self.box_top.add_widget(self.screen)
        self.box_bot.add_widget(self.bot_7)
        self.box_bot.add_widget(self.bot_8)
        self.box_bot.add_widget(self.bot_9)
        self.box_bot.add_widget(self.bot_div)
        self.box_bot.add_widget(self.bot_clear)
        self.box_bot.add_widget(self.bot_4)
        self.box_bot.add_widget(self.bot_5)
        self.box_bot.add_widget(self.bot_6)
        self.box_bot.add_widget(self.bot_mult)
        self.box_bot.add_widget(self.bot_pare_left)
        self.box_bot.add_widget(self.bot_1)
        self.box_bot.add_widget(self.bot_2)
        self.box_bot.add_widget(self.bot_3)
        self.box_bot.add_widget(self.bot_sub)
        self.box_bot.add_widget(self.bot_pare_right)
        self.box_bot.add_widget(self.bot_0)
        self.box_bot.add_widget(self.bot_virgula)
        self.box_bot.add_widget(self.bot_resto)
        self.box_bot.add_widget(self.bot_add)
        self.box_bot.add_widget(self.bot_equal)


        
        self.box.add_widget(self.box_top)
        self.box.add_widget(self.box_bot)
        
        return self.box

    def writeOne(self, button):
        self.result = str(self.result)
        self.result = str(1)
        self.screen.text = self.result

    def writeTwo(self, button):
        self.result += str(self.result)
        self.result = str(2)
        self.screen.text = self.result
        
    def writeThree(self, button):
        self.result = 3
        self.screen.text = f"{self.result}"
        
    def writeFour(self, button):
        self.result = 4
        self.screen.text = f"{self.result}"
        
    def writeFive(self, button):
        self.result = 5
        self.screen.text = f"{self.result}"
        
    def writeSix(self, button):
        self.result = 6
        self.screen.text = f"{self.result}"
        
    def writeSeven(self, button):
        self.result = 7
        self.screen.text = f"{self.result}"
        
    def writeEight(self, button):
        self.result = 8
        self.screen.text = f"{self.result}"
        
    def writeNine(self, button):
        self.result = 9
        self.screen.text = f"{self.result}"
        
    def writeZero(self, button):
        self.result = 0
        self.screen.text = f"{self.result}"

        

system = First()
system.run()