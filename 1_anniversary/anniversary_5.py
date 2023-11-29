from datetime import datetime, timedelta
import emoji
from tkinter import *

root = Tk()
root.title('Test')
root.geometry('500x500')

my_lable = Label(root, text=f'{emoji.emojize(":elf_dark_skin_tone:")} {emoji.emojize(":elf_medium-light_skin_tone:")}', font=('Helvetica', 32), fg='red')
my_lable.pack(pady=50)

plus_days = 2000
wedding_day = datetime(2010, 7, 22)
the_day = wedding_day + timedelta(days=plus_days)

result = emoji.emojize(f":ring:")
result1 = "우리 결혼한지 +{0}일은 {1}년 {2}월 {3}일".format(plus_days, the_day.year, the_day.month, the_day.day)

my_lable1 = Label(root, text=result, font=('Helvetica', 20), fg='blue')
my_lable1.pack()

my_lable2 = Label(root, text=result1)
my_lable2.pack()


# print(result1)

root.mainloop()



# pip install emoji
# http://unicode.org/emoji/charts/full-emoji-list.html

# https://carpedm20.github.io/emoji/

https://076923.github.io/posts/Python-tkinter-5/