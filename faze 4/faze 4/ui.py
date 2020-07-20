import tkinter as tk
import q

class App(object):

    def __init__(self, parent):

        self.root = parent
        self.root.title("Queries")
        self.frame = tk.Frame(parent)
        self.frame.pack()

        label = tk.Label(self.frame, text = "Please Select The Query")
        label.grid(row=0, column = 2)

        btn1 = tk.Button(self.frame, width=15, height=2,
                        text= "Query1", command = lambda : self.pop_up(q.query('1'),'1'))
        btn1.grid(row=1, column = 1)

        btn2 = tk.Button(self.frame, width=15, height=2,
                        text= "Query2", command = lambda : self.pop_up(q.query('2'),'2'))
        btn2.grid(row=1, column = 2)

        btn3 = tk.Button(self.frame, width=15, height=2,
                        text= "Query3", command = lambda : self.pop_up(q.query('3'),'3'))
        btn3.grid(row=1, column = 3)

        btn4 = tk.Button(self.frame, width=15, height=2,
                        text= "Query4", command = lambda : self.pop_up(q.query('4'),'4'))
        btn4.grid(row=2, column = 1)

        btn5 = tk.Button(self.frame, width=15, height=2,
                        text= "Query5", command = lambda : self.pop_up(q.query('5'),'5'))
        btn5.grid(row=2, column = 2)

        btn6 = tk.Button(self.frame, width=15, height=2,
                        text= "Query6", command = lambda : self.pop_up(q.query('6'),'6'))
        btn6.grid(row=2, column = 3)

        btn7 = tk.Button(self.frame, width=15, height=2,
                        text= "Query7", command = lambda : self.pop_up(q.query('7'),'7'))
        btn7.grid(row=3, column = 1)

        btn8 = tk.Button(self.frame, width=15, height=2,
                        text= "Query8", command = lambda : self.pop_up(q.query('8'),'8'))
        btn8.grid(row=3, column = 2)

        btn9 = tk.Button(self.frame, width=15, height=2,
                        text= "Query9", command = lambda : self.pop_up(q.query('9'),'9'))
        btn9.grid(row=3, column = 3)

        btn10 = tk.Button(self.frame, width=15, height=2,
                        text= "Query10", command = lambda : self.pop_up(q.query('10'),'10'))
        btn10.grid(row=4, column = 1)

        btn11 = tk.Button(self.frame, width=15, height=2,
                        text= "Query11", command = lambda : self.pop_up(q.query('11'),'11'))
        btn11.grid(row=4, column = 2)

        btn12 = tk.Button(self.frame, width=15, height=2,
                        text= "Query12", command = lambda : self.pop_up(q.query('12'),'12'))
        btn12.grid(row=4, column = 3)

        btn12 = tk.Button(self.frame, width=15, height=2,
                        text= "Query13", command = lambda : self.pop_up(q.query('13'),'13'))
        btn12.grid(row=5, column = 1)

        btn14 = tk.Button(self.frame, width=15, height=2,
                        text= "Query14", command = lambda : self.pop_up(q.query('14'),'14'))
        btn14.grid(row=5, column = 2)

        btn15 = tk.Button(self.frame, width=15, height=2,
                        text= "Query15", command = lambda : self.pop_up(q.query('15'),'15'))
        btn15.grid(row=5, column = 3)


    def pop_up(self, data, N):
    	self.root.withdraw()
    	popUp(self, data, N)

class popUp(tk.Toplevel):

    def __init__(self, original, data, N):

        self.original_frame = original
        tk.Toplevel.__init__(self)
        self.transient(root)
        self.lift()
        total_rows = len(data) 
        total_columns = len(data[0])
        
        for i in range(total_rows): 
            for j in range(total_columns): 
                e = tk.Entry(self, width=20, fg='black', 
                                font=('Arial',16,'bold')) 
                e.grid(row=i+1, column=j) 
                e.insert(tk.END, data[i][j]) 
        label = tk.Label(self, text = "This is Query Number" + N)
        label.grid(row = 0)
        btn = tk.Button(self, text ="Close", command= lambda : self.on_close())
        if total_columns == 1:
            btn.grid(row = 0, column = total_columns)
        else:
            btn.grid(row = 0, column = total_columns-1)


    def on_close(self):
    	self.destroy()
    	root.update()
    	root.deiconify()

if __name__ == "__main__":

    root = tk.Tk()
    app = App(root)
    root.geometry()
    root.mainloop()