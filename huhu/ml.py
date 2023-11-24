from datetime import date
import customtkinter as ctk
from tkinter import *
from tkinter import messagebox, PhotoImage

app = ctk.CTk()
app.title('My Fruit Shop')
app.geometry("870x450")
app.config(bg="#F8D9F3")
app.resizable(False, False)

# Fonts
font1 = ('Franklin Gothic Book', 17, 'bold', 'italic')
font2 = ('Franklin Gothic Book', 15, 'bold', 'underline')
font3 = ('Comic Sans MS', 25, 'italic', 'bold')

# Image
image1 = PhotoImage(file='C:/Users/admin/OneDrive/Documents/Melissa/My Fruit Shop/orangepic.png').subsample(3, 3)
image2 = PhotoImage(file='C:/Users/admin/OneDrive/Documents/Melissa/My Fruit Shop/applepic.png').subsample(3, 3)
image3 = PhotoImage(file='C:/Users/admin/OneDrive/Documents/Melissa/My Fruit Shop/Background.png').subsample(2, 1)

# Image labels

image1_label = Label(app, image=image1, fg="#F8D9F3", bg="#F8D9F3", compound="top", anchor="n", width=150, height=160)
image1_label.place(x=900, y=140)

image2_label = Label(app, image=image2, fg="#F8D9F3", bg="#F8D9F3", compound="top", anchor="n", width=150, height=160)
image2_label.place(x=700, y=150)

image3_label = Label(app, image=image3, fg="#F8D9F3", bg="#F8D9F3", compound="top", anchor="n", width=150, height=500)
image3_label.place(x=10, y=60)

# Frames
apple_frame = ctk.CTkFrame(app, width=110, height=60, fg_color="#AD6E8C", bg_color="#F8D9F3", corner_radius=20)
apple_frame.place(x=565, y=51)

orange_frame = ctk.CTkFrame(app, width=110, height=60, fg_color="#AD6E8C", bg_color="#F8D9F3", corner_radius=20)
orange_frame.place(x=730, y=51)

bill_frame = ctk.CTkFrame(app, width=300, height=370, fg_color="#AD6E8C", bg_color="#F8D9F3", corner_radius=20)
bill_frame.place(x=200, y=40)

quantity_frame = ctk.CTkFrame(app, width=100, height=40, fg_color="#AD6E8C", bg_color="#F8D9F3", corner_radius=15)
quantity_frame.place(x=574, y=265)

quantity2_frame = ctk.CTkFrame(app, width=100, height=40, fg_color="#AD6E8C", bg_color="#F8D9F3", corner_radius=15)
quantity2_frame.place(x=735, y=265)

customer_frame = ctk.CTkFrame(app, width=279, height=40, fg_color="#AD6E8C", bg_color="#F8D9F3", corner_radius=15)
customer_frame.place(x=570, y=330)

# Label the price
label_price1 = label_price = Label(app, text="Apple \n20 Pesos", bg='#AD6E8C', font=font1)
label_price1.place(x=720,y=70)

label_price2 = label_price = Label(app, text="Orange \n25 Pesos", bg='#AD6E8C', font=font1)
label_price2.place(x=930,y=70)

# Entry
quantity1_entry = ctk.CTkEntry(app, font=font1, text_color="#000000", bg_color="#AD6E8C", fg_color="#FFFEE7", width=80)
quantity1_entry.place(x=582, y=270)

quantity2_entry = ctk.CTkEntry(app, font=font1, text_color="#000000", bg_color="#AD6E8C", fg_color="#FFFEE7", width=80)
quantity2_entry.place(x=745, y=270)

customer_entry = ctk.CTkEntry(app, font=font1, fg_color="#FFFEE7", bg_color="#AD6E8C", text_color="#000000", border_color="#FFFFFF", width=200)
customer_entry.place(x=640, y=336)

# Label the Customer Entry
customer_label = ctk.CTkLabel(app, text="Name:", font=font1, text_color="#FFFFFF", fg_color="#AD6E8C", bg_color="#AD6E8C")
customer_label.place(x=585, y=335)

menu_label = ctk.CTkLabel(app, text="Mishy Freshy Fruities", font=font3, text_color="#FFDEED", bg_color="#AD6E8C")
menu_label.place(x=220, y=60)

price_list = [20, 25]
total_price = 0

def pay():
    global total_price
    try:
        if customer_entry.get() == '':
            messagebox.showwarning(title="Error", message="Please enter your name")
        else:
            total_price = int(quantity1_entry.get()) * price_list[0] + int(quantity2_entry.get()) * price_list[1]
            if total_price == 0:
                messagebox.showwarning(title="Error", message="Please select some fruits")
            else:
                name_label = ctk.CTkLabel(bill_frame, text=f'Name: {customer_entry.get()}', font=font2, text_color="#000000", bg_color="#AD6E8C", width=250, anchor=W)
                name_label.place(x=35, y=110)
                price_label = ctk.CTkLabel(bill_frame, text=f'Total Price: {total_price} Php', font=font2, text_color="#000000", bg_color="#AD6E8C", width=250, anchor=W)
                price_label.place(x=35, y=135)
                date_label = ctk.CTkLabel(bill_frame, text=f'Bill Date: {date.today()}', font=font2, text_color="#000000", bg_color="#AD6E8C", width=250, anchor=W)
                date_label.place(x=35, y=160)
                thank_you_label = ctk.CTkLabel(bill_frame, text='Thank You for Buying!', font=('Arial', 18, 'bold'), text_color="#76060C", bg_color="#AD6E8C", width=250, anchor=W)
                thank_you_label.place(x=35, y=300)
    except ValueError:
        messagebox.showwarning(title="Error", message="Please enter valid quantities.")
        # Optionally, you can reset the entry values to 0 or leave them unchanged
        if hasattr(quantity1_entry, 'set'):
            quantity1_entry.set(0)
        if hasattr(quantity2_entry, 'set'):
            quantity2_entry.set(0)
def new():
    customer_entry.delete(0, END)
    
    if hasattr(quantity1_entry, 'insert'):
        quantity1_entry.delete(0, END)
        quantity1_entry.insert(0, '0')

    if hasattr(quantity2_entry, 'insert'):
        quantity2_entry.delete(0, END)
        quantity2_entry.insert(0, '0')

    for widget in bill_frame.winfo_children():
        widget.destroy()


def save():
    with open(f'{customer_entry.get()} Bill', "w") as f:
        f.write(f'Customer Name: {customer_entry.get()}\n')
        f.write(f'Total Price: {total_price} Php\n')
        f.write(f'Bill Date: {date.today()}')
    messagebox.showinfo(title="Saved", message="Bill has been saved.")
# Buttons

pay_button = ctk.CTkButton(app, command=pay, text="Pay", font=font1, fg_color="#ad0c78", bg_color="#F8D9F3", hover_color="#D4A0CB", corner_radius=50, cursor="hand2", width=80)
pay_button.place(x=570, y=380)

save_button = ctk.CTkButton(app, command=save, text="Save", font=font1, fg_color="#ad0c78", bg_color="#F8D9F3", hover_color="#D4A0CB", corner_radius=50, cursor="hand2", width=80)
save_button.place(x=670, y=380)

new_button = ctk.CTkButton(app, command=new, text="New", font=font1, fg_color="#ad0c78", bg_color="#F8D9F3", hover_color="#D4A0CB", corner_radius=50, cursor="hand2", width=80)
new_button.place(x=770, y=380)

app.mainloop()