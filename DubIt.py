import os
import sys
import pygame as pg
from textbox import TextBox
from pydub import AudioSegment

KEY_REPEAT_SETTING = (200,70)

"""input is [] of words"""
sounds = []
def texttospeech(words):
    if(len(words) == 0):
        return
    original_path = os.getcwd()
    path_of_words = original_path + "/trump_words"
    os.chdir(path_of_words)
    entire_folder = os.listdir(path_of_words)

    time=60

    word = words[0]
    word = word.lower()

    if not (word + ".wav") in entire_folder:
        print(word +" not recorded")
    audio = AudioSegment.from_wav(word + ".wav")
    final_product = audio+AudioSegment.silent(duration=time)
    words = words[1:]

    for word in words:
        word = word.lower()
        if not (word + ".wav") in entire_folder:
            print(word + " not recorded")
        audio = AudioSegment.from_wav(word + ".wav")+AudioSegment.silent(duration=time)
        final_product += audio
    os.chdir(original_path)

    final_product.export("Final product.wav", format="wav")

class Control(object):
    def __init__(self):
        pg.init()
        pg.mixer.init()

        pg.display.set_caption("Dub_It")
        self.screen = pg.display.set_mode((780,220))
        self.clock = pg.time.Clock()
        self.fps = 60.0
        self.done = False
        self.input = TextBox((30,100,715,75),command=self.speech_to_speech,
                              clear_on_enter=True,inactive_on_enter=False)
        self.color = (100,100,100)
        self.prompt = self.make_prompt()
        pg.key.set_repeat(*KEY_REPEAT_SETTING)

    def make_prompt(self):
        font = pg.font.SysFont("arial", 60)
        message = 'WHAT WOULD TRUMP SAY?'
        rend = font.render(message, True, pg.Color("red"))
        return (rend, rend.get_rect(topleft=(80,35)))

    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
            self.input.get_event(event)

    def play_speech(self, speech_path):
        pg.mixer.music.set_volume(1)
        pg.mixer.init()
        sounds.append(pg.mixer.Sound(speech_path))
        pg.mixer.Sound.play(sounds[len(sounds)-1])

    def speech_to_speech(self, speech):
        texttospeech(speech)
        self.play_speech('Final product.wav')

    def main_loop(self):
        while not self.done:
            self.event_loop()
            self.input.update()
            self.screen.fill(self.color)
            self.input.draw(self.screen)
            self.screen.blit(*self.prompt)
            pg.display.update()
            self.clock.tick(self.fps)

sounds = []
soundscounter = 0

if __name__ == "__main__":
    sounds = []
    soundscounter = 0
    app = Control()
    app.main_loop()
    pg.quit()
    sys.exit()
