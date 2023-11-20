from tkinter import Canvas

# https://stackoverflow.com/questions/22835289/how-to-get-tkinter-canvas-to-dynamically-resize-to-window-width


class ResizingCanvas(Canvas):
    def __init__(self, parent, **kwargs):
        Canvas.__init__(self, parent, **kwargs)

    def on_resize(self, event=None):
        wscale = (
            self.master.winfo_width() / 1000 + self.master.winfo_height() / 1000
        ) * 2
        self.scale("all", 0, 0, wscale, wscale)
