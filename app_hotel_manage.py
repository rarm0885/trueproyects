import tkinter as tk 
from tkinter import messagebox 


data_base = []
totals = []



def calculate_total(user_data):

    room_prices = {1: 849.99, 2: 1400, 3: 5000, 4: 4500}
    
    total = room_prices[user_data["Room Type"]] * int(user_data["Length of Stay"])
    
    if user_data["Breakfast"]:
        total += 30.99 * int(user_data["Length of Stay"])
    
    if user_data["Parking Slot"]:
        total += 25 * int(user_data["Length of Stay"])

    if user_data["Helicopter Transport"]:
        total += 4500 * int(user_data["Length of Stay"])

    if user_data["Happy Massage"]:
        total += 250 * int(user_data["Length of Stay"])

    return total



def save_user():

    full_name = name.get()
    user_id = id.get()
    length_of_stay = length.get()
    room_type = rooms_option.get()
    has_breakfast = breakfast.get()
    has_parking_slot = parking_slot.get()
    has_helicopter_transport = helicopter_service.get()
    has_massage = happy_massage.get()


    if not full_name or not user_id or not length_of_stay:
        messagebox.showwarning("ERROR", "Please Fill all fields🫩... ")
        return


    try:
        length_of_stay = int(length_of_stay)
    except ValueError:
        messagebox.showwarning("ERROR","Length of stay must be an Integer...")
        return


    for letter in full_name:
        for character in "0123456789-_+=!@#$%^&*():;?/>.<,|":
            if letter == character:
                messagebox.showerror("ERROR","You can't fill the field Full Name with Special Characters or Special Symbols...")
                return


    try:
        user_id = int(user_id)
    except ValueError:
        messagebox.showerror("ERROR","You can't fill the field ID with Special Characters or Letters...")
        return


    user_data = {
        "Full Name": full_name,
        "ID": user_id,
        "Length of Stay": length_of_stay,
        "Room Type": room_type,
        "Breakfast": has_breakfast,
        "Parking Slot": has_parking_slot,
        "Helicopter Transport": has_helicopter_transport,
        "Happy Massage": has_massage
    }

    if any(user["ID"] == user_id for user in data_base):
        messagebox.showwarning("ERROR","This User is already signed into the Data Base...")
        return

    total = calculate_total(user_data)
    totals.append(total)
    data_base.append(user_data)

    messagebox.showinfo("Success", f"User data saved successfully. Total: {total}$")

    update_user_list()



def update_user_list():

    user_list.delete(0, tk.END)

    for i, user in enumerate(data_base):

        bold_map = str.maketrans("0123456789", "𝟬𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵")
        user_info = (f"{str(i+1).translate(bold_map)}. - ID: {user['ID']} - Name: {user['Full Name']} - Total: {totals[i]}$ -")

        # Inserta cada linea formateada en el Listbox
        user_list.insert(tk.END, user_info)



main_window = tk.Tk()
main_window.title(f"{'':<35}INFERNO'S GRAND HOTEL ✮⋆˙✮⋆˙✮⋆˙✮⋆˙✮⋆˙{'':>50}")



screen_width = main_window.winfo_screenwidth()     
screen_height = main_window.winfo_screenheight()   

window_width = 700                                 
window_height = screen_height - 80                


pos_x = (screen_width - window_width) // 2
pos_y = (screen_height - window_height) // 2


main_window.geometry(f"{window_width}x{window_height}+{pos_x}+{pos_y}")

main_window.resizable(False, False)              
main_window.configure(bg="#2A080C")                 



style_label = {
    "font": ("Times New Roman", 16), 
    "bg": "#2A080C", 
    "fg": "#F3E5AB"                                
}

style_entry = {
    "font": ("Segoe UI Light", 15), 
    "width": 30,
    "bg": "#1A0306",                                
    "fg": "#D4AF37",                               
    "insertbackground": "#D4AF37",                 
    "relief": tk.SOLID,
    "bd": 1,                                        
    "highlightbackground": "#821A1A",             
    "highlightcolor": "#D4AF37",                    
    "highlightthickness": 1                         
}

style_radio = {
    "font": ("Times New Roman", 13), 
    "bg": "#2A080C", 
    "fg": "#F3E5AB", 
    "selectcolor": "#1A0306",                      
    "activebackground": "#2A080C",
    "activeforeground": "#F3E5AB"
}

style_check = {
    "font": ("Times New Roman", 13), 
    "bg": "#2A080C", 
    "fg": "#F3E5AB", 
    "selectcolor": "#1A0306",                     
    "activebackground": "#2A080C",
    "activeforeground": "#F3E5AB"
}



# Entrada para Nombre Completo
tk.Label(main_window, text="Full Name:", **style_label).pack(pady=5)
name = tk.Entry(main_window, **style_entry)
name.pack(pady=5)


tk.Label(main_window, text="ID:", **style_label).pack(pady=5)
id = tk.Entry(main_window, **style_entry)
id.pack(pady=5)


tk.Label(main_window, text="Length of Stay:", **style_label).pack(pady=5)
length = tk.Entry(main_window, **style_entry)
length.pack(pady=5)



rooms_option = tk.IntVar(value=1)                  

tk.Label(main_window, text="Type of Room:", **style_label).pack(pady=5)

# Opciones de habitación
sencilla = tk.Radiobutton(main_window, text="Luxury Simple Suit (849.99$)", variable=rooms_option, value=1, **style_radio)
sencilla.pack(anchor=tk.W, padx=20)

doble = tk.Radiobutton(main_window, text="Double Premium Suit (1400$)", variable=rooms_option, value=2, **style_radio)
doble.pack(anchor=tk.W, padx=20)

suite = tk.Radiobutton(main_window, text="Exclusive Suit (5000$)", variable=rooms_option, value=3, **style_radio)
suite.pack(anchor=tk.W, padx=20)


tk.Label(main_window, text="Additional Services:", **style_label).pack(pady=5)
breakfast = tk.BooleanVar(value=False)              
parking_slot = tk.BooleanVar(value=False)         
helicopter_service = tk.BooleanVar(value=False)     
happy_massage = tk.BooleanVar(value=False)           


tk.Checkbutton(main_window, text="Premium BreakFast (+30.99$/day)", variable=breakfast, **style_check).pack(anchor=tk.W, padx=20)
tk.Checkbutton(main_window, text="Exclusive Parking Slot (+25$/day)", variable=parking_slot, **style_check).pack(anchor=tk.W, padx=20)
tk.Checkbutton(main_window, text="Helicopter Transport Ultimate Deluxe Service (+4500$/day)", variable=helicopter_service, **style_check).pack(anchor=tk.W, padx=20)
tk.Checkbutton(main_window, text="Happy Ending Massages Premium Service (250$/day)", variable=happy_massage, **style_check).pack(anchor=tk.W, padx=20)



save_button = tk.Label(
    main_window, 
    text="SAVE", 
    font=("Times New Roman", 13, "bold"), 
    bg="#821A1A",                                  
    fg="#D4AF37",                                  
    padx=25, 
    pady=6, 
    cursor="star",                                
    relief=tk.RAISED, 
    bd=3,
    highlightbackground="#D4AF37",                  
    highlightthickness=1
)


save_button.pack(pady=30)


save_button.bind("<Button-1>", lambda event: save_user()) 



user_list_label = tk.Label(main_window, text="ADDED USERS", **style_label)
user_list_label.pack(pady=10)


user_list = tk.Listbox(
    main_window, 
    width=60, 
    height=16, 
    bg="#1A0306", 
    fg="#F3E5AB", 
    selectbackground="#821A1A", 
    selectforeground="#D4AF37", 
    font=("Times New Roman", 12),
    highlightbackground="#821A1A",
    highlightcolor="#D4AF37"
)
user_list.pack(pady=10)


main_window.mainloop()
