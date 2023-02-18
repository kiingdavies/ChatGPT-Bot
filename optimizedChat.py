from tkinter import *
import customtkinter
import openai
import os
import pickle

root = customtkinter.CTk()
root.title("ChatGPT Bot")
root.geometry('600x600')
root.iconbitmap('ai_lt.ico')

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

def speak():
    if chat_entry.get():
        filename = "api_key"
        try:
            if os.path.isfile(filename):
                with open(filename, "rb") as input_file:
                    stuff = pickle.load(input_file)
                    openai.api_key = stuff
                    openai.Model.list()
                    response = openai.Completion.create(
                        model="text-davinci-003",
                        prompt=chat_entry.get(),
                        temperature=0,
                        max_tokens=60,
                        top_p=1.0,
                        frequency_penalty=0.0,
                        presence_penalty=0.0,
                    )
                    my_text.insert(END, (response["choices"][0]["text"]).strip() + "\n\n")
            else:
                with open(filename, "wb") as input_file:
                    pass
                my_text.insert(
                    END,
                    "\n\n You Need to Add Your API Key To Talk With ChatGPT. Get one here:\nhttps://platform.openai.com/account/api-keys",
                )
        except Exception as e:
            my_text.insert(END, f"\n\n There was an error\n\n{e}")
    else:
        my_text.insert(END, "\nHey! You Forgot To Type something!")

def clear():
    my_text.delete(1.0, END)
    chat_entry.delete(0, END)

def key():
    filename = "api_key"
    try:
        if os.path.isfile(filename):
            with open(filename, "rb") as input_file:
                stuff = pickle.load(input_file)
                api_entry.insert(END, stuff)
        else:
            with open(filename, "wb") as input_file:
                # Close the file
                input_file.close()
    except Exception as e:
        my_text.insert(END, f"\n\n There was an error\n\n{e}")
    root.geometry('600x750')
    api_frame.pack(pady=30)

def save_key():
    filename = "api_key"
    try:
        with open(filename, "wb") as output_file:
            pickle.dump(api_entry.get(), output_file)
            api_entry.delete(0, END)
            api_frame.pack_forget()
            root.geometry('600x600')
    except Exception as e:
        my_text.insert(END, f"\n\n There was an error\n\n{e}")

text_frame = customtkinter.CTkFrame(root)
text_frame.pack(pady=20)

my_text = Text(
    text_frame,
    bg="#343638",
    width=65,
    bd=1,
    fg="#d6d6d6",
    relief="flat",
    wrap=WORD,
    selectbackground="#1f538d",
)
my_text.grid(row=0, column=0)

text_scroll = customtkinter.CTkScrollbar(text_frame, command=my_text.yview)
text_scroll.grid(row=0, column=1, sticky="ns")

my_text.configure(yscrollcommand=text_scroll.set)


# Entry Widget To Type Stuff to ChatGPT
chat_entry = customtkinter.CTkEntry(root,
    placeholder_text="Ask ChatGPT anything...",
    width=535,
    height=50,
    border_width=1.5)
chat_entry.pack(pady=10)    


# Create Button Frame
button_frame = customtkinter.CTkFrame(root, fg_color="#242424")
button_frame.pack(pady=10)

# Create Submit Button
submit_button = customtkinter.CTkButton(button_frame, 
    text="Speak Question To ChatGPT",
    command=speak)
submit_button.grid(row=0, column=0, padx=25)

# Create Clear Button
clear_button = customtkinter.CTkButton(button_frame, 
    text="Clear Response",
    command=clear)
clear_button.grid(row=0, column=1, padx=35)

# Create API Button
api_button = customtkinter.CTkButton(button_frame, 
    text="Update API Key",
    command=key)
api_button.grid(row=0, column=2, padx=25)

# Add API Key Frame
api_frame = customtkinter.CTkFrame(root, border_width=1)
api_frame.pack(pady=30)

# Add API Entry Widget
api_entry = customtkinter.CTkEntry(api_frame, 
    placeholder_text="Enter Your API Key",
    width=350, height=50, border_width=1)
api_entry.grid(row=0, column=0, padx=20, pady=20)    

# Add API Button
api_save_button = customtkinter.CTkButton(api_frame,
    text="Save Key",
    command=save_key)
api_save_button.grid(row=0, column=1, padx=10)  



root.mainloop()
