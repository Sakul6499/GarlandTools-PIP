"""
Wrapper for GarlandTools Icon Endpoint
"""

from .globals import GARLAND_TOOLS_ENDPOINT, SESSION

GARLAND_TOOLS_ICON_ENDPOINT = f'{GARLAND_TOOLS_ENDPOINT}files/icons/'


def icon(type: str, id: int):
    """
    Returns a specific icon by type and id
    """
    result = SESSION.get(f'{GARLAND_TOOLS_ICON_ENDPOINT}{type}/{id}.png')
    return result