class controlChangeHelper:
    def __init__(self, gamepad):
        self._gamepad = gamepad
        self.deadzones = set([63, 64, 65])
        self.rightJoyX = 64
        self.leftJoyY = 64

    def controlChangeMap(self, midiMsg):
        #Left Trigger
        if (midiMsg.channel==2 and midiMsg.control == 19):
            leftTriggerVal = self.__convertSliderTo255(midiMsg.value)
            self._gamepad.left_trigger(leftTriggerVal)
            print(f"Left trigger val: {leftTriggerVal}")
        #Right Trigger
        if (midiMsg.channel==3 and midiMsg.control == 19):
            rightTriggerVal = self.__convertSliderTo255(midiMsg.value)
            self._gamepad.right_trigger(rightTriggerVal)
            print(f"Right trigger val: {rightTriggerVal}")
        #Right Joystick
        if(midiMsg.control in set([34, 33])):
            self.__rightJoystickHandler(midiMsg)
        
    def __rightJoystickHandler(self, midiMsg):
        if (midiMsg.channel == 0):
            self.leftJoyY = midiMsg.value
        if (midiMsg.channel == 1):
            self.rightJoyX = midiMsg.value

        x= self.__convertSpinnerValues(self.rightJoyX)
        y= self.__convertSpinnerValues(self.leftJoyY)

        if (self.leftJoyY in self.deadzones):
            y = 0
        if(self.rightJoyX in self.deadzones):
            x = 0

        print(f"Right Joystick Movement: x={x} y={y} ")
        self._gamepad.right_joystick(x_value=x, y_value=y)


    def __convertSliderTo255(self, num: int) -> int:
        return int((-255/127) * num +255)
    
    def __convertSpinnerValues(self, num: int) -> int:
        spinnerVal = int(1638.35 * num - 104736.4)
        if(spinnerVal > 32767):
            return 32767
        if(spinnerVal < -32768):
            return -32768
        return spinnerVal