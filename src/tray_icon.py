import pystray
from PIL import Image


class TrayIcon:

    def __init__(self):
        self.tray = pystray.Icon("network tray", menu=self.create_menu())
        self.tray.icon = self.load_image("media/icon.jpeg")

        self.tray.run()

    def create_menu(self):
        return pystray.Menu(pystray.MenuItem("Download", action=None), pystray.MenuItem(
            "Upload", action=None), pystray.MenuItem("Quit", action=self.quit))

    def quit(self):
        self.tray.stop()

    def load_image(self, path):
        return Image.open(path)


TrayIcon()
