from tkinter import ttk

from src.styles import STYLES


def create_label(container, text, style):
    """
    Crea una etiqueta (label) con el estilo especificado.

    :param container: El contenedor donde se colocará la etiqueta.
    :param text: El texto que se mostrará en la etiqueta.
    :param style: El estilo que se aplicará a la etiqueta.
    :return: Un objeto ttk.Label con el texto y estilo especificados.
    """
    imported_style = STYLES.get(style, {})
    return ttk.Label(container, text=text, **imported_style)


def create_combobox(container, values, textvariable, style):
    """
    Crea un combobox con el estilo especificado.

    :param container: El contenedor donde se colocará el combobox.
    :param values: Los valores que se mostrarán en el combobox.
    :param textvariable: La variable de texto asociada al combobox.
    :param style: El estilo que se aplicará al combobox.
    :return: Un objeto ttk.Combobox con los valores, variable de texto y estilo especificados.
    """
    imported_style = STYLES.get(style, {})
    combobox = ttk.Combobox(container, values=values, textvariable=textvariable, **imported_style)
    combobox.current(0)
    return combobox
