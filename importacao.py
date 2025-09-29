import os, sys

def resource_path(rel_path):
    """Retorna o caminho absoluto para recurso, compatível com PyInstaller."""
    if getattr(sys, 'frozen', False):  # executável criado pelo PyInstaller
        base_path = sys._MEIPASS       # pasta temporária usada pelo PyInstaller
    else:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, rel_path)
