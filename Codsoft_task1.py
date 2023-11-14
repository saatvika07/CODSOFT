from tkinter import *
from tkinter import messagebox
from tkinter.font import *
from tkinter import scrolledtext

global tasks
tasks = [] 


def add_task():
    task = entry_scroll.get("1.0",END)
    if not task.strip():
        messagebox.showerror("ERROR", "Task not entered")
    else:
        tasks.append(task)
        entry_scroll.delete("1.0", END)  # Updated to delete from line 1, column 0
        messagebox.showinfo("Added", "Task is Added")

def display_task():
    list_str = ""
    i=1
    for task in tasks:
        list_str += f"[{i}] {task}\n"
        i+=1
    
    display_scroll.delete(1.0, END)
    display_scroll.insert(END,list_str)

def delete_task():
    try:
        num = int(delete_task_num.get())
                
        task = tasks.pop(num-1)
        display_task()  # Updating the display after deletion
        messagebox.showinfo("Deleted", "Task is Deleted")
        delete_task_num.delete(0,END)

    except (ValueError, IndexError):
        messagebox.showerror("Error", "Invalid task number")
       
main_win = Tk()
main_win.geometry("500x500+400+100")
main_win.configure(bg="bisque3")
main_win.title("To-Do List")
#fonts
font1 = ("Times", "20", "bold")
font2 = ("Helvetica", "16")

frame1 = Frame(main_win).place(x=0,y=0)
title = Label(frame1,text = "To-Do List",font = font1,bg="bisque3").pack()

entry_lbl = Label(main_win,text="Enter the task:",bg="bisque3",font = font2)
entry_lbl.place(x=10,y=100)

entry_scroll = scrolledtext.ScrolledText(main_win, font=font2,bg="bisque3", height=0, width=25)
entry_scroll.place(x=150,y=100)
entry_scroll.focus()
 
add = Button(main_win,text="ADD TASK         ",bg="bisque3",font=font2,command = add_task)
add.place(x = 10,y = 200)

delete = Button(main_win, text="DELETE TASK   ",font=font2,bg="bisque3",command=delete_task)
delete.place(x = 10,y = 250)

delete_task_num = Entry(main_win,font=("Helvetica", "20"),bg="bisque3",width=5)
delete_task_num.place(x=200,y=250)


display = Button(main_win, text="DISPLAY TASKS",font=font2,bg="bisque3",command=display_task)
display.place(x = 10,y = 300)


display_scroll = scrolledtext.ScrolledText(main_win,font = font2,bg="bisque3",height=10,width=15)
display_scroll.place(x=300,y=200)



main_win.mainloop()