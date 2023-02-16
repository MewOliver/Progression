from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter.messagebox import showinfo
from functools import partial

# root window
root = tk.Tk()
root.geometry('400x250')
root.title('Progressbar Demo')
s = ttk.Style()
s.theme_use('clam')
s.configure("red.Horizontal.TProgressbar", foreground='red', background='red')
s.configure("blue.Horizontal.TProgressbar", foreground='blue', background='blue')
s.configure("yellow.Horizontal.TProgressbar", foreground='yellow', background='yellow')
s.configure("green.Horizontal.TProgressbar", foreground='green', background='green')
s.configure("purple.Horizontal.TProgressbar", foreground='purple', background='purple')

root.configure(background='light blue')


fit_lv = 0
soc_lv = 0
min_lv = 0
pro_lv = 0
sel_lv = 0

class quest:
    def __init__(self, name, type, exp, col, row, colour):
        self.name = name
        self.type = type
        self.exp = exp
        self.col = col
        self.row = row
        self.colour = colour

# Functions
def progress(x, stat):
    if stat == 'fitness':
        global fitness_label
        fitness['value'] += x
        if fitness['value'] >= 100:
            x = fitness['value'] - 100
            fitness_lv['text'] = update_lv(stat)
            fitness['value'] = x       
        fitness_label['text'] = update_exp(stat)
    elif stat == 'social':
        global social_label
        social['value'] += x
        if social['value'] >= 100:
            x = social['value'] - 100
            social_lv['text'] = update_lv(stat)
            social['value'] = x  
        social_label['text'] = update_exp(stat)
    elif stat == 'mind':
        global mind_label
        mind['value'] += x
        if mind['value'] >= 100:
            x = mind['value'] - 100
            mind_lv['text'] = update_lv(stat)
            mind['value'] = x  
        mind_label['text'] = update_exp(stat)
    elif stat == 'professional':
        global professional_label
        professional['value'] += x
        if professional['value'] >= 100:
            x = professional['value'] - 100
            professional_lv['text'] = update_lv(stat)
            professional['value'] = x  
        professional_label['text'] = update_exp(stat)
    elif stat == 'self':
        global self_label
        self['value'] += x
        if self['value'] >= 100:
            x = self['value'] - 100
            self_lv['text'] = update_lv(stat)
            self['value'] = x  
        self_label['text'] = update_exp(stat)
        

def update_exp(stat):
    if stat == 'fitness':
        return str(str(int(fitness['value'])) + " Fitness exp")
    elif stat == 'social':
        return str(str(int(social['value'])) + " Social exp")
    elif stat == 'mind':
        return str(str(int(mind['value'])) + " Mind exp")
    elif stat == 'professional':
        return str(str(int(professional['value'])) + " Professional exp")
    elif stat == 'self':
        return str(str(int(self['value'])) + " Self exp")
        
def update_lv(stat):
    global fit_lv
    global soc_lv
    global min_lv
    global pro_lv
    global sel_lv
    if stat == 'fitness':
        fit_lv = fit_lv + 1
        return str("Fitness level: " + str(fit_lv))
    elif stat == 'social':
        soc_lv = soc_lv + 1
        return str("Social level: " + str(soc_lv))
    elif stat == 'mind':
        min_lv = min_lv + 1
        return str("Mind level: " + str(min_lv))
    elif stat == 'professional':
        pro_lv = pro_lv + 1
        return str("Professional level: " + str(pro_lv))
    elif stat == 'self':
        sel_lv = sel_lv + 1
        return str("Self level: " + str(sel_lv))

# fitness progressbar
fitness = ttk.Progressbar(root, orient='horizontal', mode='determinate', style="blue.Horizontal.TProgressbar", length=350)
fitness.grid(column=0, row=1, padx=10, columnspan=20, pady=20, sticky='w')

# fitness label
fitness_label = ttk.Label(root, text=partial(update_exp, 'fitness'), background='light blue')
fitness_label.grid(column=2, row=0, padx=10, pady=20, sticky='w')

# fitness level
fitness_lv = Button(root, text=partial(update_lv, 'fitness'), bg="blue")
fitness_lv.grid(column=0, row=0, padx=10, pady=20, sticky='w')

# social progressbar
social = ttk.Progressbar(root, orient='horizontal', mode='determinate', style="red.Horizontal.TProgressbar", length=350)
social.grid(column=0, row=3, padx=10, columnspan=20, pady=20, sticky='w')

# social label
social_label = ttk.Label(root, text=partial(update_exp, 'social'), background='light blue')
social_label.grid(column=2, row=2, padx=10, pady=20, sticky='w', columnspan=20)

# social level
social_lv = Button(root, text=partial(update_lv, 'social'), bg="red")
social_lv.grid(column=0, row=2, padx=10, pady=20, sticky='w', columnspan=20)

# mind progressbar
mind = ttk.Progressbar(root, orient='horizontal', mode='determinate', style="yellow.Horizontal.TProgressbar", length=350)
mind.grid(column=0, row=5, padx=10, columnspan=20, pady=20, sticky='w')

# mind label
mind_label = ttk.Label(root, text=partial(update_exp, 'mind'), background='light blue')
mind_label.grid(column=2, row=4, padx=10, pady=20, sticky='w')

# mind level
mind_lv = Button(root, text=partial(update_lv, 'mind'), bg="yellow")
mind_lv.grid(column=0, row=4, padx=10, pady=20, sticky='w')

# professional progressbar
professional = ttk.Progressbar(root, orient='horizontal', mode='determinate', style="green.Horizontal.TProgressbar", length=350)
professional.grid(column=0, row=7, padx=10, columnspan=20, pady=20, sticky='w')

# professional label
professional_label = ttk.Label(root, text=partial(update_exp, 'professional'), background='light blue')
professional_label.grid(column=2, row=6, padx=10, pady=20, sticky='w')

# professional level
professional_lv = Button(root, text=partial(update_lv, 'professional'), bg="green")
professional_lv.grid(column=0, row=6, padx=10, pady=20, sticky='w')

# self progressbar
self = ttk.Progressbar(root, orient='horizontal', mode='determinate', style="purple.Horizontal.TProgressbar", length=350)
self.grid(column=0, row=9, padx=10, columnspan=20, pady=20, sticky='w')

# self label
self_label = ttk.Label(root, text=partial(update_exp, 'self'), background='light blue')
self_label.grid(column=2, row=8, padx=10, pady=20, sticky='w')

# self level
self_lv = Button(root, text=partial(update_lv, 'self'), bg="purple")
self_lv.grid(column=0, row=8, padx=10, pady=20, sticky='w')

# text box
TextB = Text(root, height = 25, width = 60)
TextB.place(x=800, y=130)

#save button 
save = tk.Button(root, text='Save', font= ('Helvetica 15'))
save.place(x=1020, y=555)

#journal lable
journal = ttk.Label(root, text='Journal', font= ('Helvetica 30 bold italic'), background='light blue')
journal.place(x=980, y=70)

fitness_1 = quest('Run 10km', 'fitness', 50, 11, 0, '#879FFF')
fitness_2 = quest('10 Push-ups', 'fitness', 5, 13, 0, '#879FFF')
fitness_3 = quest('10 sit-ups', 'fitness', 5, 13, 0, '#879FFF')
social_1 = quest('Talk to someone new', 'social', 80, 11, 2, '#FF7777')
social_2 = quest('Check up on a friend', 'social', 50, 13, 2, '#FF7777')
mind_1 = quest('Read for 30mins', 'mind', 20, 11, 4, '#F6FF87')
mind_2 = quest('Complete a puzzle', 'mind', 90, 13, 4, '#F6FF87')
professional_1 = quest('Research potential careers', 'professional', 40, 11, 6,'#9CFF77')
professional_2 = quest('Learn a skill related to your area of passion', 'professional', 100, 13, 6, '#9CFF77')
self_1 = quest('Write down everything you are greatful for', 'self', 50, 11, 8, '#DE77FF')
self_2 = quest('Do one random act of kindness', 'self', 60, 13, 8, '#DE77FF')

quests = (fitness_1, fitness_2, social_1, social_2, mind_1, mind_2, professional_1, professional_2, self_1, self_2)
print(quests)
for i in quests:
    tk.Button(root, text=str(i.name) + "\nexp: "+ str(i.exp), command=partial(progress, i.exp, i.type), background=i.colour).grid(column=i.col, row=i.row, padx=10, pady=20, sticky="n")

root.mainloop()
