class song(object):
    def __int__(self, lyrics):
        self.lyrics = lyrics

    def sign_me_a_song(self):
        for line in self.lyrics:
            print(line)


happy_birthday = song['May god bless you, ,', 'Have a sunshine on you,', 'Happy Birthday to you !']
print(happy_birthday.sign_me_a_song())


