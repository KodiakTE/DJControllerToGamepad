import mido
import vgamepad as vg
from findMidiPort import FindMidiPort
from controllerMapper import ControlMap
from helpers.controlChangeHelper import controlChangeHelper
from helpers.noteHelper import noteHelper

#find MIDI port for DJ Controller
findMidi = FindMidiPort()
port = findMidi.findPort()
#print(port)
input_port = mido.open_input(port)

#Initilize classes (Singleton)
gamepad = vg.VX360Gamepad()
controlchangeHelper = controlChangeHelper(gamepad)
noteHelper = noteHelper(gamepad)
mapper =  ControlMap(controlchangeHelper, noteHelper)

print('Gamepad Has Started')

for msg in input_port:
    #print(msg)
    mapper.mapMidiToGamepad(msg)
    gamepad.update()

    if(msg.type == 'note_on' and msg.note == 101 and msg.velocity == 127):
        break

    