try:
    import Tkinter as tk
    import tkFont
    import ttk
    import database.db as mdb
    import os
    import getpass
except ImportError:  # Python 3
    import tkinter as tk
    from tkinter import *
    import tkinter.font as tkFont
    import tkinter.ttk as ttk
    import database.db as mdb
    import os
    import getpass

user = getpass.getuser()
pathVaultMain = '/home/' + user + '/PyVault/KeyVault/main.py'

class MultiColumnListbox(object):
    """use a ttk.TreeView as a multicolumn ListBox"""
    
    def __init__(self):
        self.tree = None
        self._setup_widgets()
        self._build_tree()

    def _selectItem(self, a):
        curItem = self.tree.focus()
        dico = self.tree.item(curItem)
        val = dico['values']
        addToClipBoard(val[1])


    def _setup_widgets(self):
        s = """\click on header to sort by that column
to change width of column drag boundary and click on a row to copy the key
        """
        msg = ttk.Label(wraplength="4i", justify="left", anchor="n",
            padding=(10, 2, 10, 6), text=s)
        msg.pack(fill='x')
        container = ttk.Frame()
        container.pack(fill='both', expand=True)
        # create a treeview with dual scrollbars
        self.tree = ttk.Treeview(columns=header, show="headings")
        vsb = ttk.Scrollbar(orient="vertical",
            command=self.tree.yview)
        hsb = ttk.Scrollbar(orient="horizontal",
            command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set,
            xscrollcommand=hsb.set)
        self.tree.grid(column=0, row=0, sticky='nsew', in_=container)
        vsb.grid(column=1, row=0, sticky='ns', in_=container)
        hsb.grid(column=0, row=1, sticky='ew', in_=container)
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)
        self.tree.bind('<ButtonRelease-1>', self._selectItem)

    def _build_tree(self):
        for col in header:
            self.tree.heading(col, text=col.title(),
                command=lambda c=col: sortby(self.tree, c, 0))
            # adjust the column's width to the header string
            self.tree.column(col,
                width=tkFont.Font().measure(col.title()))

        for item in data:
            self.tree.insert('', 'end', values=item)
            # adjust column's width if necessary to fit each value
            for ix, val in enumerate(item):
                col_w = tkFont.Font().measure(val)
                if self.tree.column(header[ix],width=None)<col_w:
                    self.tree.column(header[ix], width=col_w)
        

def sortby(tree, col, descending):
    """sort tree contents when a column header is clicked on"""
    # grab values to sort
    data = [(tree.set(child, col), child) \
        for child in tree.get_children('')]
    # if the data to be sorted is numeric change to float
    #data =  change_numeric(data)
    # now sort the data in place
    data.sort(reverse=descending)
    for ix, item in enumerate(data):
        tree.move(item[1], '', ix)
    # switch the heading so it will sort in the opposite direction
    tree.heading(col, command=lambda col=col: sortby(tree, col, \
        int(not descending)))



class newWindow(tk.Toplevel):
    def __init__(self, master = None):  
        super().__init__(master = master)
        self.title("New Key")
        self.geometry("400x400")
        #label = tk.Label(self, text ="Register new key")
        #label.grid(column=0)

        ## The key input parts
        inputName = tk.Label(self, text="Name")
        inputName.grid(column=0, row=0)
        inputtxt = tk.Entry(self,
                   width = 20, textvariable=v1)
        inputtxt.grid(column=1, row=0)

        inputValue = tk.Label(self, text="Value")
        inputValue.grid(column=0, row=1)
        inputtxt2 = tk.Entry(self,
                   width = 20, textvariable=v2)
        inputtxt2.grid(column=1, row=1)
        #input = inputtxt.get("1.0","end-1c")
        #input2 = inputtxt2.get("1.0","end-1c")
        #Destroy window
        tk.Button(self,
                text='Close',
                command=self.destroy).grid(column=0, row=2)
        tk.Button(self,
                text='Save',
                command=self.registerNewKey).grid(column=1, row=2)
        
    def registerNewKey(self):
        mdb.writeKey(v1.get(), v2.get())
        self.destroy()
        





# the test data ...

header = ['name', 'key']
mdb.setupDb()
data_temp = mdb.readAll().fetchall()
data = []
for item in data_temp:
    new_item = (item[1], item[2])
    data.append(new_item)


#data = list.append()

def addToClipBoard(text):
    command = 'echo ' + text.strip() + '| xclip -selection clipboard' 
    os.system(command)


def update():
 root.destroy()
 os.system('python ' + pathVaultMain)

if __name__ == '__main__':
    root = tk.Tk()
    v1 = tk.StringVar()
    v2 = tk.StringVar()
    root.title("PyVault")
    root.geometry("800x600")
    btn = tk.Button(root, text ="Create new key")
  
    # Following line will bind click event
    # On any click left / right button
    # of mouse a new window will be opened
    btn.bind("<Button>", lambda e: newWindow(root))
    btn.pack(pady = 10)

    btn2 = tk.Button(root, text ="Update")
  
    # Following line will bind click event
    # On any click left / right button
    # of mouse a new window will be opened
    btn2.bind("<Button>", lambda e: update())
    btn2.pack(pady = 10)

    listbox = MultiColumnListbox()
    #update()
    root.mainloop()

