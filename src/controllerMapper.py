import vgamepad as vg
from helpers.controlChangeHelper import controlChangeHelper
from helpers.noteHelper import noteHelper

class ControlMap:
    def __init__(self, controlchangeHelper, noteHelper):
        self._controlchangeHelper = controlchangeHelper
        self._noteHelper = noteHelper
        
    def mapMidiToGamepad(self, midiMsg):
        if(midiMsg.type == 'note_on'):
            self._noteHelper.noteOnMap(midiMsg)
        if(midiMsg.type == 'control_change'):
            self._controlchangeHelper.controlChangeMap(midiMsg)