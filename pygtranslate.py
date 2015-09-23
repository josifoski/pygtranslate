#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# created by Aleksandar Josifoski about.me/josifsk 2015-september
import sys
import goslate
import codecs
from tkinter.font import *
from tkinter import *
from tkinter.ttk import Combobox
import sys

langtoshort = { "Afrikaans":"af", "Albanian":"sq", "Arabic":"ar", "Azerbaijani":"az", "Basque":"eu", "Bengali":"bn", "Belarusian":"be",
"Bulgarian":"bg", "Catalan":"ca", "Chinese Simplified":"zh-CN", "Chinese Traditional":"zh-TW", "Croatian":"hr", "Czech":"cs", "Danish":"da",
"Dutch":"nl", "English":"en", "Esperanto":"eo", "Estonian":"et", "Filipino":"tl", "Finnish":"fi", "French":"fr", "Galician":"gl",
"Georgian":"ka", "German":"de", "Greek":"el", "Gujarati":"gu", "Haitian Creole":"ht", "Hebrew":"iw", "Hindi":"hi", "Hungarian":"hu",
"Icelandic":"is", "Indonesian":"id", "Irish":"ga", "Italian":"it", "Japanese":"ja", "Kannada":"kn", "Korean":"ko", "Latin":"la",
"Latvian":"lv", "Lithuanian":"lt", "Macedonian":"mk", "Malay":"ms", "Maltese":"mt", "Norwegian":"no", "Persian":"fa", "Polish":"pl",
"Portuguese":"pt", "Romanian":"ro", "Russian":"ru", "Serbian":"sr", "Slovak":"sk", "Slovenian":"sl", "Spanish":"es", "Swahili":"sw",
"Swedish":"sv", "Tamil":"ta", "Telugu":"te", "Thai":"th", "Turkish":"tr", "Ukrainian":"uk", "Urdu":"ur", "Vietnamese":"vi",
"Welsh":"cy", "Yiddish":"yi" }

langtupple = [ "Afrikaans", "Albanian", "Arabic", "Azerbaijani", "Basque", "Bengali", "Belarusian", "Bulgarian", "Catalan", "Chinese Simplified",
"Chinese Traditional", "Croatian", "Czech", "Danish", "Dutch", "English", "Esperanto", "Estonian", "Filipino", "Finnish", "French", "Galician",
"Georgian", "German", "Greek", "Gujarati", "Haitian Creole", "Hebrew", "Hindi", "Hungarian", "Icelandic", "Indonesian", "Irish", "Italian",
"Japanese", "Kannada", "Korean", "Latin", "Latvian", "Lithuanian", "Macedonian", "Malay", "Maltese", "Norwegian", "Persian", "Polish",
"Portuguese", "Romanian", "Russian", "Serbian", "Slovak", "Slovenian", "Spanish", "Swahili", "Swedish", "Tamil", "Telugu", "Thai",
"Turkish", "Ukrainian", "Urdu", "Vietnamese", "Welsh", "Yiddish" ]

class StatusBar(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.label = Label(self, bd=1, relief=SUNKEN, anchor=W)
        self.label.pack(fill=X)

    def set(self, format, *args):
        self.label.config(text=format % args)
        self.label.update_idletasks()

    def clear(self):
        self.label.config(text="")
        self.label.update_idletasks()

def firstlanguage(*args):
    first = combo1.get()

def secondlanguage(*args):
    second = combo2.get()

def translate(*args):
    iinput = textbox.get("1.0",END)
    ffrom = combo1.get()
    to = combo2.get()
    textbox.insert(END, '\n\n' + gs.translate(iinput, langtoshort[to], langtoshort[ffrom]))

def clear(*args):
    textbox.delete(1.0, END)

def paste(*args):
    cljipboard = root.clipboard_get()
    textbox.insert("insert", cljipboard)

def en2mk(*args):
    combo1.set('English')
    combo2.set('Macedonian')

def  mk2en(*args):
    combo1.set('Macedonian')
    combo2.set('English')

def  en2sr(*args):
    combo1.set('English')
    combo2.set('Serbian')

def spell(*args):
    if dicton:
        global words
        lwrongs = []
        lwrongsind = []
        s = textbox.get("1.0",END)
        textbox.delete(1.0, END)
        textbox.insert("insert", s.rstrip())
        ln = s.split('\n')
        for lineind in range(len(ln)):
            ls = ln[lineind].split()
            for wordind in range(len(ls)):
                if ls[wordind].lower().strip('!"&\'()*,-./:;?[\]_{}«·»‑–—―‖‘’“”…′ \n#') not in words:
                    #lwrongsind.append(wordind)
                    lwrongs.append(ls[wordind])

            for bart in lwrongs:
                #leftind = s.find(bart)
                #textbox.tag_add("red", "1." + str(leftind), "1."+str(leftind + len(bart)))
                try:
                    lsequence = []
                    lsequence = [m.start() for m in re.finditer(bart, ln[lineind])]
                    for micko in lsequence:
                        textbox.tag_add("red", str(lineind + 1) + "." + str(micko), str(lineind + 1) + "." + str(micko + len(bart)))

                except:
                    pass


def handler():
    global sv
    sv.close()
    root.destroy()
    sys.exit(0)

def saving(*args):
    global sv
    s = textbox.get("1.0",END)
    sv.write(s + '\n')
    sv.write('----------\n')

gs = goslate.Goslate()

sv = codecs.open('pygtranslate_saved.txt', 'a', 'utf-8')

#using dictionaries for spellcheck
try:
    #words=open("/usr/share/dict/american-english").read().split("\n")
    
    words1=open("/data/python_scripts/pygtranslate/american-english").read().split("\n")
    words2=open("/data/python_scripts/pygtranslate/american-english-myextend").read().split("\n")
    words = words1 + words2
    for itemind in range(len(words)):
        words[itemind] = words[itemind].lower()
    
    dicton = True
except:
    dicton = False

#print(dicton)

root = Tk()
root.title("py google translator")

bfr=Frame(root)
tfr=Frame(root)

root.bind('<Control-Key-r>', translate)
root.bind('<Control-Key-s>', saving)

button4 = Button(bfr, text='en2mk', command=en2mk)
button4.pack(side=LEFT)

button5 = Button(bfr, text='mk2en', command=mk2en)
button5.pack(side=LEFT)

button6 = Button(bfr, text='en2sr', command=en2sr)
button6.pack(side=LEFT)

combovar1 = langtupple
combo1 = Combobox(bfr)
combo1['values']=combovar1
combo1.set('English')
combo1.bind('<<ComboboxSelected>>', firstlanguage)
combo1.pack(side=LEFT)

combovar2 = langtupple
combo2 = Combobox(bfr)
combo2['values']=combovar2
combo2.set('Macedonian')
combo2.bind('<<ComboboxSelected>>', secondlanguage)
combo2.pack(side=LEFT)

button1 = Button(bfr, text='paste', command=paste)
button1.pack(side=LEFT)

button2 = Button(bfr, text='clear', command=clear)
button2.pack(side=LEFT)

button7 = Button(bfr, text='spell', command=spell)
button7.pack(side=LEFT)

button3 = Button(bfr, text='translate', command=translate)
button3.pack(side=LEFT)

status = StatusBar(root)
status.pack(side=BOTTOM, fill=X)
S = Scrollbar(tfr)
S.pack(side=RIGHT, fill=Y)
customFont = Font(family="Helvetica", size=14 )
#textbox = Text(tfr, wrap=WORD, font=customFont, bg='white') #width=60
textbox = Text(tfr, wrap=WORD, font=customFont) #width=60
textbox.pack(expand = 1, fill='both') #side=LEFT
S.config(command=textbox.yview)
textbox.config(yscrollcommand=S.set)
textbox.tag_config("red", foreground="red")

bfr.pack(side=TOP,anchor=W)
tfr.pack(side=BOTTOM, expand=1, fill='both')
textbox.focus()

root.geometry('850x500+300+100')
root.protocol("WM_DELETE_WINDOW", handler)
root.mainloop()



