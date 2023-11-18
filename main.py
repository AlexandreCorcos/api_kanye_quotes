from tkinter import *
import requests

api_kanye = "https://api.kanye.rest/"
#quote_kanye = ""


def get_quote():
    #global quote_kanye
    response = requests.get(url=api_kanye)
    response.raise_for_status()

    data = response.json()
    quote_kanye = data["quote"]
    canvas.itemconfig(quote_text, text=quote_kanye)




window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()