import tkinter as tk
main = tk.Tk()

main.title('Hackathon Platformer')
gameSpace = tk.Canvas(main, width=1500, height=900)
gameSpace.pack()

main.mainloop()