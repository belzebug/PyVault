try:
    import Tkinter as tk
    import tkFont
    import ttk
    import database.db as mdb
    import os
except ImportError:  # Python 3
    import tkinter as tk
    import tkinter.font as tkFont
    import tkinter.ttk as ttk
    import database.db as mdb
    import os

class MultiColumnListbox(object):
    """use a ttk.TreeView as a multicolumn ListBox"""
    
    def __init__(self):
        self.tree = None
        self._setup_widgets()
        self._build_tree()

    def _selectItem(self, a):
        curItem = self.tree.focus()
        print(self.tree.item(curItem))
        dico = self.tree.item(curItem)
        val = dico['values']
        print(val[1])
        addToClipBoard(val[1])


    def _setup_widgets(self):
        s = """\click on header to sort by that column
to change width of column drag boundary
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

# the test data ...

header = ['name', 'key']
mdb.setupDb()
data_temp = mdb.readAll().fetchall()
data = []
for item in data_temp:
    new_item = (item[1], item[2])
    print(new_item)
    data.append(new_item)

print(data)

#data = list.append()

def addToClipBoard(text):
    command = 'echo ' + text.strip() + '| xclip'
    os.system(command)

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Multicolumn Treeview/Listbox")
    listbox = MultiColumnListbox()
    root.mainloop()

