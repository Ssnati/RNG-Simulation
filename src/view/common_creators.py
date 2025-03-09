from tkinter import ttk

from src.styles import STYLES


def create_label(container, text, style):
    imported_style = STYLES.get(style, {})
    return ttk.Label(container, text=text, **imported_style)


def create_combobox(container, values, textvariable, style):
    imported_style = STYLES.get(style, {})
    combobox = ttk.Combobox(container, values=values, textvariable=textvariable, **imported_style)
    combobox.current(0)
    return combobox
