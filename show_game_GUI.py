from tkinter import *
from tkinter import messagebox
from tkinter.font import *

from words_game import ScorePlayer


def game():

    # calculate and shows the result of each player in messagebox
    def show_result():
        word_one = user1_entry.get()
        word_two = user2_entry.get()
        messagebox.showinfo('Result',\
             f'First Word: {word_one}\nScore: {ScorePlayer.calculate_word_score(word_one)}\n\nSecond Word: {word_two}\nScore: {ScorePlayer.calculate_word_score(word_two)}')
        messagebox.showinfo('Winner', ScorePlayer.find_winner(word_one, word_two))
        messagebox.showinfo('Scores', f'First Player: {ScorePlayer.player_1}\n\nSconed Player: {ScorePlayer.player_2}')

    # try to increase the scores of players
    def cal_result():
        try:
            ScorePlayer.player_1 += ScorePlayer.calculate_word_score(user1_entry.get())
        except ValueError:
            messagebox.showerror('Invalid Word', 'First Player word is Invaild')
        
        try:
            ScorePlayer.player_2 += ScorePlayer.calculate_word_score(user2_entry.get())
        except ValueError:
            messagebox.showerror('Invalid Word', 'Second Player word is Invaild')

        show_result()

        user1_entry.delete(0, END)
        user2_entry.delete(0, END)

    # reset the scores to 0
    def reset():
        ScorePlayer.player_1 = 0
        ScorePlayer.player_2 = 0


    #show the entry and buttons to players
    window = Tk()

    my_font = Font(family='Helvatica' , size=20)
    my_font_2 = Font(family='Consolas' , size=15)

    window.geometry("550x300")
    window.title("Menu")

    window['bg'] = '#ffcccb'

    rule_label = Label(window, text="Each player should write a specific word")
    rule_label.grid(row=0,column=0, columnspan=2, padx=15, pady=15)

    user1_label = Label(window, text="First Player: ", font=my_font_2)
    user1_label.grid(row=1,column=0, padx=15, pady=15)

    user1_entry = Entry(width=15, font= my_font)
    user1_entry.grid(row=1, column=1, padx=10, pady=15)


    user2_label = Label(window, text="Second Player: ", font=my_font_2)
    user2_label.grid(row=2,column=0, padx=30, pady=15)

    user2_entry = Entry(width=15, font= my_font)
    user2_entry.grid(row=2, column=1, padx=10, pady=15)


    result_button = Button(window, text='SHOW RESULT', font = my_font_2, bg='yellow',\
                            height= 2, command=cal_result)
    result_button.grid(row=3,column=0, pady=15)

    reset_button = Button(window, text='RESET', bg='red', command=reset)
    reset_button.grid(row=3,column=1, padx=30, pady=15)


    window.mainloop()
