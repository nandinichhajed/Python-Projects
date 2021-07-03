import tkinter
import random
# list of possible colours
colours = ['red', 'blue', 'green', 'pink', 'black',
           'purple', 'white', 'orange', 'yellow', 'brown']
score = 0

# the game time lweft initallyn 30 seconds
timeleft = 30

#  function to start game


def StartGame(event):
    if timeleft == 30:
        # start the countdown timer
        countdown()
    # run function to choose next colour
    nextcolour()


def nextcolour():
    global score
    global timeleft

    # if a game is currently in play
    if timeleft > 0:
        # make the text entry box activate
        e.focus_set()

        # if the colour typed is equal to the colour of the text
        if e.get().lower() == colours[1].lower():
            score += 1

        # clear the text entry box
        e.delete(0, tkinter.END)

        random.shuffle(colours)
        label.config(fg=str(colours[1]), text=str(colours[0]))
        # update the score
        scoreLabel.config(text='score:' + str(score))


def countdown():
    global timeleft
    #  if the game is in play
    if timeleft > 0:
        # decrement the timer
        timeleft -= 1
        # update the time left label.
        timeLabel.config(text='Time Left: ' + str(timeleft))
        # run the function again after 1 second.
        timeLabel.after(1000, countdown)


# creatng a GUI window
root = tkinter.Tk()

# set the title
root.title('Colour Game')

# Set the size
root.geometry('800x400')

# add an instruction lable
instructions = tkinter.Label(
    root, text='Type in the Colour of the Words, and not the Word Text!', font=('Times New Roman', 24))
instructions.pack()

# add a score lable
scoreLabel = tkinter.Label(
    root, text='Press Enter To Start:', font=('Times New Roman', 24))
scoreLabel.pack()

# add a timeleft lable
# timeLabel = tkinter.Label(root, text='Time left:' +
#                           str(timeleft), font=('Times New Roman', 24))

timeLabel = tkinter.Label(
    root, text=f'Total Time: {timeleft} seconds', font=('Times New Roman', 24))
timeLabel.pack()

# add a lable for displaying the colours
label = tkinter.Label(root, font=('Times New Roman', 20))
label.pack()

# add the text enter box for displaying the colours
e = tkinter.Entry()

#  run the star functiion when the enter key is pressed
root.bind('<Return>', StartGame)
e.pack()

#  set focus on the entry box
e.focus_set()

#  start the GUI
root.mainloop()
