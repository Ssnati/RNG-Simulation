from tkinter import ttk

from src.styles import STYLES


def create_label(container, text, style):
    imported_style = STYLES.get(style, {})
    return ttk.Label(container, text=text, **imported_style)
