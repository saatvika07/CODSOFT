from tkinter import *
from tkinter import scrolledtext
import re
from tkinter import messagebox


global contact
contact = dict()
name_entry_delete = None
ph_no_entry_delete = None

main = Tk()
main.title("Contact Book")
main.geometry("600x550")
main.resizable(False,False)
main.configure(bg="antiquewhite3")

icon_image = PhotoImage(file="C:\\Users\\Lenovo\\Downloads\\Contact_book_pic.PNG")  
main.iconphoto(True, icon_image)


font1 = ("Times", "20", "bold")
font2 = ("Helvetica", "16")

#all the functions

def valid_ph_no(ph_no):
    return re.fullmatch("[6-9][0-9]{9}",ph_no)

def valid_email(email_id):
    pattern = r'\b[a-zA-Z0-9.+%_-]+@[A-Za-z0-9]+\.[A-Z|a-z]{2,7}\b'
    return re.match(pattern,email_id)

def add_contact():
    name = name_entry.get()
    ph_no = ph_no_entry.get()
    email_id = email_entry.get()
    address = address_entry.get()
    
    if (valid_ph_no(ph_no) != None) and (valid_email(email_id) != None):
        contact[name] = {"name":name,"ph_no":ph_no,"email_id":email_id,"address":address}   
        name = name_entry.delete(0,END)
        ph_no = ph_no_entry.delete(0,END)
        email_id = email_entry.delete(0,END)
        address = address_entry.delete(0,END)
        
    else:
        messagebox.showerror("Error","Details aren't correct")
    view_contact()

def delete_contact():
    num = int(delete_cntct_no.get())
    delete_cntct_no.delete(0,END)

    names = list(contact.keys())
    name_to_del = names[num-1]
    del contact[name_to_del]
    view_contact()

def view_contact():
    output_str = "***Contact Details are***\n"
    i=1
    for name in contact:
        output_str += f"[{i}]"
        output_str += f"Name: {contact[name]['name']}\n"
        output_str += f"Phone no.: {contact[name]['ph_no']}\n"
        output_str += f"Email-ID: {contact[name]['email_id']}\n"
        output_str += f"Address: {contact[name]['address']}\n\n"
        i+=1

    display_scroll = scrolledtext.ScrolledText(main, font=font2, height=7, width=23,bg="antiquewhite3")
    display_scroll.insert(END, output_str)
    display_scroll.place(x=300, y=250)

def search_contact():
    i=1
    search_name = name_entry.get()
    search_ph_no = ph_no_entry.get() #as phone number is unique.
    if not ((search_name.strip() or search_ph_no.strip()) or (search_name.strip() or search_ph_no.strip())):
        messagebox.showerror("Error","Enter the name and phone no. details")
    else:
        if search_name in contact :
            if contact[search_name]["ph_no"] == search_ph_no:
                messagebox.showerror("Error",f"Contact details are existing. Contact[{i}]")
            else:
                pass
        else:
            messagebox.showerror("Error","Contact details not found")
    i+=1
    
def update_contact():
    upd_num = int(update_cntct_no.get())
    update_cntct_no.delete(0,END)
    upd_name = name_entry.get()
    upd_ph_no = ph_no_entry.get()
    upd_email = email_entry.get()
    upd_address = address_entry.get()
    

    names = list(contact.keys())
    upd_cntct_name = names[upd_num-1]
    details = contact[upd_cntct_name]
    # Unpack the values from the nested dictionary for updating contact

    old_name = details["name"]
    old_ph_no = details["ph_no"]
    old_email_id = details["email_id"]
    old_address = details["address"]
    
    if not upd_name.strip():
        upd_name = old_name
    else:
        pass
        
    if not upd_ph_no.strip():
        upd_ph_no = old_ph_no
    else:
        pass
    
    if not upd_email.strip():
        upd_email = old_email_id
    else:
        pass
    
    if not upd_address.strip():
        upd_address = old_address
    else:
        pass
    
    #all values are updates ones
    contact[upd_cntct_name]["name"] = upd_name
    contact[upd_cntct_name]["ph_no"] = upd_ph_no
    contact[upd_cntct_name]["email_id"] = upd_email
    contact[upd_cntct_name]["address"] = upd_address
    messagebox.showinfo("Updated","Contact is updated")

def exit_prog():
    main.destroy()


    
frame1 = Frame(main).place(x=0,y=0)
head = Label(frame1,text="CONTACT BOOK",font=font1,bg="antiquewhite3")
head.place(x=180,y=10)

logo_image = PhotoImage(file=r"C:\Users\Lenovo\Downloads\Contact_book_pic2.png")
logo_label = Label(frame1, image=logo_image,bg="antiquewhite3")
logo_label.place(x=120,y=10)


sub_head = Label(main,text="Enter Contact details",font = font2,bg="antiquewhite3")
sub_head.place(x=10,y=50)

name_lbl = Label(main,text="Name:",font=font2,bg="antiquewhite3")
name_lbl.place(x=10,y=80)

name_entry = Entry(main,font=font2,bg="antiquewhite3")
name_entry.place(x=170,y=80)

ph_no_lbl = Label(main,text="Phone number:",font=font2,bg="antiquewhite3")
ph_no_lbl.place(x=10,y=110)

ph_no_entry = Entry(main,font=font2,bg="antiquewhite3")
ph_no_entry.place(x=170,y=110)

email_lbl = Label(main,text="Email-ID:",font=font2,bg="antiquewhite3")
email_lbl.place(x=10,y=140)

email_entry = Entry(main,font=font2,bg="antiquewhite3")
email_entry.place(x=170,y=140)

address_lbl = Label(main,text="Address:",font=font2,bg="antiquewhite3")
address_lbl.place(x=10,y=170)

address_entry = Entry(main,font=font2,bg="antiquewhite3")
address_entry.place(x=170,y=170)

add_cntct_lbl = Button(main,text="Add Contact",bg="antiquewhite3",font=font2,command = add_contact)
add_cntct_lbl.place(x=10,y=250)

update_cntct_lbl = Button(main,text="Update Contact",bg="antiquewhite3",font=font2,command = update_contact)
update_cntct_lbl.place(x=10,y=300)

update_cntct_no = Entry(main,font=("Helvetica", "20"),bg="antiquewhite3",width=5)
update_cntct_no.place(x=200,y=305)


delete_cntct_lbl = Button(main,text="Delete Contact",bg="antiquewhite3",font=font2,command = delete_contact)
delete_cntct_lbl.place(x=10,y=350)

delete_cntct_no = Entry(main,font=("Helvetica", "20"),bg="antiquewhite3",width=5)
delete_cntct_no.place(x=200,y=355)


search_cntct_lbl = Button(main,text="Search contact",font=font2,bg="antiquewhite3",command = search_contact)
search_cntct_lbl.place(x=10,y=400)

view_cntct_lbl = Button(main,text="View list",font=font2,bg="antiquewhite3",command = view_contact)
view_cntct_lbl.place(x=10,y=450)

exit_lbl = Button(main,text="Exit",font=font2,bg="antiquewhite3",command = exit_prog)
exit_lbl.place(x=10,y=500)

main.mainloop()
