import pyautogui
from appJar import gui


# handle button events
def press(button):
    if button == "Cancel":
        app.stop()
    if button == "Submit":
        amount = int(app.getEntry("amount"))
        button = app.radioButton("click")
        pyautogui.sleep(1)

        if button == "Right Click":
            button = "right"
        else:
            button = "left"
        for _ in range(amount):
            pyautogui.click(button=button)


# create a GUI variable called app
app = gui("Autoclicker", "300x200", bg='#eeeeee', font={'size':18})

# add & configure widgets - widgets get a name, to help referencing them later
app.label("Enter amount of clicks", row=0)
app.entry("amount", label=True, row=1)
app.setSticky("e")
app.radioButton("click", "Right Click", row=2)
app.setSticky("w")
app.radioButton("click", "Left Click", row=2)


# link the buttons to the function called press
app.addButtons(["Cancel", "Submit"], press, row=3)


# start the GUI
app.go()
