
infile_name = 'emotion_analysis_common_annotation.csv'
outfile_name = 'annotated.csv'

import csv
import sys
import dbm
from tkinter import *

cat_save = dbm.open('catsave',flag='c')
previndex = None



def load():
    savefile = open(infile_name)
    reader = csv.reader(savefile, delimiter=';')
    key = 0
    for save in reader:
        cat_save[str(key)]=';'.join(save)

        key += 1
    update()

def save():
    savefile = open(outfile_name, 'w')
    for key in cat_save.keys():
        savefile.write(cat_save[key.decode("utf-8")].decode("utf-8") + '\n')



def update():
    listbox.delete(0,END)
    for key in cat_save.keys():
        decoded = cat_save[key.decode("utf-8")].decode("utf-8").split(";")
        listbox.insert(END, decoded[0])
        if decoded[3] != '':
            listbox.itemconfig(END,bg='green')
        else:
            listbox.itemconfig(END, bg='gray')

def on_choosing_label(label: str):

    try:
        if listbox.size()>0:
            index = int(listbox.curselection()[0])
            temp = cat_save[str(index)].decode("utf-8").split(";")
            temp[3]= label
            cat_save[str(index)]=';'.join(temp)
            listbox.itemconfig(index, bg='green')
    except :
        pass


def on_fear():
    on_choosing_label('fear')

def on_anger():
    on_choosing_label('anger')

def on_joy():
    on_choosing_label('joy')

def on_shock():
    on_choosing_label('shock')

def on_none():
    on_choosing_label('none')




def onselect(item):
    if listbox.size()>0:
        global previndex

        index = int(listbox.curselection()[0])
        if previndex != None:
            updatetemp = cat_save[str(previndex)].decode("utf-8").split(";")
            print(updatetemp)
            updatetemp[4] = entry_comment.get(1.0,END).strip('\n')
            cat_save[str(previndex)] = ';'.join(updatetemp)

        previndex = index




        entry_comment.delete(0.0,END)
        entry_comment.insert(1.0,cat_save[str(index)].decode("utf-8").split(";")[4])
        value = listbox.get(index)
        label_2.config(text=value)




root = Tk()
win = Frame(width=200)
win.pack()
label_1 = Label(win, text='custom annotation tool')
label_1.pack(side=TOP,pady=10)
label_1.config(font=("Courier", 44), width=40)
entry_comment = Text(win, height=3, width=30)
entry_comment.pack(side=BOTTOM,expand=1,fill=X)

listbox = Listbox(win,height=10,width=30)
listbox.pack(side=LEFT,fill=BOTH,pady=10)
listbox.bind('<<ListboxSelect>>', onselect)
scrollbar = Scrollbar(win)
scrollbar.pack(side=LEFT,fill=Y)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

label_2=Label(win, text='this is cat')
label_2.pack(side=BOTTOM,pady=30)
label_2.config(font=("Courier", 30,'bold'), width=50,justify=CENTER,wraplength=800,height=6)




button_label_1 = Button(win,text='fear', command=on_fear, height=4,width=7,font=("Courier", 30,'bold'))
button_label_1.pack(side=LEFT,expand=1,fill=X)
button_label_2 = Button(win,text='joy', command=on_joy, height=4,width=7,font=("Courier", 30,'bold'))
button_label_2.pack(side=LEFT,expand=1,fill=X)
button_label_3 = Button(win,text='anger', command=on_anger, height=4,width=7,font=("Courier", 30,'bold'))
button_label_3.pack(side=LEFT,expand=1,fill=X)
button_label_4 = Button(win,text='shock', command=on_shock, height=4,width=7,font=("Courier", 30,'bold'))
button_label_4.pack(side=LEFT,expand=1,fill=X)
button_label_5 = Button(win,text='none', command=on_none, height=4,width=7,font=("Courier", 30,'bold'))
button_label_5.pack(side=LEFT,expand=1,fill=X)
button_load = Button(root,text='load csv', command=load)
button_load.pack(side=LEFT,expand=1,fill=X)
button_save = Button(root,text='save csv', command=save)
button_save.pack(side=LEFT,expand=1,fill=X)
button_quit = Button(root,text='quit', command=win.quit)
button_quit.pack(side=LEFT,expand=1,fill=X)
root.title('cat')

update()

root.mainloop()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pass
    

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
