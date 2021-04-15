import tkinter
from tkinter import *
import random
#list of questions
questions = [ 'Dipole antenna is symmetrical in nature where the two ends are at equal potentials with respect to ___point',
              'On which factor/s do/does the radiation field of a small loop depend?',
              'In the solutions of inhomogeneous vector potential wave equation, which component exists if the source is at origin and the points are removed from the source (Jz = 0)?',
              'In retarded potentials, what factor of time delay is generally introduced in A & V equations?',
              'The vector magnetic potential shows the inverse relationship with its ?',
              'Sterdian is a measurement unit of ?',
              'What would happen if the rms value of induced emf in loop acquires an angle θ = 90°?',
              ' Which conversion mechanism is performed by parabolic reflector antenna',
              'I Which type of wire antennas are also known as dipoles?',
              'Which among the following plays a primary role in generation of conduction current in an ionosphere due to presence of electric field?']

#list of options
answers = [['last', 'intial', 'mid', 'none'],
           ['Shape', 'Area', 'Both A & B', 'None of the above'],
           ['OUTWARDS', 'inwards', 'none', 'All of the above'],
           [' R + c','R-C', 'R/C', 'NONE'],
           ['Distance of point from the source (R)', 'Normal E-region', 'Sporadic E-region', 'Distance of point from the source (R)'],
           ['solid angle', ' 90° & 180°', '180° & 270°', '180° & 360°'],
           ['Wave is incident in direction of plane of the loop with induced maximum voltage', 'Wave is incident normal to plane of the loop with no induced voltage', 'Wave is incident in opposite direction of plane of the loop with minimum voltage','none of the above'],
           ['Plane to spherical wave', 'Spherical to plane wave', 'Spherical to Sherical wave', 'none'],    
           ['Linear', 'Loop', 'Helical', 'All of the above'],
           [' Ions', 'Motion of electrons', 'Neutral molecules', 'None of the above']]

rightanswers=[2,1,0,0,0,0,1,1,0,1]  #correct answers

userselected =[]
index =[]
# order of the questions are changed here

def generate():
    global index
    while(len(index) < 10):
        x = random.randint(0,9)
        if x in index:
            continue
        else:
            index.append(x)

#result display
def result(score):
    question.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    end=Label(root, text=(f'Your score was',score), bg='#ffffff', font=('Britannic', 30))
    end.pack(pady=100)

#score calculation
def calculate():
    global index, userselected, rightanswers
    x=0
    score=0
    for i in index:
        if userselected[x] == rightanswers[i]:
            score+=1
        x+=1
    result(score)

#when a radio button is selected

ques = 1
def whenselected():
    global radiovar, userselected
    global question, r1, r2, r3, r4
    global ques
    x = radiovar.get()
    userselected.append(x)
    radiovar.set(-1)
    if ques < 10:
        question.config(text= questions[index[ques]])
        r1['text'] = answers[index[ques]][0]
        r2['text'] = answers[index[ques]][1]
        r3['text'] = answers[index[ques]][2]
        r4['text'] = answers[index[ques]][3]
        ques +=1
    else:
        print(index)
        print(userselected)
        calculate()


#quiz questions with radiobutton options

def quizbegins():
    global question, r1, r2, r3, r4
    question = Label(root, text=questions[index[0]], font=('Britannic', 15), bg='#ffffff')
    question.pack(pady=15)
    global radiovar
    radiovar = IntVar()
    radiovar.set(-1)

    r1 = Radiobutton(root, text=answers[index[0]][0], font=('Bold', 15), value=0, variable=radiovar, command= whenselected)
    r1.pack(pady= 15)

    r2 = Radiobutton(root, text=answers[index[0]][1], font=('Bold', 15), value=1, variable=radiovar,command= whenselected)
    r2.pack(pady=15)

    r3 = Radiobutton(root, text=answers[index[0]][2], font=('Bold', 15), value=2, variable=radiovar,command= whenselected)
    r3.pack(pady=15)

    r4 = Radiobutton(root, text=answers[index[0]][3], font=('Bold', 15), value=3, variable=radiovar,command= whenselected)
    r4.pack(pady=15)

#enter button pressed
def when_enter_is_clicked():
    lblname.destroy()
    lblintro.destroy()
    lblenter.destroy()
    enterbutton.destroy()
    generate()
    quizbegins()

#window design
root = tkinter.Tk()

root.geometry('1000x500')
root.title('Quiz Emulator')
root.configure(bg='#ffffff')
root.resizable(0, 0)

lblname = Label(root, text='Quiz master', font=('Bradley Hand ITC', 30), background='#ffffff')
lblname.pack(pady=15)

lblintro = Label(root, background="#ffcccc",
                 text='You will be given a series of 10 questions.\n Once option is selected, you can not undo it.\n So choose wisely.',
                 font=(20))
lblintro.pack(pady=15)

lblenter = Label(root, text='Press enter to proceed', bg='#ffffff', font=(15))
lblenter.pack()
enterbutton = Button(root, text='Enter', width=20, font=('Bold', 15), command=when_enter_is_clicked)
enterbutton.pack(pady=15)

root.mainloop()
