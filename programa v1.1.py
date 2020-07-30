from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.app import MDApp
from kivy.lang import Builder
import Apileague
from kivy.properties import ObjectProperty
import requests
from threading import Thread
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.clock import Clock, ClockBaseInterrupt
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.list import OneLineAvatarListItem
screen_helper = """
ScreenManager:
    id: screen_management
    prof : prof
    men : men
    MenuScreen:
        id : men

            
    ProfileScreen:
        id : prof
<MenuScreen>:
    sear8h: id_searc
    name: 'menu'
    canvas.before:

        Color:
            rgba: rgba('#052336')
        Triangle
            points: [0, self.size[1], self.size[0], self.size[1], self.size[0], self.size[1] - (.4*self.size[1])]
        Color:
            rgba: rgba('#123a4d')
        Triangle
            points: [0, self.size[1], self.size[0], self.size[1], 0, self.size[1] - (.4*self.size[1])]
       
    MDRectangleFlatButton:
        text: 'Search'
        pos_hint: {'center_x':0.5,'center_y':0.4}
        on_release: root.startdata()


    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.7,'top':1}
        on_press: root.manager.current = 'profile'
        
    MDTextField:
        id: id_searc
        hint_text: "Summoner name"
        helper_text: "You need to be in an active game"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.5, 'center_y': 0.6}
        size_hint_x:None
        width:170

<ProfileScreen>:
    name: 'profile'
    avatar1 : avatar1
    avatar2 : avatar2
    avatar3 : avatar3
    avatar4 : avatar4
    avatar5 : avatar5
    ul1 : ul1
    ul2 : ul2
    ul3 : ul3
    ul4 : ul4
    ul5 : ul5
    sp1_1 : sp1_1
    sp1_2 : sp1_2
    sp2_1 : sp2_1
    sp2_2 : sp2_2
    sp3_1 : sp3_1
    sp3_2 : sp3_2
    sp4_1 : sp4_1
    sp4_2 : sp4_2
    sp5_1 : sp5_1
    sp5_2 : sp5_2
    spelln1:spelln1
    spelln2:spelln2
    spelln3:spelln3
    spelln4:spelln4
    spelln5:spelln5
    spelln6:spelln6
    spelln7:spelln7
    spelln8:spelln8
    spelln9:spelln9
    spelln10:spelln10
    ult1:ult1
    ult2:ult2
    ult3:ult3
    ult4:ult4
    ult5:ult5
    champ1 : champ1
    champ2:champ2
    champ3:champ3
    champ4:champ4
    champ5:champ5
    champ1cd:champ1cd
    champ2cd:champ2cd
    champ3cd:champ3cd
    champ4cd:champ4cd
    champ5cd:champ5cd
    AsyncImage:
        id: avatar1
        size_hint: (None,None)
        nocache: True
        width: 65
        height: 65
        pos_hint:{'center_x': 0.2, 'center_y': 0.1}
        source: f""
        anim_delay: 0.1
    AsyncImage:
        id: avatar2
        pos_hint:{'center_x': 0.2, 'center_y': 0.3}
        size_hint: (None,None)
        width: 65
        height: 65
        source: f""
    AsyncImage:
        id: avatar3
        pos_hint:{'center_x': 0.2, 'center_y': 0.5}
        size_hint: (None,None)
        width: 65
        height: 65
        source: f""
    AsyncImage:
        id: avatar4
        pos_hint:{'center_x': 0.2, 'center_y': 0.7}
        size_hint: (None,None)
        width: 65
        height: 65
        source: f""
    AsyncImage:
        id: avatar5
        pos_hint:{'center_x': 0.2, 'center_y': 0.9}
        size_hint: (None,None)
        width: 65
        height: 65
        source: f""
    AsyncImage:
        id: ul1
        size_hint: (None,None)
        nocache: True
        width: 65
        height: 65
        pos_hint:{'center_x': 0.3, 'center_y': 0.1}
        source: f""
    AsyncImage:
        id: ul2
        pos_hint:{'center_x': 0.3, 'center_y': 0.3}
        size_hint: (None,None)
        width: 65
        height: 65
        source: f""
    AsyncImage:
        id: ul3
        pos_hint:{'center_x': 0.3, 'center_y': 0.5}
        size_hint: (None,None)
        width: 65
        height: 65
        source: f""
    AsyncImage:
        id: ul4
        pos_hint:{'center_x': 0.3, 'center_y': 0.7}
        size_hint: (None,None)
        width: 65
        height: 65
        source: f""
    AsyncImage:
        id: ul5
        pos_hint:{'center_x': 0.3, 'center_y': 0.9}
        size_hint: (None,None)
        width: 65
        height: 65
        source: f""
    AsyncImage:
        id: sp1_1
        size_hint: (None,None)
        nocache: True
        width: 65
        height: 65
        pos_hint:{'center_x': 0.4, 'center_y': 0.1}
        source: f""
    AsyncImage:
        id: sp1_2
        pos_hint:{'center_x': 0.5, 'center_y': 0.1}
        size_hint: (None,None)
        width: 65
        height: 65
        source: f""
    AsyncImage:
        id: sp2_1
        pos_hint:{'center_x': 0.4, 'center_y': 0.3}
        size_hint: (None,None)
        width: 65
        height: 65
        source: f""
    AsyncImage:
        id: sp2_2
        pos_hint:{'center_x': 0.5, 'center_y': 0.3}
        size_hint: (None,None)
        width: 65
        height: 65
        source: f""
    AsyncImage:
        id: sp3_1
        pos_hint:{'center_x': 0.4, 'center_y': 0.5}
        size_hint: (None,None)
        width: 65
        height: 65
        source: f""
    AsyncImage:
        id: sp3_2
        size_hint: (None,None)
        nocache: True
        width: 65
        height: 65
        pos_hint:{'center_x': 0.5, 'center_y': 0.5}
        source: f""
    AsyncImage:
        id: sp4_1
        pos_hint:{'center_x': 0.4, 'center_y': 0.7}
        size_hint: (None,None)
        width: 65
        height: 65
        source: f""
    AsyncImage:
        id: sp4_2
        pos_hint:{'center_x': 0.5, 'center_y': 0.7}
        size_hint: (None,None)
        width: 65
        height: 65
        source: f""
    AsyncImage:
        id: sp5_1
        pos_hint:{'center_x': 0.4, 'center_y': 0.9}
        size_hint: (None,None)
        width: 65
        height: 65
        source: f""
    AsyncImage:
        id: sp5_2
        pos_hint:{'center_x': 0.5, 'center_y': 0.9}
        size_hint: (None,None)
        width: 65
        height: 65
        source: f""

    Button:
        id:ult5
        text: ''
        font_size: "25sp"
        background_color: 0, 0, 0, 0
        size_hint: (None,None)
        width: 65
        height: 65
        background_color : 1, 1, 1, 0
        text_color: 0, 0, 1, 1
        pos_hint: {'center_x':0.3,'center_y':0.9}
        on_press: root.timeult5()
    Button:
        id:ult4
        text: ''
        font_size: "25sp"
        background_color: 0, 0, 0, 0
        size_hint: (None,None)
        width: 65
        height: 65
        background_color : 1, 1, 1, 0
        text_color: 0, 0, 1, 1
        pos_hint: {'center_x':0.3,'center_y':0.7}
        on_press: root.timeult4()
    Button:
        id:ult3
        text: ''
        font_size: "25sp"
        background_color: 0, 0, 0, 0
        size_hint: (None,None)
        width: 65
        height: 65
        background_color : 1, 1, 1, 0
        text_color: 0, 0, 1, 1
        pos_hint: {'center_x':0.3,'center_y':0.5}
        on_press: root.timeult3()
    Button:
        id:ult2
        text: ''
        font_size: "25sp"
        background_color: 0, 0, 0, 0
        size_hint: (None,None)
        width: 65
        height: 65
        background_color : 1, 1, 1, 0
        text_color: 0, 0, 1, 1
        pos_hint: {'center_x':0.3,'center_y':0.3}
        on_press: root.timeult2()
    Button:
        id:ult1
        text: ''
        font_size: "25sp"
        background_color: 0, 0, 0, 0
        size_hint: (None,None)
        width: 65
        height: 65
        background_color : 1, 1, 1, 0
        text_color: 0, 0, 1, 1
        pos_hint: {'center_x':0.3,'center_y':0.1}
        on_press: root.timeult1()
    Button:
        id:spelln1
        text: ''
        font_size: "25sp"
        background_color: 0, 0, 0, 0
        size_hint: (None,None)
        width: 65
        height: 65
        background_color : 1, 1, 1, 0
        text_color: 0, 0, 1, 1
        pos_hint: {'center_x':0.4,'center_y':0.1}
        on_press: root.timespell1()
    Button:
        id:spelln2
        text: ''
        font_size: "25sp"
        background_color: 0, 0, 0, 0
        size_hint: (None,None)
        width: 65
        height: 65
        background_color : 1, 1, 1, 0
        text_color: 0, 0, 1, 1
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.timespell2()
    Button:
        id:spelln3
        text: ''
        font_size: "25sp"
        background_color: 0, 0, 0, 0
        size_hint: (None,None)
        width: 65
        height: 65
        background_color : 1, 1, 1, 0
        text_color: 0, 0, 1, 1
        pos_hint: {'center_x':0.4,'center_y':0.3}
        on_press: root.timespell3()
    Button:
        id:spelln4
        text: ''
        font_size: "25sp"
        background_color: 0, 0, 0, 0
        size_hint: (None,None)
        width: 65
        height: 65
        background_color : 1, 1, 1, 0
        text_color: 0, 0, 1, 1
        pos_hint: {'center_x':0.5,'center_y':0.3}
        on_press: root.timespell4()
    Button:
        id:spelln5
        text: ''
        font_size: "25sp"
        background_color: 0, 0, 0, 0
        size_hint: (None,None)
        width: 65
        height: 65
        background_color : 1, 1, 1, 0
        text_color: 0, 0, 1, 1
        pos_hint: {'center_x':0.4,'center_y':0.5}
        on_press: root.timespell5()
    Button:
        id:spelln6
        text: ''
        font_size: "25sp"
        background_color: 0, 0, 0, 0
        size_hint: (None,None)
        width: 65
        height: 65
        background_color : 1, 1, 1, 0
        text_color: 0, 0, 1, 1
        pos_hint: {'center_x':0.5,'center_y':0.5}
        on_press: root.timespell6()
    Button:
        id:spelln7
        text: ''
        font_size: "25sp"
        background_color: 0, 0, 0, 0
        size_hint: (None,None)
        width: 65
        height: 65
        background_color : 1, 1, 1, 0
        text_color: 0, 0, 1, 1
        pos_hint: {'center_x':0.4,'center_y':0.7}
        on_press: root.timespell7()
    Button:
        id:spelln8
        text: ''
        font_size: "25sp"
        background_color: 0, 0, 0, 0
        size_hint: (None,None)
        width: 65
        height: 65
        background_color : 1, 1, 1, 0
        text_color: 0, 0, 1, 1
        pos_hint: {'center_x':0.5,'center_y':0.7}
        on_press: root.timespell8()
    Button:
        id:spelln9
        text: ''
        font_size: "25sp"
        background_color: 0, 0, 0, 0
        size_hint: (None,None)
        width: 65
        height: 65
        background_color : 1, 1, 1, 0
        text_color: 0, 0, 1, 1
        pos_hint: {'center_x':0.4,'center_y':0.9}
        on_press: root.timespell9()
    Button:
        id:spelln10
        text: ''
        font_size: "25sp"
        background_color: 0, 0, 0, 0
        size_hint: (None,None)
        width: 65
        height: 65
        background_color : 1, 1, 1, 0
        text_color: 0, 0, 1, 1
        pos_hint: {'center_x':0.5,'center_y':0.9}
        on_press: root.timespell10()
    MDDropDownItem:
        id: champ1
        pos_hint: {'center_x': 0.1, 'center_y': 0.05}
        text: 'Lv:6'
        on_release: app.menu.open()
    MDDropDownItem:
        id: champ1cd
        pos_hint: {'center_x': 0.1, 'center_y': 0.15}
        text: 'Cdr:0'
        on_release: app.menucdr.open()
    MDDropDownItem:
        id: champ2
        pos_hint: {'center_x': 0.1, 'y': 0.25}
        text: 'Lv:6'
        on_release: app.menu2.open()
    MDDropDownItem:
        id: champ2cd
        pos_hint: {'center_x': 0.1, 'y': 0.3}
        text: 'Cdr:0'
        on_release: app.menucdr2.open()
    MDDropDownItem:
        id: champ3
        pos_hint: {'center_x': 0.1, 'y': 0.45}
        text: 'Lv:6'
        on_release: app.menu3.open()
    MDDropDownItem:
        id: champ3cd
        pos_hint: {'center_x': 0.1, 'y': 0.5}
        text: 'Cdr:0'
        on_release: app.menucdr3.open()
    MDDropDownItem:
        id: champ4
        pos_hint: {'center_x': 0.1, 'y': 0.65}
        text: 'Lv:6'
        on_release: app.menu4.open()
    MDDropDownItem:
        id: champ4cd
        pos_hint: {'center_x': 0.1, 'y': 0.7}
        text: 'Cdr:0'
        on_release: app.menucdr4.open()
    MDDropDownItem:
        id: champ5
        pos_hint: {'center_x': 0.1, 'y': 0.85}
        text: 'Lv:6'
        on_release: app.menu5.open()
    MDDropDownItem:
        id: champ5cd
        pos_hint: {'center_x': 0.1, 'y': 0.9}
        text: 'Cdr:0'
        on_release: app.menucdr5.open()
        
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'right':1,'top':1}
        on_press: root.manager.current = 'menu'

"""

versao = requests.get('https://ddragon.leagueoflegends.com/api/versions.json').json()[0]


class Screen_Management(ScreenManager):
    men = ObjectProperty(None)
    prof = ObjectProperty(None)


class MenuScreen(Screen):

    def startdata(self):
        if self.sear8h.text is "":
            user_error = "Please enter a username"

            self.dialog = MDDialog(title='Username check',
                                   text=user_error, size_hint=(0.8, 1),
                                   buttons=[MDFlatButton(text='Close', on_release=lambda *args: self.dialog.dismiss())],
                                   auto_dismiss=True)

            self.dialog.open()
        else:

            self.pop = MDDialog(title='Searching for active game...',
                                size_hint=(0.8, 1),auto_dismiss=True)
            self.pop.open()

            self.data = Thread(target=self.show_data)
            self.data.start()

    def show_data(self):

        self.champs = Apileague.aplicativo(self.manager.men.sear8h.text)
        print(self.champs)
        if self.champs is not None:
            self.manager.prof.ultscampeaoes()
            self.manager.prof.tradwwwe()
            self.pop.dismiss()
            self.manager.current = 'profile'
        self.pop.dismiss()

    pass


class ProfileScreen(Screen):

    def timeult1(self):
        if self.ult1.background_color == [1, 1, 1, 0.5]:
            self.ult1.background_color = 1, 1, 1, 0
            self.ult1.text = ''
            Clock.unschedule(self.gf1)
        else:
            self.ult1.background_color = 1, 1, 1, 0.5

            CDR = int(''.join(filter(str.isdigit, self.champ1cd.text)))

            print(CDR)
            if self.manager.prof.champ1.text == 'Lv:6':
                self.Cronometro1 = self.Ultimatecds[0][0]
            elif self.manager.prof.champ1.text == 'Lv:11':
                self.Cronometro1 = self.Ultimatecds[0][1]
            else:
                self.Cronometro1 = self.Ultimatecds[0][2]

            self.Cronometro1 = self.Cronometro1 - (self.Cronometro1 * CDR / 100)

            Clock.unschedule(self.gf1)
            Clock.schedule_interval(self.gf1, 1)
            self.ult1.text = str(f'{self.Cronometro1:.0f}')

    def gf1(self, dt):

        self.Cronometro1 = self.Cronometro1 - 1
        self.ult1.text = str(f'{self.Cronometro1:.0f}')
        print(int(self.Cronometro1))
        if self.Cronometro1 < 1:
            self.ult1.background_color = 1, 1, 1, 0
            self.ult1.text = ''
            Clock.unschedule(self.gf1)

    def timeult2(self):
        if self.ult2.background_color == [1, 1, 1, 0.5]:
            self.ult2.background_color = 1, 1, 1, 0
            self.ult2.text = ''
            Clock.unschedule(self.gf2)
        else:
            self.ult2.background_color = 1, 1, 1, 0.5

            print(self.ult2.background_color)
            CDR = int(''.join(filter(str.isdigit, self.champ2cd.text)))

            print(CDR)
            if self.manager.prof.champ2.text == 'Lv:6':
                self.Cronometro2 = self.Ultimatecds[1][0]
            elif self.manager.prof.champ2.text == 'Lv:11':
                self.Cronometro2 = self.Ultimatecds[1][1]
            else:
                self.Cronometro2 = self.Ultimatecds[1][2]

            self.Cronometro2 = self.Cronometro2 - (self.Cronometro2 * CDR / 100)

            Clock.unschedule(self.gf2)
            Clock.schedule_interval(self.gf2, 1)
            self.ult2.text = str(f'{self.Cronometro2:.0f}')

    def gf2(self, dt):

        self.Cronometro2 = self.Cronometro2 - 1
        self.ult2.text = str(f'{self.Cronometro2:.0f}')
        print(int(self.Cronometro2))
        if self.Cronometro2 < 1:
            self.ult2.background_color = 1, 1, 1, 0
            self.ult2.text = ''
            Clock.unschedule(self.gf2)

    def timeult3(self):
        if self.ult3.background_color == [1, 1, 1, 0.5]:
            self.ult3.background_color = 1, 1, 1, 0
            self.ult3.text = ''
            Clock.unschedule(self.gf3)
        else:
            self.ult3.background_color = 1, 1, 1, 0.5

            print(self.ult3.background_color)
            CDR = int(''.join(filter(str.isdigit, self.champ3cd.text)))

            print(CDR)
            if self.manager.prof.champ3.text == 'Lv:6':
                self.Cronometro3 = self.Ultimatecds[2][0]
            elif self.manager.prof.champ3.text == 'Lv:11':
                self.Cronometro3 = self.Ultimatecds[2][1]
            else:
                self.Cronometro3 = self.Ultimatecds[2][2]

            self.Cronometro3 = self.Cronometro3 - (self.Cronometro3 * CDR / 100)

            Clock.unschedule(self.gf3)
            Clock.schedule_interval(self.gf3, 1)
            self.ult3.text = str(f'{self.Cronometro3:.0f}')

    def gf3(self, dt):

        self.Cronometro3 = self.Cronometro3 - 1
        self.ult3.text = str(f'{self.Cronometro3:.0f}')
        print(int(self.Cronometro3))
        if self.Cronometro3 < 1:
            self.ult3.background_color = 1, 1, 1, 0
            self.ult3.text = ''
            Clock.unschedule(self.gf3)

    def timeult4(self):
        if self.ult4.background_color == [1, 1, 1, 0.5]:
            self.ult4.background_color = 1, 1, 1, 0
            self.ult4.text = ''
            Clock.unschedule(self.gf4)
        else:
            self.ult4.background_color = 1, 1, 1, 0.5

            print(self.ult4.background_color)
            CDR = int(''.join(filter(str.isdigit, self.champ4cd.text)))

            print(CDR)
            if self.manager.prof.champ4.text == 'Lv:6':
                self.Cronometro4 = self.Ultimatecds[3][0]
            elif self.manager.prof.champ4.text == 'Lv:11':
                self.Cronometro4 = self.Ultimatecds[3][1]
            else:
                self.Cronometro4 = self.Ultimatecds[3][2]

            self.Cronometro4 = self.Cronometro4 - (self.Cronometro4 * CDR / 100)

            Clock.unschedule(self.gf4)
            Clock.schedule_interval(self.gf4, 1)
            self.ult4.text = str(f'{self.Cronometro4:.0f}')

    def gf4(self, dt):

        self.Cronometro4 = self.Cronometro4 - 1
        self.ult4.text = str(f'{self.Cronometro4:.0f}')
        print(int(self.Cronometro4))
        if self.Cronometro4 < 1:
            self.ult4.background_color = 1, 1, 1, 0
            self.ult4.text = ''
            Clock.unschedule(self.gf4)

    def timeult5(self):
        if self.ult5.background_color == [1, 1, 1, 0.5]:
            self.ult5.background_color = 1, 1, 1, 0
            self.ult5.text = ''
            Clock.unschedule(self.gf5)
        else:
            self.ult5.background_color = 1, 1, 1, 0.5

            print(self.ult5.background_color)
            CDR = int(''.join(filter(str.isdigit, self.champ5cd.text)))

            print(CDR)
            if self.manager.prof.champ5.text == 'Lv:6':
                self.Cronometro5 = self.Ultimatecds[4][0]
            elif self.manager.prof.champ5.text == 'Lv:11':
                self.Cronometro5 = self.Ultimatecds[4][1]
            else:
                self.Cronometro5 = self.Ultimatecds[4][2]

            self.Cronometro5 = self.Cronometro5 - (self.Cronometro5 * CDR / 100)

            Clock.unschedule(self.gf5)
            Clock.schedule_interval(self.gf5, 1)
            self.ult5.text = str(f'{self.Cronometro5:.0f}')

    def gf5(self, dt):

        self.Cronometro5 = self.Cronometro5 - 1
        self.ult5.text = str(f'{self.Cronometro5:.0f}')
        print(int(self.Cronometro5))
        if self.Cronometro5 < 1:
            self.ult5.background_color = 1, 1, 1, 0
            self.ult5.text = ''
            Clock.unschedule(self.gf5)

    def timespell1(self):
        if self.spelln1.background_color == [1, 1, 1, 0.5]:
            self.spelln1.background_color = 1, 1, 1, 0
            self.spelln1.text = ''
            Clock.unschedule(self.spell1cd)
        else:
            self.spelln1.background_color = 1, 1, 1, 0.5

            print(self.spelln1.background_color)

            self.feiticos1 = self.manager.men.champs[2][0][0]
            if self.feiticos1 == 0:
                if self.manager.prof.champ1.text == 'Lv:6':
                    self.feiticos1 = 370
                elif self.manager.prof.champ1.text == 'Lv:11':
                    self.feiticos1 = 314
                else:
                    self.feiticos1 = 240

            Clock.unschedule(self.spell1cd)
            Clock.schedule_interval(self.spell1cd, 1)
            self.spelln1.text = str(f'{self.feiticos1:.0f}')

    def spell1cd(self, dt):

        self.feiticos1 = self.feiticos1 - 1
        self.spelln1.text = str(f'{self.feiticos1:.0f}')
        print(int(self.feiticos1))
        if self.feiticos1 < 1:
            self.spelln1.background_color = 1, 1, 1, 0
            self.spelln1.text = ''
            Clock.unschedule(self.spell1cd)

    def timespell2(self):
        if self.spelln2.background_color == [1, 1, 1, 0.5]:
            self.spelln2.background_color = 1, 1, 1, 0
            self.spelln2.text = ''
            Clock.unschedule(self.spell2cd)
        else:
            self.spelln2.background_color = 1, 1, 1, 0.5

            print(self.spelln2.background_color)

            self.feiticos2 = self.manager.men.champs[2][1][0]
            if self.feiticos2 == 0:
                if self.manager.prof.champ1.text == 'Lv:6':
                    self.feiticos2 = 370
                elif self.manager.prof.champ1.text == 'Lv:11':
                    self.feiticos2 = 314
                else:
                    self.feiticos2 = 240

            Clock.unschedule(self.spell2cd)
            Clock.schedule_interval(self.spell2cd, 1)
            self.spelln2.text = str(f'{self.feiticos2:.0f}')

    def spell2cd(self, dt):

        self.feiticos2 = self.feiticos2 - 1
        self.spelln2.text = str(f'{self.feiticos2:.0f}')
        print(int(self.feiticos2))
        if self.feiticos2 < 1:
            self.spelln2.background_color = 1, 1, 1, 0
            self.spelln2.text = ''
            Clock.unschedule(self.spell2cd)

    def timespell3(self):
        if self.spelln3.background_color == [1, 1, 1, 0.5]:
            self.spelln3.background_color = 1, 1, 1, 0
            self.spelln3.text = ''
            Clock.unschedule(self.spell3cd)
        else:
            self.spelln3.background_color = 1, 1, 1, 0.5

            print(self.spelln3.background_color)

            self.feiticos3 = self.manager.men.champs[2][2][0]
            if self.feiticos3 == 0:
                if self.manager.prof.champ2.text == 'Lv:6':
                    self.feiticos3 = 370
                elif self.manager.prof.champ2.text == 'Lv:11':
                    self.feiticos3 = 314
                else:
                    self.feiticos3 = 240

            Clock.unschedule(self.spell3cd)
            Clock.schedule_interval(self.spell3cd, 1)
            self.spelln3.text = str(f'{self.feiticos3:.0f}')

    def spell3cd(self, dt):

        self.feiticos3 = self.feiticos3 - 1
        self.spelln3.text = str(f'{self.feiticos3:.0f}')
        print(int(self.feiticos3))
        if self.feiticos3 < 1:
            self.spelln3.background_color = 1, 1, 1, 0
            self.spelln3.text = ''
            Clock.unschedule(self.spell3cd)

    def timespell4(self):
        if self.spelln4.background_color == [1, 1, 1, 0.5]:
            self.spelln4.background_color = 1, 1, 1, 0
            self.spelln4.text = ''
            Clock.unschedule(self.spell4cd)
        else:
            self.spelln4.background_color = 1, 1, 1, 0.5

            print(self.spelln4.background_color)

            self.feiticos4 = self.manager.men.champs[2][3][0]
            if self.feiticos4 == 0:
                if self.manager.prof.champ2.text == 'Lv:6':
                    self.feiticos4 = 370
                elif self.manager.prof.champ2.text == 'Lv:11':
                    self.feiticos4 = 314
                else:
                    self.feiticos4 = 240

            Clock.unschedule(self.spell4cd)
            Clock.schedule_interval(self.spell4cd, 1)
            self.spelln4.text = str(f'{self.feiticos4:.0f}')

    def spell4cd(self, dt):

        self.feiticos4 = self.feiticos4 - 1
        self.spelln4.text = str(f'{self.feiticos4:.0f}')
        print(int(self.feiticos4))
        if self.feiticos4 < 1:
            self.spelln4.background_color = 1, 1, 1, 0
            self.spelln4.text = ''
            Clock.unschedule(self.spell4cd)

    def timespell5(self):
        if self.spelln5.background_color == [1, 1, 1, 0.5]:
            self.spelln5.background_color = 1, 1, 1, 0
            self.spelln5.text = ''
            Clock.unschedule(self.spell5cd)
        else:
            self.spelln5.background_color = 1, 1, 1, 0.5

            print(self.spelln5.background_color)

            self.feiticos5 = self.manager.men.champs[2][4][0]
            if self.feiticos5 == 0:
                if self.manager.prof.champ3.text == 'Lv:6':
                    self.feiticos5 = 370
                elif self.manager.prof.champ3.text == 'Lv:11':
                    self.feiticos5 = 314
                else:
                    self.feiticos5 = 240

            Clock.unschedule(self.spell5cd)
            Clock.schedule_interval(self.spell5cd, 1)
            self.spelln5.text = str(f'{self.feiticos5:.0f}')

    def spell5cd(self, dt):

        self.feiticos5 = self.feiticos5 - 1
        self.spelln5.text = str(f'{self.feiticos5:.0f}')
        print(int(self.feiticos5))
        if self.feiticos5 < 1:
            self.spelln5.background_color = 1, 1, 1, 0
            self.spelln5.text = ''
            Clock.unschedule(self.spell5cd)

    def timespell6(self):
        if self.spelln6.background_color == [1, 1, 1, 0.5]:
            self.spelln6.background_color = 1, 1, 1, 0
            self.spelln6.text = ''
            Clock.unschedule(self.spell6cd)
        else:
            self.spelln6.background_color = 1, 1, 1, 0.5

            print(self.spelln6.background_color)

            self.feiticos6 = self.manager.men.champs[2][5][0]
            if self.feiticos6 == 0:
                if self.manager.prof.champ3.text == 'Lv:6':
                    self.feiticos6 = 370
                elif self.manager.prof.champ3.text == 'Lv:11':
                    self.feiticos6 = 314
                else:
                    self.feiticos6 = 240

            Clock.unschedule(self.spell6cd)
            Clock.schedule_interval(self.spell6cd, 1)
            self.spelln6.text = str(f'{self.feiticos6:.0f}')

    def spell6cd(self, dt):

        self.feiticos6 = self.feiticos6 - 1
        self.spelln6.text = str(f'{self.feiticos6:.0f}')
        print(int(self.feiticos6))
        if self.feiticos6 < 1:
            self.spelln6.background_color = 1, 1, 1, 0
            self.spelln6.text = ''
            Clock.unschedule(self.spell6cd)

    def timespell7(self):
        if self.spelln7.background_color == [1, 1, 1, 0.5]:
            self.spelln7.background_color = 1, 1, 1, 0
            self.spelln7.text = ''
            Clock.unschedule(self.spell7cd)
        else:
            self.spelln7.background_color = 1, 1, 1, 0.5

            print(self.spelln7.background_color)

            self.feiticos7 = self.manager.men.champs[2][6][0]
            if self.feiticos7 == 0:
                if self.manager.prof.champ4.text == 'Lv:6':
                    self.feiticos7 = 370
                elif self.manager.prof.champ4.text == 'Lv:11':
                    self.feiticos7 = 314
                else:
                    self.feiticos7 = 240

            Clock.unschedule(self.spell7cd)
            Clock.schedule_interval(self.spell7cd, 1)
            self.spelln7.text = str(f'{self.feiticos7:.0f}')

    def spell7cd(self, dt):

        self.feiticos7 = self.feiticos7 - 1
        self.spelln7.text = str(f'{self.feiticos7:.0f}')
        print(int(self.feiticos7))
        if self.feiticos7 < 1:
            self.spelln7.background_color = 1, 1, 1, 0
            self.spelln7.text = ''
            Clock.unschedule(self.spell7cd)

    def timespell8(self):
        if self.spelln8.background_color == [1, 1, 1, 0.5]:
            self.spelln8.background_color = 1, 1, 1, 0
            self.spelln8.text = ''
            Clock.unschedule(self.spell8cd)
        else:
            self.spelln8.background_color = 1, 1, 1, 0.5

            print(self.spelln8.background_color)

            self.feiticos8 = self.manager.men.champs[2][7][0]
            if self.feiticos8 == 0:
                if self.manager.prof.champ4.text == 'Lv:6':
                    self.feiticos8 = 370
                elif self.manager.prof.champ4.text == 'Lv:11':
                    self.feiticos8 = 314
                else:
                    self.feiticos8 = 240

            Clock.unschedule(self.spell8cd)
            Clock.schedule_interval(self.spell8cd, 1)
            self.spelln8.text = str(f'{self.feiticos8:.0f}')

    def spell8cd(self, dt):

        self.feiticos8 = self.feiticos8 - 1
        self.spelln8.text = str(f'{self.feiticos8:.0f}')
        print(int(self.feiticos8))
        if self.feiticos8 < 1:
            self.spelln8.background_color = 1, 1, 1, 0
            self.spelln8.text = ''
            Clock.unschedule(self.spell8cd)

    def timespell9(self):
        if self.spelln9.background_color == [1, 1, 1, 0.5]:
            self.spelln9.background_color = 1, 1, 1, 0
            self.spelln9.text = ''
            Clock.unschedule(self.spell9cd)
        else:
            self.spelln9.background_color = 1, 1, 1, 0.5

            print(self.spelln9.background_color)

            self.feiticos9 = self.manager.men.champs[2][8][0]
            if self.feiticos9 == 0:
                if self.manager.prof.champ5.text == 'Lv:6':
                    self.feiticos9 = 370
                elif self.manager.prof.champ5.text == 'Lv:11':
                    self.feiticos9 = 314
                else:
                    self.feiticos9 = 240

            Clock.unschedule(self.spell9cd)
            Clock.schedule_interval(self.spell9cd, 1)
            self.spelln9.text = str(f'{self.feiticos9:.0f}')

    def spell9cd(self, dt):

        self.feiticos9 = self.feiticos9 - 1
        self.spelln9.text = str(f'{self.feiticos9:.0f}')
        print(int(self.feiticos9))
        if self.feiticos9 < 1:
            self.spelln9.background_color = 1, 1, 1, 0
            self.spelln9.text = ''
            Clock.unschedule(self.spell9cd)

    def timespell10(self):
        if self.spelln10.background_color == [1, 1, 1, 0.5]:
            self.spelln10.background_color = 1, 1, 1, 0
            self.spelln10.text = ''
            Clock.unschedule(self.spell10cd)
        else:
            self.spelln10.background_color = 1, 1, 1, 0.5

            print(self.spelln10.background_color)

            self.feiticos10 = self.manager.men.champs[2][9][0]
            if self.feiticos10 == 0:
                if self.manager.prof.champ5.text == 'Lv:6':
                    self.feiticos10 = 370
                elif self.manager.prof.champ5.text == 'Lv:11':
                    self.feiticos10 = 314
                else:
                    self.feiticos10 = 240

            Clock.unschedule(self.spell10cd)
            Clock.schedule_interval(self.spell10cd, 1)
            self.spelln10.text = str(f'{self.feiticos10:.0f}')

    def spell10cd(self, dt):

        self.feiticos10 = self.feiticos10 - 1
        self.spelln10.text = str(f'{self.feiticos10:.0f}')
        print(int(self.feiticos10))
        if self.feiticos10 < 1:
            self.spelln10.background_color = 1, 1, 1, 0
            self.spelln10.text = ''
            Clock.unschedule(self.spell10cd)

    def trade(self):
        print(self.manager.men.sear8h.text)
        print(self.manager.men.champs)

    def tradwwwe(self):
        global versao
        self.avatar1.source = f"http://ddragon.leagueoflegends.com/cdn/{versao}/img/champion/{self.manager.men.champs[0][0]}.png"
        self.avatar2.source = f"http://ddragon.leagueoflegends.com/cdn/{versao}/img/champion/{self.manager.men.champs[0][1]}.png"
        self.avatar3.source = f"http://ddragon.leagueoflegends.com/cdn/{versao}/img/champion/{self.manager.men.champs[0][2]}.png"
        self.avatar4.source = f"http://ddragon.leagueoflegends.com/cdn/{versao}/img/champion/{self.manager.men.champs[0][3]}.png"
        self.avatar5.source = f"http://ddragon.leagueoflegends.com/cdn/{versao}/img/champion/{self.manager.men.champs[0][4]}.png"
        self.ul1.source = f"http://ddragon.leagueoflegends.com/cdn/{versao}/img/spell/{self.ultimatesss[0]}"
        self.ul2.source = f"http://ddragon.leagueoflegends.com/cdn/{versao}/img/spell/{self.ultimatesss[1]}"
        self.ul3.source = f"http://ddragon.leagueoflegends.com/cdn/{versao}/img/spell/{self.ultimatesss[2]}"
        self.ul4.source = f"http://ddragon.leagueoflegends.com/cdn/{versao}/img/spell/{self.ultimatesss[3]}"
        self.ul5.source = f"http://ddragon.leagueoflegends.com/cdn/{versao}/img/spell/{self.ultimatesss[4]}"
        self.sp1_1.source = f"http://ddragon.leagueoflegends.com/cdn/{versao}/img/spell/{self.manager.men.champs[1][0]}.png"
        self.sp1_2.source = f"http://ddragon.leagueoflegends.com/cdn/{versao}/img/spell/{self.manager.men.champs[1][1]}.png"
        self.sp2_1.source = f"http://ddragon.leagueoflegends.com/cdn/{versao}/img/spell/{self.manager.men.champs[1][2]}.png"
        self.sp2_2.source = f"http://ddragon.leagueoflegends.com/cdn/{versao}/img/spell/{self.manager.men.champs[1][3]}.png"
        self.sp3_1.source = f"http://ddragon.leagueoflegends.com/cdn/{versao}/img/spell/{self.manager.men.champs[1][4]}.png"
        self.sp3_2.source = f"http://ddragon.leagueoflegends.com/cdn/{versao}/img/spell/{self.manager.men.champs[1][5]}.png"
        self.sp4_1.source = f"http://ddragon.leagueoflegends.com/cdn/{versao}/img/spell/{self.manager.men.champs[1][6]}.png"
        self.sp4_2.source = f"http://ddragon.leagueoflegends.com/cdn/{versao}/img/spell/{self.manager.men.champs[1][7]}.png"
        self.sp5_1.source = f"http://ddragon.leagueoflegends.com/cdn/{versao}/img/spell/{self.manager.men.champs[1][8]}.png"
        self.sp5_2.source = f"http://ddragon.leagueoflegends.com/cdn/{versao}/img/spell/{self.manager.men.champs[1][9]}.png"

    def startult(self):
        ult = Thread(target=self.ultscampeaoes)
        ult.start()

    def ultscampeaoes(self):
        champs = self.manager.men.champs[0]
        self.ultimatesss = []
        for quant in range(len(champs)):
            global versao
            URLcampeao = requests.get(
                f'http://ddragon.leagueoflegends.com/cdn/{versao}/data/en_US/champion/{champs[quant]}.json').json()
            ultimate = URLcampeao['data'][champs[quant]]['spells'][3]['image']['full']
            self.ultimatesss.append(ultimate)
        print(self.ultimatesss)

        self.Ultimatecds = []
        for quantidade in range(0, 5):
            URLcampeao = requests.get(
                f'http://ddragon.leagueoflegends.com/cdn/{versao}/data/en_US/champion/{champs[quantidade]}.json').json()
            ultimate = URLcampeao['data'][champs[quantidade]]['spells'][3]['cooldown']
            self.Ultimatecds.append(ultimate)
        print(self.Ultimatecds)

    pass


# Create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(ProfileScreen(name='profile'))


class MDApp(MDApp):
    def build(self):
        self.screen = Builder.load_string(screen_helper)

        menu_items = [{"icon": "git", "text": f"Lv:{i}"} for i in range(6, 17, 5)]
        self.menu = MDDropdownMenu(
            caller=self.screen.prof.champ1,
            items=menu_items,
            position="auto",
            callback=self.set_item,
            width_mult=4, )
        menu_cdr = [{"icon": "git", "text": f"Cdr:{i}"} for i in range(0, 41, 10)]
        self.menucdr = MDDropdownMenu(
            caller=self.screen.prof.champ1cd,
            items=menu_cdr,
            position="auto",
            callback=self.set_itemcdr,
            width_mult=4, )

        menu_items2 = [{"icon": "git", "text": f"Lv:{i}"} for i in range(6, 17, 5)]
        self.menu2 = MDDropdownMenu(
            caller=self.screen.prof.champ2,
            items=menu_items2,
            position="auto",
            callback=self.set_item2,
            width_mult=4, )
        menu_cdr2 = [{"icon": "git", "text": f"Cdr:{i}"} for i in range(0, 41, 10)]
        self.menucdr2 = MDDropdownMenu(
            caller=self.screen.prof.champ2cd,
            items=menu_cdr2,
            position="auto",
            callback=self.set_itemcdr2,
            width_mult=4, )

        menu_items3 = [{"icon": "git", "text": f"Lv:{i}"} for i in range(6, 17, 5)]
        self.menu3 = MDDropdownMenu(
            caller=self.screen.prof.champ3,
            items=menu_items3,
            position="auto",
            callback=self.set_item3,
            width_mult=4, )
        menu_cdr3 = [{"icon": "git", "text": f"Cdr:{i}"} for i in range(0, 41, 10)]
        self.menucdr3 = MDDropdownMenu(
            caller=self.screen.prof.champ3cd,
            items=menu_cdr3,
            position="auto",
            callback=self.set_itemcdr3,
            width_mult=4, )

        menu_items4 = [{"icon": "git", "text": f"Lv:{i}"} for i in range(6, 17, 5)]
        self.menu4 = MDDropdownMenu(
            caller=self.screen.prof.champ4,
            items=menu_items4,
            position="auto",
            callback=self.set_item4,
            width_mult=4, )
        menu_cdr4 = [{"icon": "git", "text": f"Cdr:{i}"} for i in range(0, 41, 10)]
        self.menucdr4 = MDDropdownMenu(
            caller=self.screen.prof.champ4cd,
            items=menu_cdr4,
            position="auto",
            callback=self.set_itemcdr4,
            width_mult=4, )

        menu_items5 = [{"icon": "git", "text": f"Lv:{i}"} for i in range(6, 17, 5)]
        self.menu5 = MDDropdownMenu(
            caller=self.screen.prof.champ5,
            items=menu_items5,
            position="auto",
            callback=self.set_item5,
            width_mult=4, )
        menu_cdr5 = [{"icon": "git", "text": f"Cdr:{i}"} for i in range(0, 41, 10)]
        self.menucdr5 = MDDropdownMenu(
            caller=self.screen.prof.champ5cd,
            items=menu_cdr5,
            position="auto",
            callback=self.set_itemcdr5,
            width_mult=4, )

        return self.screen

    def set_item(self, instance):
        self.screen.prof.champ1.set_item(instance.text)
        self.screen.prof.champ1.text = instance.text
        self.menu.dismiss()

    def set_itemcdr(self, instance):
        self.screen.prof.champ1cd.set_item(instance.text)
        self.screen.prof.champ1cd.text = instance.text
        self.menucdr.dismiss()

    def set_item2(self, instance):
        self.screen.prof.champ2.set_item(instance.text)
        self.screen.prof.champ2.text = instance.text
        self.menu2.dismiss()

    def set_itemcdr2(self, instance):
        self.screen.prof.champ2cd.set_item(instance.text)
        self.screen.prof.champ2cd.text = instance.text
        self.menucdr2.dismiss()

    def set_item3(self, instance):
        self.screen.prof.champ3.set_item(instance.text)
        self.screen.prof.champ3.text = instance.text
        self.menu3.dismiss()

    def set_itemcdr3(self, instance):
        self.screen.prof.champ3cd.set_item(instance.text)
        self.screen.prof.champ3cd.text = instance.text
        self.menucdr3.dismiss()

    def set_item4(self, instance):
        self.screen.prof.champ4.set_item(instance.text)
        self.screen.prof.champ4.text = instance.text
        self.menu4.dismiss()

    def set_itemcdr4(self, instance):
        self.screen.prof.champ4cd.set_item(instance.text)
        self.screen.prof.champ4cd.text = instance.text
        self.menucdr4.dismiss()

    def set_item5(self, instance):
        self.screen.prof.champ5.set_item(instance.text)
        self.screen.prof.champ5.text = instance.text
        self.menu5.dismiss()

    def set_itemcdr5(self, instance):
        self.screen.prof.champ5cd.set_item(instance.text)
        self.screen.prof.champ5cd.text = instance.text
        self.menucdr5.dismiss()


MDApp().run()
