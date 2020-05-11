# convert.py
# IPO or program description

from graphics import *


def main():
    # create a window object
    win = GraphWin("Celsius Converter", 400, 300)

    # create text objects
    celsiusTempString = "Celsius Temperature:   "
    fahrenheightTempString = "Fahrenheit Temperature:"
    input()

    # create Text box
    Text(Point(150, 50), celsiusTempString).draw(win)
    Text(Point(150, 250), fahrenheightTempString).draw(win)

    # create center box
    Rectangle(Point(125, 100), Point(275, 200)).draw(win)

    # create button text
    buttonText = Text(Point(200, 150), "convert it")
    buttonText.draw(win)

    # create input and output fields
    inputCelsiusField = Entry(Point(300, 50), 5)
    inputCelsiusField.setText("0.0")
    inputCelsiusField.draw(win)

    outputFhrenheightFeild = Text(Point(300, 250), "")
    outputFhrenheightFeild.draw(win)

    win.getMouse()

    celsiusTemperature = float(inputCelsiusField.getText())
    farhenheight = 9.0/5.0 * celsiusTemperature + 32

    # display results
    outputFhrenheightFeild.setText(round(farhenheight, 2))

    buttonText.setText("quit")

    win.getMouse()


main()
