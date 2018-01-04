import android
from android.widget import LinearLayout, TextView
from .models import manamoneyDB

class MainApp:
    def __init__(self):
        self._activity = android.PythonActivity.setListener(self)
        self.db = manamoneyDB()

    def onCreate(self):
        label = TextView(self._activity)
        label.setTextSize(50)
        label.setText('Hello World')

        vlayout = LinearLayout(self._activity)
        vlayout.setOrientation(LinearLayout.VERTICAL)
        vlayout.addView(label)

        self._activity.setContentView(vlayout)


def main():
    MainApp()
