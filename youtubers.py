import tkinter as tk
from tkinter import messagebox
import random

class YoutuberLifeGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Youtuber's Life")
        self.master.geometry("400x300")

        self.video_title = ""
        self.views = 0
        self.subscribers = 0

        self.create_video_button = tk.Button(self.master, text="Создать видео", command=self.create_video)
        self.create_video_button.pack(pady=10)

        self.video_title_entry = tk.Entry(self.master, width=30)
        self.video_title_entry.pack(pady=10)

        self.stats_label = tk.Label(self.master, text="Просмотры: 0 | Подписчики: 0")
        self.stats_label.pack(pady=10)

    def create_video(self):
        new_video_title = self.video_title_entry.get()

        if not new_video_title:
            messagebox.showinfo("Ошибка", "Введите название видео!")
            return

        if new_video_title == self.video_title:
            # Если пользователь ввел одинаковое название видео дважды подряд
            self.views = 0
            self.subscribers -= 10  # Уменьшаем подписчиков на 10
        else:
            self.video_title = new_video_title
            # Генерация случайного числа просмотров и подписчиков
            self.views += random.randint(100, 1000)
            bad_video_chance = random.random()
            if bad_video_chance <= 0.25:
                # Если выпадает "плохое" видео
                self.views //= 2  # Уменьшаем количество просмотров вдвое
                self.subscribers -= 5  # Уменьшаем подписчиков на 5
            else:
                self.subscribers += random.randint(1, 10)

        # Обновление статистики
        self.update_stats()

        # Проверка условия победы
        if self.subscribers >= 100000:
            messagebox.showinfo("Поздравляем!", "Вы достигли 100,000 подписчиков! Вы победили!")
            self.master.destroy()  # Закрыть окно при достижении цели

    def update_stats(self):
        stats_text = f"Просмотры: {self.views} | Подписчики: {self.subscribers}"
        self.stats_label.config(text=stats_text)

if __name__ == "__main__":
    root = tk.Tk()
    game = YoutuberLifeGame(root)
    root.mainloop()
