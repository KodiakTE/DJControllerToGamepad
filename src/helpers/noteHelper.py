import vgamepad as vg
class noteHelper:
    def __init__(self, gamepad):
        self._gamepad = gamepad
        self._leftJoyUp = False
        self._leftJoyDown = False
        self._leftJoyLeft = False
        self._leftJoyRight = False
        self.leftJoystickNotes = set([1, 5, 4, 6])
        self.__noteMappings = {
            52: vg.XUSB_BUTTON.XUSB_GAMEPAD_A,
            48: vg.XUSB_BUTTON.XUSB_GAMEPAD_B,
            53: vg.XUSB_BUTTON.XUSB_GAMEPAD_X,
            49: vg.XUSB_BUTTON.XUSB_GAMEPAD_Y,
            50: vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP,
            54: vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN,
            51: vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT,
            55: vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT,
            65: vg.XUSB_BUTTON.XUSB_GAMEPAD_GUIDE,
            73: vg.XUSB_BUTTON.XUSB_GAMEPAD_START,
            72: vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK
        }
        self.__noteAndChannelMappings = {
            63: (vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB, vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB),
            12: (vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER, vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
        }
    
    def noteOnMap(self, midiMsg):
        #Bring to Joystick Handler
        if(midiMsg.note in self.leftJoystickNotes):
            self.__leftJoystickHandler(midiMsg)
        if(midiMsg.note in self.__noteMappings and not ((midiMsg.note == 54 and midiMsg.channel == 0) or (midiMsg.note == 54 and midiMsg.channel == 1))): #Extra note logic here to avoid collision with deck spinner
            self.__noteToButton(midiMsg.note, midiMsg.velocity)
        if(midiMsg.note in self.__noteAndChannelMappings):
            self.__noteAndChannelToButton(midiMsg.note, midiMsg.channel, midiMsg.velocity)

    def __noteToButton(self, note:int, velocity:int):
        button = self.__noteMappings[note]
        self.__noteButtonPress(velocity, button)

    def __noteAndChannelToButton(self, note:int, channel:int, velocity:int):
        button = self.__noteAndChannelMappings[note][channel]
        self.__noteButtonPress(velocity, button)
    
    def __noteButtonPress(self, velocity:int, button):
        if(velocity == 127):
            self._gamepad.press_button(button=button)
            print(f"Press: {button=}")
        if(velocity == 0):
            self._gamepad.release_button(button = button)
            print(f"Release: {button=}")

    def __leftJoystickHandler(self, midiMsg):
        # LEFT JOYSTICK
        # Up
        if(midiMsg.note == 1 and midiMsg.velocity == 127):
            self._leftJoyUp = True
            print("Left Joystick Up press")
        if(midiMsg.note == 1 and midiMsg.velocity == 0):
            self._leftJoyUp = False
            print("Left Joystick Up release")
        #Down
        if(midiMsg.note == 5 and midiMsg.velocity == 127):
            self._leftJoyDown = True
            print("Left Joystick Down press")
        if(midiMsg.note == 5 and midiMsg.velocity == 0):
            self._leftJoyDown = False
            print("Left Joystick Down release")
        #Left
        if(midiMsg.note == 4 and midiMsg.velocity == 127):
            self._leftJoyLeft = True
            print("Left Joystick Left press")
        if(midiMsg.note == 4 and midiMsg.velocity == 0):
            self._leftJoyLeft = False
            print("Left Joystick Left release")
        #Right
        if(midiMsg.note == 6 and midiMsg.velocity == 127):
            self._leftJoyRight = True
            print("Left Joystick Right press")
        if(midiMsg.note == 6 and midiMsg.velocity == 0):
            self._leftJoyRight = False
            print("Left Joystick Right release")
        
        x = 0
        y = 0
        if(self._leftJoyUp):
            y += 32767
        if(self._leftJoyDown):
            y -= 32767
        if(self._leftJoyRight):
            x += 32767
        if(self._leftJoyLeft):
            x -= 32767
        self._gamepad.left_joystick(x_value=x, y_value=y)