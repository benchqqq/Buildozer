
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

Window.clearcolor = (0.9, 0.9, 0.9, 1)  # لون خلفية النافذة

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # عنوان التطبيق
        title_label = Label(
            text="مرحبًا بك في تطبيق Kivy!",
            font_size=30,
            color=(0, 0, 0.5, 1)  # لون النص (أزرق غامق)
        )

        # حقل إدخال النص
        self.name_input = TextInput(
            hint_text="أدخل اسمك",
            size_hint=(1, 0.2),
            font_size=20,
            background_color=(1, 1, 1, 1),
            foreground_color=(0, 0, 0, 1)
        )

        # زر الإرسال
        submit_button = Button(
            text="تقديم",
            size_hint=(1, 0.2),
            background_color=(0, 0.5, 1, 1),  # لون الزر (أزرق فاتح)
            color=(1, 1, 1, 1)  # لون النص (أبيض)
        )
        submit_button.bind(on_press=self.say_hello)

        # إضافة العناصر إلى الواجهة
        layout.add_widget(title_label)
        layout.add_widget(self.name_input)
        layout.add_widget(submit_button)

        return layout

    def say_hello(self, instance):
        name = self.name_input.text
        if name:
            self.root.clear_widgets()  # مسح الواجهة الحالية
            self.root.add_widget(Label(
                text=f"مرحبًا، {name}!",
                font_size=40,
                color=(0, 0, 0.5, 1)
            ))
        else:
            self.name_input.hint_text = "الرجاء إدخال اسمك!"

if __name__ == "__main__":
    MyApp().run()