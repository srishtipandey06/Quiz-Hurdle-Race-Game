import tkinter
from tkinter import *
import random
#list of questions
questions = [ 'On which factor/s do/does the radiation field of a small loop depend?',
              'Under which conditions of charge does the radiation occur through wire antenna?',
              'On which factor/s do/does the radiation field of a small loop depend?',
              'What is the nature of radiation pattern of an isotropic antenna?',
              'Which mode of propagation is adopted in HF antennas?',
              'Which equations are regarded as wave equations in frequency domain for lossless media?',
              'What is the functioning role of an antenna in receiving mode?',
              'Under which conditions of two unit vectors, the polarization loss factor (PLF) is equal to unity?',
              'What is/are the major applications of an infinitesimal dipole that contribute/s to its analysis?',
              'Which property/ies of antenna is/are likely to be evidenced in accordance to Reciprocity theorem?']

#list of options
answers = [['Shape', 'Area', 'Both A & B', 'None of the above'],
           ['For a charge with no motion', 'For a charge moving with uniform velocity with straight & infinite wire', 'For a charge oscillating in time motion', 'All of the above'],
           ['Shape', 'Area', 'Both A & B', 'None'],
           ['Spherical', 'Dough-nut', 'Elliptical', 'Hyperbolic'],
           ['Ionospheric', 'Ground wave', 'Tropospheric', 'All of the above'],
           ['Maxwell’s', 'Lorentz', 'Helmholtz', 'Poisson’s'],
           ['Radiator', 'Converter', 'Sensor', 'Inverter'],
           ['Perpendicular', 'Perfectly aligned', 'Angle inclination (Ψp)', 'All of the above'],
           ['Field pattern estimation due to any length of antenna', 'Improvement in radiation resistance by increasing dipole length', 'Both a and b', 'None of the above'],
           ['Equality of impedances', 'Equality of directional patterns', 'Equality of effective lengths', 'All of the above']]

rightanswers=[1,2,1,0,0,2,2,1,2,3]  #correct answers

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
