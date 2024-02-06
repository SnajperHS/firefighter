from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label

class PhotoApp(App):
    def build(self):
        # Tworzymy główny layout jako FloatLayout
        layout = FloatLayout()

        # Dodajemy obraz do layout
        self.photo_image = Image(source='mapa.jpg', allow_stretch=True, keep_ratio=False)
        layout.add_widget(self.photo_image)

        # Tworzymy etykietę do wyświetlania współrzędnych
        self.coordinates_label = Label(text='', pos=(0, 0), size_hint=(None, None), size=(300, 50))
        layout.add_widget(self.coordinates_label)

        # Ustawiamy funkcje obsługi zdarzeń
        self.photo_image.bind(on_touch_down=self.on_image_click)

        return layout

    def on_image_click(self, instance, touch):
        # Funkcja wywoływana po kliknięciu na obrazie
        if self.photo_image.collide_point(*touch.pos):
            x, y = touch.pos
            self.coordinates_label.text = f'Współrzędne: x={x}, y={y}'

            # Zapisujemy współrzędne do pliku
            with open('coordinates.txt', 'a') as file:
                file.write(f'{x},{y}\n')

if __name__ == '__main__':
    PhotoApp().run()
