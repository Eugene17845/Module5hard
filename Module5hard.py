import time
class User:

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):
        return f"{self.nickname}"


    def __hash__(self):
        return hash(self.password)


class Video:

    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.abult_mode = False

    def __str__(self):
        return f"{self.title}"

class UrTube:
    users = []
    videos = []
    current_user = None

    def  log_in(self, nickname, password ):
        for us in self.users:
            if nickname == us.nickname and password == us.password:
                self.current_user = us

    def register(self, nickname, password, age):
        for us in self.users:
            if nickname in us.nickname:
                print(f'Пользователь {nickname} уже есть')
                break
        else:
            n_u = User(nickname, password, age)
            self.users.append(n_u)
            self.current_user = n_u
            print(f'Пользователь {nickname} зарегестрирован и вошёл в систему')

    def log_out(self):
        self.current_user = None

    def add(self, *other):
        for vid in other:
            if vid != other:
                self.videos.append(vid)

    def get_videos(self, sl):
        list = []
        for vid in self.videos:
            if sl.upper() in vid.title.upper():
                list.append(vid.title)
        return list

    def watch_video(self, sl):
        if self.current_user and self.current_user.age < 18:
            print(f'{self.current_user} нет 18, сообщаем маме')
        elif self.current_user:
            for vid in self.videos:
                if sl in vid.title:
                    for a in range(1, 11):
                        print(a, end=' ')
                        time.sleep(1)
                    print('Конец видео')

        else:
            print('Войдите в аккаунт, что бы смотреть')

    def __str__(self):
        return f"{self.videos}"
if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')
