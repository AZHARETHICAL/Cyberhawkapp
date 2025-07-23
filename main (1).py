
import os
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput

class CyberHawkApp(App):
    def build(self):
        self.output = TextInput(text='>> CyberHawk Toolkit by Muhammad Azhar\n', readonly=True, background_color=(0,0,0,1), foreground_color=(0,1,0,1), size_hint_y=None, height=400)

        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        layout.add_widget(Label(text='CYBER HAWK TOOLKIT BY MUHAMMAD AZHAR', bold=True, color=(0,1,0,1), size_hint_y=None, height=40))

        scroll = ScrollView(size_hint=(1, None), size=(400, 400))
        scroll.add_widget(self.output)
        layout.add_widget(scroll)

        buttons = [
            ('Network Scan (ifconfig)', 'ifconfig'),
            ('Ping Google', 'ping -c 3 google.com'),
            ('Base64 Encode "Hello"', 'echo Hello | base64'),
            ('Base64 Decode "SGVsbG8="', 'echo SGVsbG8= | base64 -d'),
            ('Hash Identifier', 'hash-identifier'),
            ('Exit', 'exit')
        ]

        for text, command in buttons:
            btn = Button(text=text, size_hint_y=None, height=40, background_color=(0, 0.5, 0, 1))
            btn.bind(on_press=lambda instance, cmd=command: self.run_command(cmd))
            layout.add_widget(btn)

        return layout

    def run_command(self, cmd):
        if cmd == 'exit':
            App.get_running_app().stop()
        else:
            self.output.text += f"$ {cmd}\n"
            try:
                result = os.popen(cmd).read()
                self.output.text += result + '\n'
            except Exception as e:
                self.output.text += f"Error: {str(e)}\n"

if __name__ == '__main__':
    CyberHawkApp().run()
