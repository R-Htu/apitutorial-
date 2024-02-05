from tkinter import *
import requests

def get_quote():
    category = 'happiness'
    api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
    response = requests.get(api_url, headers={'X-Api-Key': "ZTGbVGEYTqdMtYIkwaYohQ==x4mCecbPVOgUvbgf"})
    data = response.json()
    if data:
        quote = data[0]["quote"]
        author = data[0]["author"]
        window.title(f"{author} Says...")
        canvas.itemconfig(quote_text, text=quote, font=("Arial", 12, "italic"))
    else:
        print("No quotes found in the response :(.")

window = Tk()
window.title("Author Says ....")
window.config(padx=50, pady=50)
canvas = Canvas(width=500, height=400)
try:
    background_img = PhotoImage(file="tree.png")
    canvas.create_image(150, 200, anchor="w", image=background_img)
except Exception as e:
    print(f"Error loading background image: {e}")

custom_font = ("Helvetica", 14, "bold")
quote_text = canvas.create_text(50, 200, text="Author Quote goes here", width=250, anchor="w", font=custom_font)
canvas.grid(row=0, column=0)
button = Button(text="Get Quote", command=get_quote)
button.grid(row=1, column=0)
get_quote()
window.mainloop()


