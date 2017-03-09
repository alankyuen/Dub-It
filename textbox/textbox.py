import string
import pygame as pg


ACCEPTED = string.ascii_letters+string.digits+string.punctuation+" "
VOCABULARY_FILE = 'trump_words.txt'

class TextBox(object):
    def __init__(self,rect,**kwargs):
        self.rect = pg.Rect(rect)
        self.buffer = []
        self.final = None
        self.rendered = None
        self.render_rect = None
        self.render_area = None
        self.blink = True
        self.blink_timer = 0.0
        self.process_kwargs(kwargs)
        self.buffer_bookmark = 0
        self.words_to_transcribe = []

    def process_kwargs(self,kwargs):
        defaults = {"id" : None,
                    "command" : None,
                    "active" : True,
                    "color" : pg.Color("white"),
                    "font_color" : pg.Color("black"),
                    "outline_color" : pg.Color("black"),
                    "outline_width" : 2,
                    "active_color" : pg.Color("blue"),
                    "font" : pg.font.Font(None, 60),
                    "clear_on_enter" : False,
                    "inactive_on_enter" : True}
        for kwarg in kwargs:
            if kwarg in defaults:
                defaults[kwarg] = kwargs[kwarg]
            else:
                raise KeyError("InputBox accepts no keyword {}.".format(kwarg))
        self.__dict__.update(defaults)

    def get_event(self,event):
        if event.type == pg.KEYDOWN and self.active:
            if event.key in (pg.K_RETURN,pg.K_KP_ENTER):
                word = "".join(self.buffer[self.buffer_bookmark:])
                if " "+word+" " in open(VOCABULARY_FILE).read():
                    
                    self.words_to_transcribe.append(word)
                    self.buffer.append(' ')
                    self.buffer_bookmark = len(self.buffer)
                else:
                    for i in range(len(self.buffer) - self.buffer_bookmark):
                        self.buffer.pop()
                    print(word + " is not in his vocabulary...")
                self.execute()
            elif event.key == pg.K_BACKSPACE:
                if self.buffer and self.buffer[len(self.buffer)-1] is not ' ':
                    self.buffer.pop()

            elif event.key == pg.K_SPACE:
                word = "".join(self.buffer[self.buffer_bookmark:])
                if " "+word+" " in open(VOCABULARY_FILE).read():
                    
                    self.words_to_transcribe.append(word)
                    self.buffer.append(' ')
                    self.buffer_bookmark = len(self.buffer)
                else:
                    for i in range(len(self.buffer) - self.buffer_bookmark):
                        print(self.buffer.pop())
                    print(word + " is not in his vocabulary...")

            elif event.key == pg.K_ESCAPE:
                self.words_to_transcribe = []
                self.buffer = []
                self.buffer_bookmark = 0

            elif event.unicode in ACCEPTED:
                self.buffer.append(event.unicode.encode('ascii','ignore'))

        elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            self.active = self.rect.collidepoint(event.pos)

    def execute(self):
        if self.command:
            self.command(self.words_to_transcribe)
            self.words_to_transcribe = []
            self.buffer_bookmark = 0
            self.buffer = []
        self.active = not self.inactive_on_enter
        if self.clear_on_enter:
            self.buffer = []


    def update(self):
        new = "".join(self.buffer)
        if new != self.final:
            self.final = new
            self.rendered = self.font.render(self.final, True, self.font_color)
            self.render_rect = self.rendered.get_rect(x=self.rect.x+3,
                                                      centery=self.rect.y + 35)
            if self.render_rect.width > self.rect.width-6:
                offset = self.render_rect.width-(self.rect.width-6)
                self.render_area = pg.Rect(offset,0,self.rect.width-6,
                                           self.render_rect.height)
            else:
                self.render_area = self.rendered.get_rect(topleft=(0,0))
        if pg.time.get_ticks()-self.blink_timer > 200:
            self.blink = not self.blink
            self.blink_timer = pg.time.get_ticks()

    def draw(self,surface):
        outline_color = self.active_color if self.active else self.outline_color
        outline = self.rect.inflate(self.outline_width*2,self.outline_width*2)
        surface.fill(outline_color,outline)
        surface.fill(self.color,self.rect)
        if self.rendered:
            surface.blit(self.rendered,self.render_rect,self.render_area)
        if self.blink and self.active:
            curse = self.render_area.copy()
            curse.topleft = self.render_rect.topleft
            surface.fill(self.font_color,(curse.right+1,curse.y,2,curse.h))
