from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from subprocess import call

class MapApp(App):

    def on_button_press(self, instance, file_name):
        # Teraz funkcja on_button16_press przyjmuje argument file_name z miejsca wywołania
        self.open_file(file_name)

    def open_file(self, file_name):
        call(["python", file_name])





    def build(self):
        # Tworzymy główny layout jako FloatLayout
        layout = FloatLayout()

        # Dodajemy obraz mapy do layout
        map_image = Image(source='mapa.jpg', allow_stretch=True, keep_ratio=False)
        layout.add_widget(map_image)

        # etykieta i przycisk w layout
        # Przyciski województw
        label = Label()
        exit_button = Button(text="Exit", size_hint=(None, None), size=(100, 50), pos=(10, 10))

        button1 = Button(
            text="Zachodnio-Pomorskie",
            size_hint=(None, None),
            size=(100, 50),
            pos=(121.28035043804756, 602.7011686143572),
            font_size=10
        )

        button1 = Button(text="Zachodnio-Pomorskie", size_hint=(None, None), size=(80, 40),
                         pos=(121.28035043804756, 602.7011686143572), font_size = 10)
        button1.bind(on_press=lambda instance, file_name="Zachodnio-Pomorskie.py": self.on_button_press(instance, file_name))
        layout.add_widget(button1)
        button2 = Button(text="Pomorskie", size_hint=(None, None), size=(100, 50),
                         pos=(363.8410513141427, 673.9749582637729), font_size=10)
        button2.bind(on_press=lambda instance, file_name="Pomorskie.py": self.on_button_press(instance, file_name))
        layout.add_widget(button2)

        button3 = Button(text="Warmińsko-Mazurskie", size_hint=(None, None), size=(100, 50),
                         pos=(652.6633291614519, 633.9616026711185), font_size=10)
        button3.bind(on_press=lambda instance, file_name="Warminsko-Mazurskie.py": self.on_button_press(instance, file_name))
        layout.add_widget(button3)

        button4 = Button(text="Lubuskie", size_hint=(None, None), size=(100, 50),
                         pos=(92.52315394242804, 423.89148580968276), font_size=10)
        button4.bind(on_press=lambda instance, file_name="Lubuskie.py": self.on_button_press(instance, file_name))
        layout.add_widget(button4)

        button5 = Button(text="Wielkopolskie", size_hint=(None, None), size=(100, 50),
                         pos=(277.5694618272841, 431.39398998330546), font_size=10)
        button5.bind(on_press=lambda instance, file_name="Wielkopolskie.py": self.on_button_press(instance, file_name))
        layout.add_widget(button5)

        button6 = Button(text="Kujawsko-Pomorskie", size_hint=(None, None), size=(100, 50),
                         pos=(423.8560700876095, 527.6761268781303), font_size=10)
        button6.bind(on_press=lambda instance, file_name="Kujawsko-Pomorskie.py": self.on_button_press(instance, file_name))
        layout.add_widget(button6)

        button7 = Button(text="Mazowieckie", size_hint=(None, None), size=(100, 50),
                         pos=(683.9211514392991, 445.1485809682805), font_size=10)
        button7.bind(on_press=lambda instance, file_name="Mazowieckie.py": self.on_button_press(instance, file_name))
        layout.add_widget(button7)

        button8 = Button(text="Podlaskie", size_hint=(None, None), size=(100, 50),
                         pos=(865.2165206508135, 551.4340567612687), font_size=10)
        button8.bind(on_press=lambda instance, file_name="Podlaskie.py": self.on_button_press(instance, file_name))
        layout.add_widget(button8)

        button9 = Button(text="Dolnośląskie", size_hint=(None, None), size=(100, 50),
                         pos=(201.30037546933667, 275.0918196994991), font_size=10)
        button9.bind(on_press=lambda instance, file_name="Dolnoslaskie.py": self.on_button_press(instance, file_name))
        layout.add_widget(button9)

        button10 = Button(text="Łódzkie", size_hint=(None, None), size=(100, 50),
                          pos=(513.8785982478098, 333.86143572621035), font_size=10)
        button10.bind(on_press=lambda instance, file_name="Lodzkie.py": self.on_button_press(instance, file_name))
        layout.add_widget(button10)

        button11 = Button(text="Lubelskie", size_hint=(None, None), size=(100, 50),
                          pos=(867.7171464330413, 300.10016694490815), font_size=10)
        button11.bind(on_press=lambda instance, file_name="Lubelskie.py": self.on_button_press(instance, file_name))
        layout.add_widget(button11)

        button12 = Button(text="Opolskie", size_hint=(None, None), size=(100, 50),
                          pos=(357.5894868585732, 216.32220367278794), font_size=10)
        button12.bind(on_press=lambda instance, file_name="Opolskie.py": self.on_button_press(instance, file_name))
        layout.add_widget(button12)

        button13 = Button(text="Śląskie", size_hint=(None, None), size=(100, 50),
                          pos=(462.61576971214015, 171.30717863105173), font_size=10)
        button13.bind(on_press=lambda instance, file_name="Slaskie.py": self.on_button_press(instance, file_name))
        layout.add_widget(button13)

        button14 = Button(text="Świętokrzyskie", size_hint=(None, None), size=(100, 50),
                          pos=(655.1639549436796, 230.07679465776295), font_size=10)
        button14.bind(on_press=lambda instance, file_name="Swietokrzyskie.py": self.on_button_press(instance, file_name))
        layout.add_widget(button14)

        button15 = Button(text="Małopolskie", size_hint=(None, None), size=(100, 50),
                          pos=(593.898623279099, 101.28380634390652), font_size=10)
        button15.bind(on_press=lambda instance, file_name="Malopolskie.py": self.on_button_press(instance, file_name))

        layout.add_widget(button15)

        button16 = Button(text="Podkarpackie", size_hint=(None, None), size=(100, 50),
                          pos=(795.1989987484355, 118.78964941569285), font_size=10)
        button16.bind(on_press=lambda instance, file_name="Podkarpackie.py": self.on_button_press(instance, file_name))

        layout.add_widget(button16)



        # Dodajemy etykietę i przycisk do layout
        layout.add_widget(label)
        layout.add_widget(exit_button)
        # Ustawiamy funkcje obsługi zdarzeń
        exit_button.bind(on_press=self.exit_app)
        map_image.bind(on_touch_down=self.on_map_click)

        return layout

    def exit_app(self, instance):
        # Funkcja wywoływana po kliknięciu na przycisku "Exit"
        App.get_running_app().stop()

    def on_map_click(self, instance, touch):
        # Funkcja wywoływana po kliknięciu na obszarze mapy
        if touch.is_double_tap:
            popup = Popup(title='Kliknięcie na mapie',
                          content=Label(text='Przechodzenie do innej strony!'),
                          size_hint=(None, None), size=(400, 200))
            popup.open()
            call(["python", "Podkarpackie.py"])

if __name__ == '__main__':
    MapApp().run()
