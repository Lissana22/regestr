from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Викторина")
root.geometry("500x500")

def que_one():
    question = Label(root, text="Кто стоял во главе славянского языческого пантеона богов?")
    answer = Entry()
    btn = Button(root, text= "Ответить", command=lambda: game1(que_two))
    question.grid()
    answer.grid()
    btn.grid()

    def game1(que_two):
        if answer.get().lower() == "перун":
            que_two()
        else:
            messagebox.showerror("Ощибка!", "Попробуй еще раз!")



def que_two():
    question_2 = Label(root, text="В каком году произошло крещение Руси?")
    answer_2= Entry()
    btn_2 = Button(root, text= "Ответить", command=lambda: game2(que_three))
    question_2.grid()
    answer_2.grid()
    btn_2.grid()

    def game2(que_three):
        if answer_2.get() == "988":
            que_three()
        else:
            messagebox.showerror("Ощибка!", "Попробуй еще раз!")

def que_three():
    question_3 = Label(root, text="В каком году состоялась Куликовская битва?")
    answer_3= Entry()
    btn_3 = Button(root, text= "Ответить", command=lambda: game3(que_four))
    question_3.grid()
    answer_3.grid()
    btn_3.grid()

    def game3(que_four):
        if answer_3.get() == "1380":
            que_four()
        else:
            messagebox.showerror("Ощибка!", "Попробуй еще раз!")

def que_four():
    question_4 = Label(root, text="Как звали первого царя из дома Романовых?")
    answer_4 = Entry()
    btn_4 = Button(root, text= "Ответить", command=lambda: game4(que_four))
    question_4.grid()
    answer_4.grid()
    btn_4.grid()

    def game4(que_four):
        if answer_4.get() == "Михаил":
            messagebox.showinfo("Победа", "Ты молодец")
        else:
            messagebox.showerror("Ощибка!", "Попробуй еще раз!")

que_one()

root.mainloop()


