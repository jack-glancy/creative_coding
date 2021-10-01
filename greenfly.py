from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty
import overview as ovr
import airp as air
import diet_options as diet
from kivy.uix.textinput import TextInput


class Eco_run(Widget):
    pass


class EcoApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        dropdiet = DropDown()
        options = list(diet.diet_options.dict.keys())
        for i in options:
            btn = Button(text=str(i), size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: dropdiet.select(btn.text))
            dropdiet.add_widget(btn)
        drop1 = DropDown()
        drop2 = DropDown()
        options = list(air.airports.dict.keys())
        for i in options:
            btn = Button(text=str(i), size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: drop1.select(btn.text))
            drop1.add_widget(btn)
        for i in options:
            btn = Button(text=str(i), size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: drop2.select(btn.text))
            drop2.add_widget(btn)
        self.dietbtn = Button(text='Diet')
        self.Departbtn = Button(text='Departure')
        self.Arrivalbtn = Button(text='Arrival')
        self.dietbtn.bind(on_release=dropdiet.open)
        self.Departbtn.bind(on_release=drop1.open)
        self.Arrivalbtn.bind(on_release=drop2.open)
        dropdiet.bind(on_select=lambda instance, y: setattr(self.dietbtn, 'text', y))
        drop1.bind(on_select=lambda instance, y: setattr(self.Departbtn, 'text', y))
        drop2.bind(on_select=lambda instance, x: setattr(self.Arrivalbtn, 'text', x))
        calcbtn = Button(text='Calculate')
        calcbtn.bind(on_release=self.calculate)
        label0 = Label(text='Please enter the diet that best describes your own.')
        label1 = Label(text='Please enter your departure destination:')
        label2 = Label(text='And please enter where you are flying to:')
        self.solution = Label(text='', markup=True, halign='center')
        layout.add_widget(label0)
        layout.add_widget(self.dietbtn)
        layout.add_widget(label1)
        layout.add_widget(self.Departbtn)
        layout.add_widget(label2)
        layout.add_widget(self.Arrivalbtn)
        layout.add_widget(calcbtn)
        layout.add_widget(self.solution)
        return layout

    def calculate(self, out):
        ovr.lookup_positions(str(self.Departbtn.text), str(self.Arrivalbtn.text))
        ovr.get_class()
        ovr.calculate_ghg()
        ovr.diet_find(str(self.dietbtn.text))
        ovr.calc_days()
        self.solution.text = 'You\'ve flown ' + str(round(ovr.cons.dist)) + ' km and generated ' + str(round(ovr.cons.ghg, 1)) + ' kg of CO[sub]2[/sub] equivalents with your flight.\n ' \
                                                                                                                                 'You can offset this with ' + str(round(ovr.cons.days)) + ' days of changing your diet from ' + str(self.dietbtn.text) + ' to being a vegan.'




class AirDrop(Widget):
        xq = DropDown()
        for index in range(10):
            # When adding widgets, we need to specify the height manually
            # (disabling the size_hint_y) so the dropdown can calculate
            # the area it needs.

            btn = Button(text='Value %d' % index, size_hint_y=None, height=44)

            # for each button, attach a callback that will call the select() method
            # on the dropdown. We'll pass the text of the button as the data of the
            # selection.
            btn.bind(on_release=lambda btn: xq.select(btn.text))

            # then add the button inside the dropdown
            xq.add_widget(btn)
        # create a big main button
        mainbutton = Button(text='Hello', size_hint=(None, None))

        # show the dropdown menu when the main button is released
        # note: all the bind() calls pass the instance of the caller (here, the
        # mainbutton instance) as the first argument of the callback (here,
        # dropdown.open.).
        mainbutton.bind(on_release=xq.open)

        # one last thing, listen for the selection in the dropdown list and
        # assign the data to the button text.
        xq.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))


if __name__ == '__main__':
    EcoApp().run()
