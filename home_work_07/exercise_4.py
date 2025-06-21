# Опис завдання
'''
Завдання 4 (необов'язкове завдання)

Реалізуйте структуру даних для системи коментарів так, щоб коментарі могли мати відповіді, які, в свою чергу, також могли мати відповіді, 
формуючи таким чином ієрархічну структуру.



Також візьміть до уваги наступні вимоги:

Реалізуйте клас Comment, що представляє собою окремий коментар. Він має зберігати текст коментаря, автора та список відповідей.
Метод класу add_reply має додавати нову відповідь до коментаря.
Метод класу remove_reply має видаляти відповідь із коментаря. Це має змінювати текст коментаря на стандартне повідомлення 
(наприклад, "Цей коментар було видалено.") і встановлювати прапорець is_deleted в True.
Метод display має рекурсивно виводити коментар та всі його відповіді, використовуючи відступи для відображення ієрархічної структури.


Приклад очікуваного результату:

root_comment = Comment("Яка чудова книга!", "Бодя")
reply1 = Comment("Книга повне розчарування :(", "Андрій")
reply2 = Comment("Що в ній чудового?", "Марина")

root_comment.add_reply(reply1)
root_comment.add_reply(reply2)

reply1_1 = Comment("Не книжка, а перевели купу паперу ні нащо...", "Сергій")
reply1.add_reply(reply1_1)

reply1.remove_reply()

root_comment.display()



Виведення:

Бодя: Яка чудова книга!
    Цей коментар було видалено.
        Сергій: Не книжка, а перевели купу паперу ні нащо...
    Марина: Що в ній чудового?
'''
# Виконання завдання
class Comment:
    def __init__(self, text, author):
        self.text = text
        self.author = author
        self.replies = []
        self.is_deleted = False

    def add_reply(self, reply_comment):
        """Додає відповідь до поточного коментаря"""
        self.replies.append(reply_comment)

    def remove_reply(self):
        """Позначає цей коментар як видалений"""
        self.text = "Цей коментар було видалено."
        self.is_deleted = True

    def display(self, level=0):
        """Рекурсивно виводить коментар і всі відповіді з відступами"""
        indent = "    " * level
        if self.is_deleted:
            print(f"{indent}{self.text}")
        else:
            print(f"{indent}{self.author}: {self.text}")
        for reply in self.replies:
            reply.display(level + 1)


# === Демонстрація ===

# Головний коментар
root_comment = Comment("Яка чудова книга!", "Бодя")

# Перший рівень відповідей
reply1 = Comment("Книга повне розчарування :(", "Андрій")
reply2 = Comment("Що в ній чудового?", "Марина")

root_comment.add_reply(reply1)
root_comment.add_reply(reply2)

# Вкладена відповідь до коментаря Андрія
reply1_1 = Comment("Не книжка, а перевели купу паперу ні нащо...", "Сергій")
reply1.add_reply(reply1_1)

# Видалення коментаря Андрія
reply1.remove_reply()

# Виведення ієрархії коментарів
root_comment.display()
