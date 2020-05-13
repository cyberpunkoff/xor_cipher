from tkinter import *

# creting main window
root = Tk()
root.title('XOR_cipher')
try:
    root.iconbitmap('favicon.ico')
except TclError:
    print("Icon not found!")
root.geometry("300x120")
root.resizable(False, False)

#creating frames for a good look
frame1 = Frame(root)
frame2 = Frame(root)
frame3 = Frame(frame2)
frame4 = Frame(frame2)

# creating widgets
phrase = Entry(frame1, width = 50, bd = 3)
passcode = Entry(frame1, width = 50, show = '*', bd = 3)
encrypt = Button(frame3, text = 'Encrypt', width = 20, height = 2)
decrypt = Button(frame3, text = 'Decrypt', width = 20, height = 2)
output = Text(frame4)

# default values
phrase.insert(0, "Your phrase here")
passcode.insert(0, "Passcode")

# encryption/decryption part
def XOR_encrypt(event):
    some_str = phrase.get()
    key = passcode.get()
    key_bin = sum(ord(x) for x in key)
    newXORstr = ''.join([chr(ord(i) ^ key_bin) for i in some_str])

    phrase.delete(0, END)
    phrase.insert(0, newXORstr)
    output.configure(state = 'normal')
    output.delete(1.0, END)
    output.insert(1.0, newXORstr)
    output.tag_add('modify', 1.0, '1.end')
    output.tag_config('modify', font = ('Segoe UI', -24, 'normal'), justify = CENTER)
    output.configure(state = 'disabled')

def XOR_decrypt(event):
    some_str = phrase.get()
    key = passcode.get()
    key_bin = sum(ord(x) for x in key)
    newXORstr = ''.join([chr(ord(i) ^ key_bin) for i in some_str])

    phrase.delete(0, END)
    phrase.insert(0, newXORstr)
    output.configure(state = 'normal')
    output.delete(1.0, END)
    output.insert(1.0, newXORstr)
    output.tag_add('modify', 1.0, '1.end')
    output.tag_config('modify', font = ('Segoe UI', -24, 'normal'), justify = CENTER)
    output.configure(state = 'disabled')

# binding buttons
encrypt.bind('<Button-1>', XOR_encrypt)
decrypt.bind('<Button-1>', XOR_decrypt)

# making everything visiable
frame1.pack(side = 'top')
frame2.pack(side = 'bottom')
frame3.pack(side = 'top')
frame4.pack(side = 'bottom')
phrase.pack(side = 'top')
passcode.pack(side = 'bottom')
encrypt.pack(side = 'left')
decrypt.pack(side = 'right')
output.pack()
mainloop()
