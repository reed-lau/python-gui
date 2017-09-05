# get screen size
root.winfo_screenwidth()
root.winfo_screenheight()

# get window size
root.winfo_width()
root.winfo_height()

# requesting window size
root.winfo_reqwidth()
root.winfo_reqheight()

# when it did could not get the size before showing it, you can call update before 
root.update()
