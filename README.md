# AutoClicker
-----
Written in Python 3.9, unknown to work in previous Python versions, known to work in python 3.10.0.
-----

This is the guide for the AutoClicker program. It is designed to allow you to to send the mouse to a user specified location and automatically click for a user specified length of time with a user specified click and a user specified length between clicks.

Desired Position:
    This is the position you want your cursor to go to. You can use the Send Mouse button to test coordinates you put in.

Infinite:
    This allows you to run the clicker indefinitely, this can mess with Windows(not tested on Linux yet) and cause more than one program to crash due to the potential speed of the 
    clicks. It is suggested you use this sparingly if ever, it is further suggested to use large time blocks, specifically 5 minutes, if you wish for long periods of clicking.

Double:
    Allows you to make every click the clicker makes to be a double click.

Lengh and Delay:
    These two fields allow you to determine the length of time the clicker runs for(in seconds) and the delay(in milliseconds) between clicks.
    It is suggested you always input some amount of delay as this part can cause a lot of trouble because of how fast undelayed clicks can get.

Current Mouse Position and Setting your Desired Position:
    This nifty button tied to the left control button on your keyboard allows you to set the Desired Position to the Current Mouse Position which is displayed(in pixels)
    above the button.

Choosing which button is clicked:
    Using the drop down menu next to the "Send & Start Clicking" button allows you to select the button on your mouse that the clicker clicks.
    You can choose Left, Middle, and Right.

Send & Start Clicking:
    This button sends your cursor to the desired position and starts the clicker with the settings you input, you can also press Return on your keyboard to use this button.
    Note, the cursor is unlocked, if you move the cursor outside of a 10x10 pixel box then it will stop clicking. As the clicker runs you can press escape at anytime to stop 
    the current execution and regain click control, so long as the windo is in focus. The focus part goes for all of the keybinds.

Emergency quit:
    Should you need to quit, at anytime press both Shift and Escape at the same time and the program should shutdown immediately.

Keybindings:

Left Control: Sets the Desired Position to the Current Mouse Position.
Escape: Stops the clicker during execution.
Shift Escape: Emergency quit, does what it says on the tin.
Return: Presses the Send & Start Clicking button for you.
