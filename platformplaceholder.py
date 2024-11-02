import tkinter as tk
main = tk.Tk()

main.title('Hackathon Platformer')
gameSpace = tk.Canvas(main, width=1500, height=900)
gameSpace.pack()

gameSpace.create_rectangle((100, 200), (900, 300), fill='green')

main.mainloop()