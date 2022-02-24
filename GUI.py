from tkinter import *
from tkinter import messagebox

from Atbash import *
from Vernam import *
from Vigenere import *
from RC4 import *
from conversor import *

# Main window
base = Tk()
base.title('Cifrado')
base.resizable(False, False)
base.geometry('500x400')

# Main Frame
MainFrame = Frame(base, bg='#232426')
MainFrame.place(x=0, y=0, width=500, height=400)
Mfbar = Canvas(MainFrame, width=500, height=65, bg='#2a2b2d', highlightthickness=0)
Mfbar.place(x=0, y=335)
# Buttons
MfRC4 = Button(MainFrame, text='RC4', command=lambda: show('RC4'))
MfRC4.place(x=30, y=30)
MfRC4.configure(background='#04BF68', foreground='#155939', borderwidth=0, activebackground='#232426', pady=5, padx=10, width=10)
MfAtbash = Button(MainFrame, text='Atbash', command=lambda: show('Atbash'))
MfAtbash.place(x=30, y=80)
MfAtbash.configure(background='#04BF68', foreground='#155939', borderwidth=0, activebackground='#232426', pady=5, padx=10, width=10)
MfVernam = Button(MainFrame, text='Vernam', command=lambda: show('Vernam'))
MfVernam.place(x=30, y=130)
MfVernam.configure(background='#04BF68', foreground='#155939', borderwidth=0, activebackground='#232426', pady=5, padx=10, width=10)
MfVigenere = Button(MainFrame, text='Vigenere', command=lambda: show('Vigenere'))
MfVigenere.place(x=30, y=180)
MfVigenere.configure(background='#04BF68', foreground='#155939', borderwidth=0, activebackground='#232426', pady=5, padx=10, width=10)
MfConversor = Button(MainFrame, text='Conversor', command=lambda: show('Conversor'))
MfConversor.place(x=30, y=230)
MfConversor.configure(background='#04BF68', foreground='#155939', borderwidth=0, activebackground='#232426', pady=5, padx=10, width=10)

AtbashFrame = Frame(base, bg='#232426')
AtbashFrame.place(x=0, y=0, width=500, height=400)
ABBar = Canvas(AtbashFrame, width=500, height=65, bg='#2a2b2d', highlightthickness=0)
ABBar.place(x=0, y=335)
ABinputTextLabel = Label(AtbashFrame, text='Input Text')
ABinputTextLabel.place(x=30, y=30)
ABinputTextLabel.configure(background='#232426', foreground='#F2F2F2')
ABoutputTextLabel = Label(AtbashFrame, text='Output Text')
ABoutputTextLabel.place(x=30, y=170)
ABoutputTextLabel.configure(background='#232426', foreground='#BFBFBD')
ABinputText = Text(AtbashFrame, width=50, height=5)
ABinputText.place(x=20, y=60)
ABinputText.configure(background='#04BF68', foreground='#232426', borderwidth=0)
ABoutputText = Text(AtbashFrame, width=50, height=5)
ABoutputText.place(x=20, y=200)
ABoutputText.config(state=DISABLED, bg='#155939', fg='#BFBFBF', borderwidth=0)
ABBack = Button(AtbashFrame, text='<', command=lambda: show('Home'))
ABBack.place(x=20, y=355)
ABBack.configure(background='#04BF68', foreground='#155939', borderwidth=0, activebackground='#232426', pady=5, padx=10)
ABEncrypt = Button(AtbashFrame, text='Convert', command=lambda: GUI_atbash('convert'))
ABEncrypt.place(x=70, y=355)
ABEncrypt.configure(background='#04BF68', foreground='#155939', borderwidth=0, activebackground='#232426', pady=5, padx=10)
ABClear = Button(AtbashFrame, text='Clear', command=lambda: GUI_atbash('clear'))
ABClear.place(x=410, y=355)
ABClear.configure(background='#04BF68', foreground='#155939', borderwidth=0, activebackground='#232426', pady=5, padx=10)

VernamFrame = Frame(base, bg='#232426')
VernamFrame.place(x=0, y=0, width=500, height=400)
VNBar = Canvas(VernamFrame, width=500, height=65, bg='#2a2b2d', highlightthickness=0)
VNBar.place(x=0, y=335)
VNSize = StringVar()
VNSize.set('Bin size: 0')
VNinputTextLabel = Label(VernamFrame, text='Input Text')
VNinputTextLabel.place(x=30, y=30)
VNinputTextLabel.configure(background='#232426', foreground='#F2F2F2')
VNinputTextBinLabel = Label(VernamFrame, text='Input Text (Bin)')
VNinputTextBinLabel.place(x=280, y=30)
VNinputTextBinLabel.configure(background='#232426', foreground='#BFBFBF')
VNkeyTextLabel = Label(VernamFrame, text='Key')
VNkeyTextLabel.place(x=30, y=130)
VNkeyTextLabel.configure(background='#232426', foreground='#F2F2F2')
VNkeyTextBinLabel = Label(VernamFrame, text='Key (Bin)')
VNkeyTextBinLabel.place(x=280, y=130)
VNkeyTextBinLabel.configure(background='#232426', foreground='#BFBFBD')
VNoutputTextLabel = Label(VernamFrame, text='Output Text')
VNoutputTextLabel.place(x=30, y=230)
VNoutputTextLabel.configure(background='#232426', foreground='#BFBFBD')
VNoutputTextBinLabel = Label(VernamFrame, text='Output Text (Bin)')
VNoutputTextBinLabel.place(x=280, y=230)
VNoutputTextBinLabel.configure(background='#232426', foreground='#BFBFBD')
VNsizeLabel = Label(VernamFrame, textvariable=VNSize)
VNsizeLabel.place(x=230, y=360)
VNsizeLabel.configure(background='#2a2b2d', foreground='#BFBFBD')
VNinputText = Text(VernamFrame, width=25, height=3)
VNinputText.place(x=20, y=60)
VNinputText.configure(background='#04BF68', foreground='#232426', borderwidth=0)
VNinputTextBin = Text(VernamFrame, width=25, height=3)
VNinputTextBin.place(x=270, y=60)
VNinputTextBin.config(state=DISABLED, bg='#155939', fg='#BFBFBF', borderwidth=0)
VNkeyText = Text(VernamFrame, width=25, height=3)
VNkeyText.place(x=20, y=160)
VNkeyText.configure(background='#04BF68', foreground='#232426', borderwidth=0)
VNkeyTextBin = Text(VernamFrame, width=25, height=3)
VNkeyTextBin.place(x=270, y=160)
VNkeyTextBin.config(state=DISABLED, bg='#155939', fg='#BFBFBF', borderwidth=0)
VNoutputText = Text(VernamFrame, width=25, height=3)
VNoutputText.place(x=20, y=260)
VNoutputText.config(state=DISABLED, bg='#155939', fg='#BFBFBF', borderwidth=0)
VNoutputTextBin = Text(VernamFrame, width=25, height=3)
VNoutputTextBin.place(x=270, y=260)
VNoutputTextBin.config(state=DISABLED, bg='#155939', fg='#BFBFBF', borderwidth=0)
VNBack = Button(VernamFrame, text='<', command=lambda: show())
VNBack.place(x=20, y=355)
VNBack.configure(background='#04BF68', foreground='#155939', borderwidth=0, activebackground='#232426', pady=5, padx=10)
VNEncrypt = Button(VernamFrame, text='Encrypt', command=lambda: GUI_Vernam('encrypt'))
VNEncrypt.place(x=70, y=355)
VNEncrypt.configure(background='#04BF68', foreground='#155939', borderwidth=0, activebackground='#232426', pady=5, padx=10)
VNDecript = Button(VernamFrame, text='Decrypt', command=lambda: GUI_Vernam('decrypt'))
VNDecript.place(x=140, y=355)
VNDecript.configure(background='#04BF68', foreground='#155939', borderwidth=0, activebackground='#232426', pady=5, padx=10)
VNClear = Button(VernamFrame, text='Clear', command=lambda: GUI_Vernam('clear'))
VNClear.place(x=410, y=355)
VNClear.configure(background='#04BF68', foreground='#155939', borderwidth=0, activebackground='#232426', pady=5, padx=10)
VNauto = BooleanVar()
VNon = Radiobutton(VernamFrame, text='Auto', variable=VNauto, value=1)
VNon.place(x=320, y=345)
VNon.configure(background='#2a2b2d', foreground='#BFBFBF', activebackground='#232426', activeforeground='#BFBFBF', selectcolor='#232426')
VNoff = Radiobutton(VernamFrame, text='Manual', variable=VNauto, value=0)
VNoff.place(x=320, y=370)
VNoff.configure(background='#2a2b2d', foreground='#BFBFBF', activebackground='#232426', activeforeground='#BFBFBF', selectcolor='#232426')

VigenereFrame = Frame(base, bg='#232426')
VigenereFrame.place(x=0, y=0, width=500, height=400)
VGBar = Canvas(VigenereFrame, width=500, height=65, bg='#2a2b2d', highlightthickness=0)
VGBar.place(x=0, y=335)
VGinputTextLabel = Label(VigenereFrame, text='Input Text')
VGinputTextLabel.place(x=30, y=30)
VGinputTextLabel.configure(background='#232426', foreground='#F2F2F2')
VGkeyTextLabel = Label(VigenereFrame, text='Key')
VGkeyTextLabel.place(x=30, y=130)
VGkeyTextLabel.configure(background='#232426', foreground='#F2F2F2')
VGoutputTextLabel = Label(VigenereFrame, text='Output Text')
VGoutputTextLabel.place(x=30, y=210)
VGoutputTextLabel.configure(background='#232426', foreground='#BFBFBD')
VGinputText = Text(VigenereFrame, width=50, height=3)
VGinputText.place(x=20, y=60)
VGinputText.configure(background='#04BF68', foreground='#232426', borderwidth=0)
VGkeyText = Entry(VigenereFrame, width=25)
VGkeyText.place(x=20, y=160)
VGkeyText.configure(background='#04BF68', foreground='#232426', borderwidth=0)
VGoutputText = Text(VigenereFrame, width=50, height=3)
VGoutputText.place(x=20, y=240)
VGoutputText.config(state=DISABLED, bg='#155939', fg='#BFBFBF', borderwidth=0)
VGBack = Button(VigenereFrame, text='<', command=lambda: show())
VGBack.place(x=20, y=355)
VGBack.configure(background='#04BF68', foreground='#155939', borderwidth=0, activebackground='#232426', pady=5, padx=10)
VGEncrypt = Button(VigenereFrame, text='Encrypt', command=lambda: GUI_Vigenere('encrypt'))
VGEncrypt.place(x=70, y=355)
VGEncrypt.configure(background='#04BF68', foreground='#155939', borderwidth=0, activebackground='#232426', pady=5, padx=10)
VGDecript = Button(VigenereFrame, text='Decrypt', command=lambda: GUI_Vigenere('decrypt'))
VGDecript.place(x=140, y=355)
VGDecript.configure(background='#04BF68', foreground='#155939', borderwidth=0, activebackground='#232426', pady=5, padx=10)
VGClear = Button(VigenereFrame, text='Clear', command=lambda: GUI_Vigenere('clear'))
VGClear.place(x=410, y=355)
VGClear.configure(background='#04BF68', foreground='#155939', borderwidth=0, activebackground='#232426', pady=5, padx=10)

RC4Frame = Frame(base, bg='#232426')
RC4Frame.place(x=0, y=0, width=500, height=400)
RC4Bar = Canvas(RC4Frame, width=500, height=65, bg='#2a2b2d', highlightthickness=0)
RC4Bar.place(x=0, y=335)
RC4inputTextLabel = Label(RC4Frame, text='Input Text')
RC4inputTextLabel.place(x=30, y=30)
RC4inputTextLabel.configure(background='#232426', foreground='#F2F2F2')
RC4inputBytesLabel = Label(RC4Frame, text='Input Bytes')
RC4inputBytesLabel.place(x=280, y=30)
RC4inputBytesLabel.configure(background='#232426', foreground='#F2F2F2')
RC4keySeedTextLabel = Label(RC4Frame, text='Key Seed')
RC4keySeedTextLabel.place(x=30, y=130)
RC4keySeedTextLabel.configure(background='#232426', foreground='#F2F2F2')
RC4keySeedBytesLabel = Label(RC4Frame, text='Key Seed Bytes')
RC4keySeedBytesLabel.place(x=280, y=130)
RC4keySeedBytesLabel.configure(background='#232426', foreground='#F2F2F2')
RC4outputTextLabel = Label(RC4Frame, text='Output Text')
RC4outputTextLabel.place(x=30, y=200)
RC4outputTextLabel.configure(background='#232426', foreground='#BFBFBD')
RC4outputBytesLabel = Label(RC4Frame, text='Output Bytes')
RC4outputBytesLabel.place(x=280, y=200)
RC4outputBytesLabel.configure(background='#232426', foreground='#BFBFBD')
RC4inputText = Text(RC4Frame, width=25, height=3)
RC4inputText.place(x=20, y=60)
RC4inputText.configure(background='#04BF68', foreground='#232426', borderwidth=0)
RC4inputBytes = Text(RC4Frame, width=25, height=3)
RC4inputBytes.place(x=270, y=60)
RC4inputBytes.configure(background='#04BF68', foreground='#232426', borderwidth=0)
RC4keySeedText = Entry(RC4Frame, width=33)
RC4keySeedText.place(x=20, y=160)
RC4keySeedText.configure(background='#04BF68', foreground='#232426', borderwidth=0)
RC4keySeedBytes = Entry(RC4Frame, width=33)
RC4keySeedBytes.place(x=270, y=160)
RC4keySeedBytes.configure(background='#04BF68', foreground='#232426', borderwidth=0)
RC4outputText = Text(RC4Frame, width=25, height=3)
RC4outputText.place(x=20, y=230)
RC4outputText.config(state=DISABLED, background='#155939', foreground='#BFBFBF', borderwidth=0)
RC4outputBytes = Text(RC4Frame, width=25, height=3)
RC4outputBytes.place(x=270, y=230)
RC4outputBytes.config(state=DISABLED, background='#155939', foreground='#BFBFBF', borderwidth=0)
RC4Back = Button(RC4Frame, text='<', command=lambda: show())
RC4Back.place(x=20, y=355)
RC4Back.configure(background='#04BF68', foreground='#155939', borderwidth=0, activebackground='#232426', pady=5, padx=10)
RC4cipherText = Button(RC4Frame, text='Cipher text', command=lambda: GUI_RC4("ASCII"))
RC4cipherText.place(x=70, y=355)
RC4cipherText.configure(background='#04BF68', foreground='#155939', borderwidth=0, activebackground='#232426', pady=5, padx=10)
RC4cipherBytes = Button(RC4Frame, text='Cipher bytes', command=lambda: GUI_RC4("Bytes"))
RC4cipherBytes.place(x=160, y=355)
RC4cipherBytes.configure(background='#04BF68', foreground='#155939', borderwidth=0, activebackground='#232426', pady=5, padx=10)
RC4Clear = Button(RC4Frame, text='Clear', command=lambda: GUI_RC4("Clear"))
RC4Clear.place(x=410, y=355)
RC4Clear.configure(background='#04BF68', foreground='#155939', borderwidth=0, activebackground='#232426', pady=5, padx=10)

ConversorFrame = Frame(base, bg='#232426')
ConversorFrame.place(x=0, y=0, width=500, height=400)
CNVBar = Canvas(ConversorFrame, width=500, height=65, bg='#2a2b2d', highlightthickness=0)
CNVBar.place(x=0, y=335)
CNVinputTextLabel = Label(ConversorFrame, text='Input Text')
CNVinputTextLabel.place(x=30, y=30)
CNVinputTextLabel.configure(background='#232426', foreground='#F2F2F2')
CNVoutputTextLabel = Label(ConversorFrame, text='Output Text')
CNVoutputTextLabel.place(x=30, y=170)
CNVoutputTextLabel.configure(background='#232426', foreground='#BFBFBD')
CNVinputText = Text(ConversorFrame, width=50, height=5)
CNVinputText.place(x=20, y=60)
CNVinputText.configure(background='#04BF68', foreground='#232426', borderwidth=0)
CNVoutputText = Text(ConversorFrame, width=50, height=5)
CNVoutputText.place(x=20, y=200)
CNVoutputText.config(state=DISABLED, bg='#155939', fg='#BFBFBF', borderwidth=0)
CNVBack = Button(ConversorFrame, text='<', command=lambda: show())
CNVBack.place(x=20, y=355)
CNVBack.configure(background='#04BF68', foreground='#155939', borderwidth=0, activebackground='#232426', pady=5, padx=10)
CNVEncrypt = Button(ConversorFrame, text='txt_to_bin', command=lambda: GUI_Conversor("txt_to_bin"))
CNVEncrypt.place(x=70, y=355)
CNVEncrypt.configure(background='#04BF68', foreground='#155939', borderwidth=0, activebackground='#232426', pady=5, padx=10)
CNVDecrypt = Button(ConversorFrame, text='bin_to_txt', command=lambda: GUI_Conversor("bin_to_txt"))
CNVDecrypt.place(x=150, y=355)
CNVDecrypt.configure(background='#04BF68', foreground='#155939', borderwidth=0, activebackground='#232426', pady=5, padx=10)
CNVClear = Button(ConversorFrame, text='Clear', command=lambda: GUI_Conversor('Clear'))
CNVClear.place(x=410, y=355)
CNVClear.configure(background='#04BF68', foreground='#155939', borderwidth=0, activebackground='#232426', pady=5, padx=10)

# Show frame
def show(page = 'Home'):
    if page == 'Atbash':
        AtbashFrame.lift()
    elif page == 'Vernam':
        VernamFrame.lift()
    elif page == 'Vigenere':
        VigenereFrame.lift()
    elif page == 'RC4':
        RC4Frame.lift()
    elif page == 'Conversor':
        ConversorFrame.lift()
    elif page == 'Home':
        MainFrame.lift()

    return

def GUI_atbash(mode):
    if mode == "convert":
        encrypted = atbashEncrypt(ABinputText.get('1.0', END))

        ABoutputText.config(state=NORMAL)
        ABoutputText.delete('1.0', END)
        ABoutputText.insert(END, encrypted)
        ABoutputText.config(state=DISABLED)

        return
    elif mode == "clear":
        ABinputText.delete('1.0', END)

        ABoutputText.config(state=NORMAL)
        ABoutputText.delete('1.0', END)
        ABoutputText.config(state=DISABLED)
    return

def GUI_Vernam(mode):
    if mode == "encrypt":
        if VNauto.get():
            temp = vernamEncrypt(VNinputText.get('1.0', END).rstrip("\n"))
        else:
            if len(txt_to_bin(VNkeyText.get('1.0', END).rstrip("\n"))) != len(txt_to_bin(VNinputText.get('1.0', END).rstrip("\n"))):
                messagebox.showerror('Error', 'key size and input size must be equal')
                return
            else:
                temp = vernamEncrypt(VNinputText.get('1.0', END).rstrip("\n"), VNkeyText.get('1.0', END).rstrip("\n"))

        VNSize.set("Bin size: " + str(len(temp['cripted_bin'])))

        VNoutputText.config(state=NORMAL)
        VNoutputText.delete('1.0', END)
        VNoutputText.insert('1.0', temp['cripted_ascii'])
        VNoutputText.config(state=DISABLED)

        VNoutputTextBin.config(state=NORMAL)
        VNoutputTextBin.delete('1.0', END)
        VNoutputTextBin.insert('1.0', temp['cripted_bin'])
        VNoutputTextBin.config(state=DISABLED)

        VNkeyText.delete('1.0', END)
        VNkeyText.insert('1.0', temp['key_ascii'])

        VNkeyTextBin.config(state=NORMAL)
        VNkeyTextBin.delete('1.0', END)
        VNkeyTextBin.insert('1.0', temp['key_bin'])
        VNkeyTextBin.config(state=DISABLED)

        VNinputTextBin.config(state=NORMAL)
        VNinputTextBin.delete('1.0', END)
        VNinputTextBin.insert('1.0', txt_to_bin(VNinputText.get('1.0', END).rstrip("\n")))
        VNinputTextBin.config(state=DISABLED)

    elif mode == "decrypt":
        temp_txt = (VNinputText.get('1.0', END).rstrip("\n"))
        temp_key = (VNkeyText.get('1.0', END).rstrip("\n"))

        VNSize.set("Bin size: " + str(len(txt_to_bin(temp_txt))))

        VNinputTextBin.config(state=NORMAL)
        VNinputTextBin.delete('1.0', END)
        VNinputTextBin.insert('1.0', txt_to_bin(temp_txt))
        VNinputTextBin.config(state=DISABLED)

        VNkeyTextBin.config(state=NORMAL)
        VNkeyTextBin.delete('1.0', END)
        VNkeyTextBin.insert('1.0', txt_to_bin(temp_key))
        VNkeyTextBin.config(state=DISABLED)

        decrypted = vernamDecrypt(temp_txt, temp_key)

        VNoutputText.config(state=NORMAL)
        VNoutputText.delete('1.0', END)
        VNoutputText.insert('1.0', decrypted)
        VNoutputText.config(state=DISABLED)
        
        VNoutputTextBin.config(state=NORMAL)
        VNoutputTextBin.delete('1.0', END)
        VNoutputTextBin.insert('1.0', txt_to_bin(decrypted))
        VNoutputTextBin.config(state=DISABLED)
        return
    elif mode == "clear":
        VNinputText.delete('1.0', END)
        
        VNinputTextBin.config(state=NORMAL)
        VNinputTextBin.delete('1.0', END)
        VNinputTextBin.config(state=DISABLED)

        VNkeyText.delete('1.0', END)

        VNkeyTextBin.config(state=NORMAL)
        VNkeyTextBin.delete('1.0', END)
        VNkeyTextBin.config(state=DISABLED)

        VNoutputText.config(state=NORMAL)
        VNoutputText.delete('1.0', END)
        VNoutputText.config(state=DISABLED)

        VNoutputTextBin.config(state=NORMAL)
        VNoutputTextBin.delete('1.0', END)
        VNoutputTextBin.config(state=DISABLED)
        return
    return

def GUI_Vigenere(mode):
    if mode == "encrypt":
        key = VGkeyText.get()
        if key == '' or key.count(' ') > 1:
            messagebox.showerror('Error', 'Key must be one word')
            return
        elif key.isalpha() == False:
            messagebox.showerror('Error', 'Key must be alphabetic')
        key = key.replace('\n', '')
        key = key.replace('\t', '')

        encrypted = vigenereEncrypt(VGinputText.get('1.0', END), VGkeyText.get())

        VGoutputText.config(state=NORMAL)
        VGoutputText.delete('1.0', END)
        VGoutputText.insert(END, encrypted)
        VGoutputText.config(state=DISABLED)
    elif mode == "decrypt":
        key = VGkeyText.get()
        if key == '' or key.count(' ') > 1:
            messagebox.showerror('Error', 'Key must be one word')
            return
        key = key.replace('\n', '')
        key = key.replace('\t', '')

        decrypted = vigenereDecrypt(VGinputText.get('1.0', END), VGkeyText.get())

        VGoutputText.config(state=NORMAL)
        VGoutputText.delete('1.0', END)
        VGoutputText.insert(END, decrypted)
        VGoutputText.config(state=DISABLED)
    elif mode == "clear":
        VGinputText.delete('1.0', END)

        VGkeyText.delete(0, END)

        VGoutputText.config(state=NORMAL)
        VGoutputText.delete('1.0', END)
        VGoutputText.config(state=DISABLED)
    return

def GUI_RC4(mode):
    if mode == "ASCII":
        input = RC4inputText.get("1.0", END).strip()
        input = txt_to_bytes(input)
        keySeed = RC4keySeedText.get().strip()
        keySeed = txt_to_bytes(keySeed)
        RC4inputBytes.delete("1.0", END)
        for i in input:
            RC4inputBytes.insert(END, str(i) + " ")
        RC4keySeedBytes.delete(0, END)
        for i in keySeed:
            RC4keySeedBytes.insert(END, str(i) + " ")
    elif mode == "Bytes":
        input = RC4inputBytes.get("1.0", END).strip()
        input = input.split(" ")
        keySeed = RC4keySeedBytes.get().strip()
        keySeed = keySeed.split(" ")
        for i in range(len(input)):
            input[i] = int(input[i])
        for i in range(len(keySeed)):
            keySeed[i] = int(keySeed[i])
        RC4inputText.delete("1.0", END)
        RC4inputText.insert(END, bytes_to_txt(input))
        RC4keySeedText.delete(0, END)
        RC4keySeedText.insert(END, bytes_to_txt(keySeed))
    elif mode == "Clear":
        RC4inputText.delete("1.0", END)
        RC4inputBytes.delete("1.0", END)
        RC4keySeedText.delete(0, END)
        RC4keySeedBytes.delete(0, END)
        RC4outputText.config(state=NORMAL)
        RC4outputText.delete("1.0", END)
        RC4outputText.config(state=DISABLED)
        RC4outputBytes.config(state=NORMAL)
        RC4outputBytes.delete("1.0", END)
        RC4outputBytes.config(state=DISABLED)
        return
    output = RC4(keySeed, input)
    RC4outputText.config(state=NORMAL)
    RC4outputText.delete("1.0", END)
    RC4outputText.insert(END, bytes_to_txt(output))
    RC4outputText.config(state=DISABLED)
    RC4outputBytes.config(state=NORMAL)
    RC4outputBytes.delete("1.0", END)
    RC4outputBytes.insert(END, output)
    RC4outputBytes.config(state=DISABLED)
    return
    
def GUI_Conversor(mode):
    if mode == 'txt_to_bin':
        temp = txt_to_bin(CNVinputText.get('1.0', END).rstrip("\n"))
        CNVoutputText.config(state=NORMAL)
        CNVoutputText.delete('1.0', END)
        CNVoutputText.insert(END, temp)
        CNVoutputText.config(state=DISABLED)
        return
    elif mode == 'bin_to_txt':
        temp = bin_to_txt(CNVinputText.get('1.0', END).rstrip("\n"))
        CNVoutputText.config(state=NORMAL)
        CNVoutputText.delete('1.0', END)
        CNVoutputText.insert(END, temp)
        CNVoutputText.config(state=DISABLED)
        return
    elif mode == 'Clear':
        CNVinputText.delete('1.0', END)
        CNVoutputText.config(state=NORMAL)
        CNVoutputText.delete('1.0', END)
        CNVoutputText.config(state=DISABLED)
        return
    return

MainFrame.lift()
base.mainloop()