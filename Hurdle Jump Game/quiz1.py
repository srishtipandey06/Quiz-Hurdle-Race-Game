import tkinter
from tkinter import *
import random
#list of questions
questions = [ 'Which among the following is an application of high frequency?',
              'In which kind of waveform is the phase velocity defined?',
              'Which among the following is/are not present in free space?',
              'Which ionization layer exists during day time & usually vanishes at night due to highest recombination rate?',
              'At which angles does the front to back ratio specify an antenna gain?',
              'According to the geometry, how many sterdians are present in a full sphere?',
              'Which antennas are renowned as patch antennas especially adopted for space craft applications?',
              'Which type of wire antennas are also known as dipoles?',
              'In an electrical circuit,which nature of impedance causes the current & voltages in phase?',
              'Which equations are regarded as wave equations in frequency domain for lossless media?']

#list of options
answers = [['SONAR', 'Subsurface communication', 'Radio navigation', 'Facsimile'],
           ['Sinusoidal', 'Rectangular', 'Square', 'Triangular'],
           ['Solid bodies', 'Ionized particles', 'Interference of normal radiation & radio wave propagation', 'All of the above'],
           ['D-region', 'Normal E-region', 'Sporadic E-region', 'Appleton region'],
           ['0° & 180°', ' 90° & 180°', '180° & 270°', '180° & 360°'],
           ['π/2°', ' π', '2π', '4π'],
           ['Aperture', 'Microstrip', 'Array', 'Lens'],
           ['Linear', 'Loop', 'Helical', 'All of the above'],
           ['Reactive', 'Resistive', 'Capacitive', 'Inductive'],
           ['Maxwell’s', 'Lorentz', 'Helmholtz', 'Poisson’s']]

rightanswers=[3,0,3,0,0,3,1,0,1,2]  #correct answers

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

# def run(score):
#     if score>=5:
#         exec(open("main.py").read(), globals()) 
#     elif score<5:
#         exit()
    

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
#     run(score)

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
