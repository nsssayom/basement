from kivy.app import App
from kivy.uix.button import Button
from kivy.config import Config
from kivy.core.window import Window

Config.set('input', 'mouse', 'mouse,disable_multitouch')

Window.size = (600, 1024)
Window.show_cursor = False
Window.fullscreen = True


class ScrollButton(Button):
    pass


class ScrollApp(App):
    def build(self):
        super(ScrollApp, self).build()
        container = self.root.ids.container
        for i in range(100):
            container.add_widget(ScrollButton(text=str(i)))
        return self.root   # return root does not work


if __name__ == '__main__':
    ScrollApp().run()
