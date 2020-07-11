from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen, CardTransition
from kivy.properties import ObjectProperty, NumericProperty, ReferenceListProperty, ListProperty, BooleanProperty, DictProperty
from kivy.uix.widget import Widget
from kivy.vector import Vector
from kivy.graphics import Rotate, Rectangle, Ellipse, Color
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.progressbar import ProgressBar
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.recycleview import RecycleView
from kivy.uix.settings import SettingsWithSidebar
from kivy.graphics.context_instructions import PopMatrix, PushMatrix

Builder.load_string('''
<PongBall>:
    size: 50,50
    canvas:
        Color:
            rgba: 0,0,1,1
        Ellipse:
            pos: self.x - self.size[0]/2, self.y - self.size[1]/2
            size: self.size

<PongGame>:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
           
    ball: pong_ball
    object: Object
    canvas:
        Color: 
            rgba: 1,0,0,1
        Rectangle:
            pos: 80,335
            size: 10, 150
        Color: 
            rgba: 0,1,0,1
        Rectangle:
            pos: 470,200
            size: 200,10
        
    FloatLayout:
        Button:
            pos_hint:{"x":2.5,"y":0}
            size_hint: 3, 0.7
            text:"Throw"
            background_color: 223,1,190,1
            on_release:
                root.start()
        Button:
            pos_hint:{"x":0.5,"y":0}
            size_hint: 2, 0.5
            text:"<<Home"
            background_color: 2,1,190,1
            on_release:
                root.home()
        Button:
            pos_hint:{"x":5.5,"y":0}
            size_hint: 2, 0.5
            text:"Stages>>"
            background_color: 2,1,190,1
            on_release:
                root.stage()
        Button:
            pos_hint:{'x':7.3, 'y':5.3}
            size_hint: 0.5,0.5
            text:'Home'
            on_release:
                root.home()
    
    PongBall:
        id: pong_ball
        center: self.center
        
    Object:
        id: Object
        center: self.rotate_origin

<Stage_2>:
    ball: pong_ball
    object2: Object2
    object3: Object3
    canvas:
        Color: 
            rgba: 1,0,0,1
        Rectangle:
            pos: 80,370
            size: 10, 150
        Color: 
            rgba: 0,1,0,1
        Rectangle:
            pos: 80,190
            size: 10,150
    FloatLayout:
        Button:
            pos_hint:{"x":2.5,"y":0}
            size_hint: 3, 0.7
            text:"Throw"
            background_color: 2,1,190,1
            on_release:
                root.start()
        Button:
            pos_hint:{"x":0.5,"y":0}
            size_hint: 2, 0.5
            text:"<<Home"
            background_color: 2,1,190,1
            on_release:
                root.home()
        Button:
            pos_hint:{"x":5.5,"y":0}
            size_hint: 2, 0.5
            text:"Stages>>"
            background_color: 2,1,190,1
            on_release:
                root.stage()
        Button:
            pos_hint:{'x':7.3, 'y':5.3}
            size_hint: 0.5,0.5
            text:'restart'
            on_release:
                root.serve_ball()
    
    PongBall:
        id: pong_ball
        center: self.center
    
    Object3:
        id: Object3
        center: self.rotate_origin
            
    Object2:
        id: Object2
        center: self.rotate_origin     
                   
<Stage_3>:
    ball: pong_ball
    object5: Object5
    object4: Object4
    object6: Object6
    canvas:
        Color: 
            rgba: 1,0,0,1
        Rectangle:
            pos: 80,370
            size: 10, 150
        Color: 
            rgba: 0,1,0,1
        Rectangle:
            pos: 470,500
            size: 200,10
    FloatLayout:
        Button:
            pos_hint:{"x":2.5,"y":0}
            size_hint: 3, 0.7
            text:"Throw"
            background_color: 2,1,190,1
            on_release:
                root.start()
        Button:
            pos_hint:{"x":0.5,"y":0}
            size_hint: 2, 0.5
            text:"<<Home"
            background_color: 2,1,190,1
            on_release:
                root.home()
        Button:
            pos_hint:{"x":5.5,"y":0}
            size_hint: 2, 0.5
            text:"Stages>>"
            background_color: 2,1,190,1
            on_release:
                root.stage()
        Button:
            pos_hint:{'x':7.3, 'y':5.3}
            size_hint: 0.5,0.5
            text:'restart'
            on_release:
                root.serve_ball()
    
    PongBall:
        id: pong_ball
        center: self.center
    
    Object4:
        id: Object4
        center: self.rotate_origin
            
    Object5:
        id: Object5
        center: self.rotate_origin 
        
    Object6:
        id: Object6
        center: self.rotate_origin

<Stage_4>:
    ball: pong_ball
    object7: Object7
    object8: Object8
    object9: Object9
    canvas:
        Color: 
            rgba: 1,0,0,1
        Rectangle:
            pos: 80,370
            size: 10, 150
        Color: 
            rgba: 0,1,0,1
        Rectangle:
            pos: 300,500
            size: 200,10
    FloatLayout:
        Button:
            pos_hint:{"x":2.5,"y":0}
            size_hint: 3, 0.7
            text:"Throw"
            background_color: 2,1,190,1
            on_release:
                root.start()
        Button:
            pos_hint:{"x":0.5,"y":0}
            size_hint: 2, 0.5
            text:"<<Home"
            background_color: 2,1,190,1
            on_release:
                root.home()
        Button:
            pos_hint:{"x":5.5,"y":0}
            size_hint: 2, 0.5
            text:"Stages>>"
            background_color: 2,1,190,1
            on_release:
                root.stage()
        Button:
            pos_hint:{'x':7.3, 'y':5.3}
            size_hint: 0.5,0.5
            text:'restart'
            on_release:
                root.serve_ball()
    
    PongBall:
        id: pong_ball
        center: self.center
    
    Object7:
        id: Object7
        center: self.rotate_origin
            
    Object8:
        id: Object8
        center: self.rotate_origin 
        
    Object9:
        id: Object9
        center: self.rotate_origin  

<Stage_5>:
    ball: pong_ball
    object10: Object10
    object11: Object11
    object12: Object12
    object13: Object13
    canvas:
        Color: 
            rgba: 1,0,0,1
        Rectangle:
            pos: 80,370
            size: 10, 150
        Color: 
            rgba: 0,1,0,1
        Rectangle:
            pos: 320,520
            size: 200,10
    FloatLayout:
        Button:
            pos_hint:{"x":2.5,"y":0}
            size_hint: 3, 0.7
            text:"Throw"
            background_color: 2,1,190,1
            on_release:
                root.start()
        Button:
            pos_hint:{"x":0.5,"y":0}
            size_hint: 2, 0.5
            text:"<<Home"
            background_color: 2,1,190,1
            on_release:
                root.home()
        Button:
            pos_hint:{"x":5.5,"y":0}
            size_hint: 2, 0.5
            text:"Stages>>"
            background_color: 2,1,190,1
            on_release:
                root.stage()
        Button:
            pos_hint:{'x':7.3, 'y':5.3}
            size_hint: 0.5,0.5
            text:'restart'
            on_release:
                root.serve_ball()
    
    PongBall:
        id: pong_ball
        center: self.center
    
    Object10:
        id: Object10
        center: self.rotate_origin
            
    Object11:
        id: Object11
        center: self.rotate_origin 
        
    Object12:
        id: Object12
        center: self.rotate_origin 
    
    Object13:
        id: Object13
        center: self.rotate_origin

<Stage_6>:
    ball: pong_ball
    object14: Object14
    object15: Object15
    object16: Object16
    object17: Object17
    canvas:
        Color: 
            rgba: 1,0,0,1
        Rectangle:
            pos: 80,390
            size: 10, 130
        Color: 
            rgba: 0,1,0,1
        Rectangle:
            pos: 700,100
            size: 10,120
    FloatLayout:
        Button:
            pos_hint:{"x":2.5,"y":0}
            size_hint: 3, 0.7
            text:"Throw"
            background_color: 2,1,190,1
            on_release:
                root.start()
        Button:
            pos_hint:{"x":0.5,"y":0}
            size_hint: 2, 0.5
            text:"<<Home"
            background_color: 2,1,190,1
            on_release:
                root.home()
        Button:
            pos_hint:{"x":5.5,"y":0}
            size_hint: 2, 0.5
            text:"Stages>>"
            background_color: 2,1,190,1
            on_release:
                root.stage()
        Button:
            pos_hint:{'x':7.3, 'y':5.3}
            size_hint: 0.5,0.5
            text:'restart'
            on_release:
                root.serve_ball()
    
    PongBall:
        id: pong_ball
        center: self.center
    
    Object14:
        id: Object14
        center: self.rotate_origin
            
    Object15:
        id: Object15
        center: self.rotate_origin 
        
    Object16:
        id: Object16
        center: self.rotate_origin 
    
    Object17:
        id: Object17
        center: self.rotate_origin

<Stage_7>:
    ball: pong_ball
    object18: Object18
    object19: Object19
    canvas:
        Color: 
            rgba: 1,0,0,1
        Rectangle:
            pos: 80,370
            size: 10, 150
        Color: 
            rgba: 0,1,0,1
        Rectangle:
            pos: 700,340
            size: 10,150
    FloatLayout:
        Button:
            pos_hint:{"x":2.5,"y":0}
            size_hint: 3, 0.7
            text:"Throw"
            background_color: 2,1,190,1
            on_release:
                root.start()
        Button:
            pos_hint:{"x":0.5,"y":0}
            size_hint: 2, 0.5
            text:"<<Home"
            background_color: 2,1,190,1
            on_release:
                root.home()
        Button:
            pos_hint:{"x":5.5,"y":0}
            size_hint: 2, 0.5
            text:"Stages>>"
            background_color: 2,1,190,1
            on_release:
                root.stage()
        Button:
            pos_hint:{'x':7.3, 'y':5.3}
            size_hint: 0.5,0.5
            text:'restart'
            on_release:
                root.serve_ball()
    
    PongBall:
        id: pong_ball
        center: self.center
    
    Object18:
        id: Object18
        center: self.rotate_origin
            
    Object19:
        id: Object19
        center: self.rotate_origin   
   
<P>:
    
    Label:
        text: "You made it!!"
        size_hint: 0.6, 0.2
        pos_hint: {"x":0.2, "top":1}
    
    Button:
        text: "Next"
        size_hint: 0.8, 0.2
        pos_hint: {"x":0.1, "y":0.1}
        background_color: 0,20,1,1
        on_release: 
            root.manager.transition.direction = "up"
            root.current = "stage"
   
<loss>:
    
    
<ManagerButton@Button>:
    manager: None
    pos_hint: {'x': 0,'y':0}
    name_screen: ""
    on_release:
        self.manager.current = self.name_screen

<ExampleRV>:
    viewclass: 'ManagerButton'

    RecycleBoxLayout:
        size_hint_y: None
        size_hint_x: None
        pos_hint: {'x': 0,'y': 0}
        height: self.minimum_height
        width: self.minimum_width
        orientation: 'horizontal'
    
<Manager>:
    id: screen_manager
    
    Screen:
        name:"P"
        canvas.before:
            Color:
                rgba: 1,0,0,1
            Rectangle:
                pos: self.pos
                size: self.pos
                
        FloatLayout:
            Button:
                pos_hint:{"x":0.2,"y":0.35}
                size_hint: 0.6, 0.2
                font_size: (root.width**2 + root.height**2) / 13**4
                text: "Settings"
                on_release:app.open_settings()

            Button:
                background_normal: 'Home.png'
                background_down: 'Home.png'
                border: 30,30,30,30
                pos_hint:{"x":0.2,"y":0.05}
                size_hint: 0.6, 0.2
                font_size: (root.width**2 + root.height**2) / 13**4
                text: "Play \U0001F918"
                background_color: 1,1,1,1
                on_release:
                    root.transition.direction = "up"        
                    root.current = "recycleview";game.serve_ball();s2.serve_ball();s3.serve_ball(),s4.serve_ball(), s5.serve_ball(), s6.serve_ball(), s7.serve_ball()
                    
    Screen:
        name: 'Loading'
        MyWidget:
            id: loading                
                    
    Screen:
        name: "stage"
        
        Label:
            pos_hint:{"x": 0.04, "y":0.3}
            size_hint:1.0, 1.0
            text: "Stage>> "
        
        Button:
            pos_hint:{"x":0,"y":0.05}
            size_hint: 0.2, 0.2
            text:"1"
            background_color: 153,1,190,1
            on_release:
                root.transition.direction = "right"
                root.current= "Game";game.serve_ball()
        Button:
            pos_hint:{"x":0.2,"y":0.05}
            size_hint: 0.2, 0.2
            text:"2"
            on_release:
                root.transition.direction = "up"
                root.current = "stage2";s2.serve_ball()
        Button:
            pos_hint:{"x":0.4,"y":0.05}
            size_hint: 0.2, 0.2
            text:"3"
            on_release:
                root.manager.transition.direction = "up"
                root.nextpage()
        Button:
            pos_hint:{"x":0.6,"y":0.05}
            size_hint: 0.2, 0.2
            text:"4"
            on_release:
                root.manager.transition.direction = "up"
                root.nextpage()
        Button:
            pos_hint:{"x":0.8,"y":0.05}
            size_hint: 0.2, 0.2
            text:"5"
            on_release:
                root.manager.transition.direction = "down"
                root.nextpage()

    Screen:         
        name: 'Game'
        PongGame:   
            id: game
            
    Screen:
        name: 'stage comp'
        Label:
            text: "You made it!!"
            size_hint: 0.6, 0.2
            pos_hint: {"x":0.2, "top":1}
    
        Button:
            text: "Next"
            size_hint: 0.8, 0.2
            pos_hint: {"x":0.1, "y":0.1}
            background_color: 0,20,1,1
            on_release: 
                root.transition.direction = "up"
                root.current = "recycleview"
    
    Screen:
        name: 'loss'
        Label:
            text: "That was not the supposed one!!"
            size_hint: 0.6, 0.2
            pos_hint: {"x":0.2, "top":1}
    
        Button:
            text: "Retry"
            size_hint: 0.8, 0.2
            pos_hint: {"x":0.1, "y":0.1}
            background_color: 0,20,1,1
            on_release: 
                root.transition.direction = "up";game.serve_ball()
                root.current = "recycleview"
                
    Screen:
        name: 'stage2'
        Stage_2:
            id:s2
            
    Screen:
        name: 'recycleview'
        ExampleRV:
            data: [ {"text": str(i), "manager": root, "name_screen": name} for i, name in enumerate(self.screen_names, 1) ]
    
    Screen:
        name:'stage3'
        Stage_3:
            id:s3
    
    Screen:
        name:'stage4'
        Stage_4:
            id:s4
    Screen: 
        name:'stage5'
        Stage_5:
            id:s5
    Screen:
        name:'stage6'
        Stage_6:
            id:s6
    Screen:
        name:'stage7'
        Stage_7:
            id:s7

''')

class MyWidget(Widget):
    progress_bar = ObjectProperty()

    def __init__(self, **kwa):
        super(MyWidget, self).__init__(**kwa)

        self.progress_bar = ProgressBar()
        self.popup = Popup(
            title='Loading...',
            content=self.progress_bar
        )
        self.popup.bind(on_open=self.puopen)
       # self.add_widget(Button(text='Download', on_release=self.pop))

    # the function which works when you click the button
    def pop(self, instance):
        self.progress_bar.value = 1
        self.popup.open()

    # To continuesly increasing the value of pb.
    def next(self, dt):
        if self.progress_bar.value >= 100:
            #sm.current = "stage"
            self.popup.dismiss()
            #return False
        self.progress_bar.value += 1

    def puopen(self, instance):
        Clock.schedule_interval(self.next, 1 / 50)
        sm.current = "stage"


class ExampleRV(RecycleView):
    screen_names = ListProperty(["Game", "stage2","stage3","stage4","stage5","stage6","stage7","","","","","","",""])


class Object(Widget):
    def __init__(self, *args, **kwargs):
        Widget.__init__(self, *args, **kwargs)
        self.rect_pos_x = 500
        self.rect_pos_y = 420
        self.rect_pos = self.rect_pos_x, self.rect_pos_y
        self.rect_width = 200
        self.rect_height = 15
        self.rect_size = self.rect_width, self.rect_height
        self.rotate_origin_x = self.rect_pos_x + self.rect_width / 2
        self.rotate_origin_y = self.rect_pos_y + self.rect_height / 2
        self.rotate_origin = self.rotate_origin_x, self.rotate_origin_y
        self.angle = 225
        self.rot_x_dir = Vector(1, 0).rotate(self.angle)
        self.rot_y_dir = Vector(0, 1).rotate(self.angle)
        print('rect 1')
        with self.canvas:
            Rotate(origin=self.rotate_origin, angle=self.angle)
            Color(rgb=(0,197,68))
            Rectangle(pos=self.rect_pos, size=self.rect_size)

    def rotate(self):
        self.canvas.clear()
        self.angle += 90
        if (self.angle > 315):
            self.angle = 225
        self.rot_x_dir = Vector(1, 0).rotate(self.angle)
        self.rot_y_dir = Vector(0, 1).rotate(self.angle)
        with self.canvas:
            PushMatrix()
            self.rot = Rotate(origin=self.rotate_origin, angle=self.angle)
            Color(rgb=(0, 255, 100))
            Rectangle(pos=self.rect_pos, size=self.rect_size)
            PopMatrix()

    def deflect_ball(self, ball):
        if self.collide_ball(ball):
            if ball.collided[self] is False:
                vx, vy = ball.velocity
                if self.angle == 135:
                    ball.velocity = Vector(-vx, vy).rotate(90)
                if self.angle == 225:
                    ball.velocity = Vector(-vx, vy).rotate(270)
                if self.angle == 315:
                    ball.velocity = Vector(-vx, vy).rotate(90)
                print(ball.collided)
                ball.collided[self] = True

        else:
            ball.collided[self] = False


    def on_touch_up(self, touch):
        if self.collide_point(*touch.pos):
            self.rotate()
            print(self.angle)

    def collide_ball(self, ball):
        # get vector from center of rect to the ball
        to_ball = Vector((ball.x - self.rotate_origin_x), (ball.y - self.rotate_origin_y))

        # get x and y coordinates of above vector in rotated system
        x = to_ball.dot(self.rot_x_dir)  # along rect width
        y = to_ball.dot(self.rot_y_dir)  # along rect height

        # test for collision
        if x < -self.rect_width / 2 - ball.size[0] / 2:
            return False
        if x > self.rect_width / 2 + ball.size[0] / 2:
            return False
        if y < -self.rect_height / 2 - ball.size[1] / 2:
            return False
        if y > self.rect_height / 2 + ball.size[1] / 2:
            return False
        return True

class PongBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)
    collided = DictProperty(False)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos

class PongGame(Widget):
    ball = ObjectProperty(None)
    object = ObjectProperty(None)

    def start(self):
        Clock.schedule_interval(self.update, 1.0 / 60.0)
        self.ball.collided[self.object] = False

    def home(self):
        sm.current = 'P'

    def stage(self):
        sm.current = 'recycleview'

    def show_p(self):
        show_popup()

    def serve_ball(self, vel=(6, 0)):
        Clock.unschedule(self.update)
        self.ball.center = 60, 435
        self.ball.velocity = vel

    def update(self, dt):
        self.ball.move()
        self.object.deflect_ball(self.ball)

        if (self.ball.y < self.y+100):
           # self.ball.velocity_y *= -1
            self.ball.velocity_y = 0
            #show = True
            #if self.ball.y >= 49:
            Clock.unschedule(self.update)
            print('tested')
            #self.show_p()
            sm.current = 'stage comp'
           # print('Down')
            self.serve_ball()

        if (self.ball.top > self.top + 100):
            print('Up')
            Clock.unschedule(self.update)
            sm.current = 'loss'

class Object2(Widget):
    def __init__(self, *args, **kwargs):
        Widget.__init__(self, *args, **kwargs)
        self.rect_pos_x = 500
        self.rect_pos_y = 460
        self.rect_pos = self.rect_pos_x, self.rect_pos_y
        self.rect_width = 150
        self.rect_height = 15
        self.rect_size = self.rect_width, self.rect_height
        self.rotate_origin_x = self.rect_pos_x + self.rect_width / 2
        self.rotate_origin_y = self.rect_pos_y + self.rect_height / 2
        self.rotate_origin = self.rotate_origin_x, self.rotate_origin_y
        self.angle = 225
        self.rot_x_dir = Vector(1, 0).rotate(self.angle)
        self.rot_y_dir = Vector(0, 1).rotate(self.angle)
        print('rect 2')
        with self.canvas:
            PushMatrix()
            Rotate(origin=self.rotate_origin, angle=self.angle)
            Color(rgb=(0,197,68))
            Rectangle(pos=self.rect_pos, size=self.rect_size)
            PopMatrix()

    def rotate(self):
        self.canvas.clear()
        self.angle += 90
        if (self.angle > 315):
            self.angle = 225
        self.rot_x_dir = Vector(1, 0).rotate(self.angle)
        self.rot_y_dir = Vector(0, 1).rotate(self.angle)
        with self.canvas:
            PushMatrix()
            self.rot = Rotate(origin=self.rotate_origin, angle=self.angle)
            Color(rgb=(0, 255, 100))
            Rectangle(pos=self.rect_pos, size=self.rect_size)
            PopMatrix()

    def deflect_ball(self, ball):
        if self.collide_ball(ball):
            if not ball.collided[self]:
                vx, vy = ball.velocity
                if self.angle == 135:
                    ball.velocity = Vector(-vx, vy).rotate(90)
                if self.angle == 225:
                    ball.velocity = Vector(-vx, vy).rotate(270)
                if self.angle == 315:
                    ball.velocity = Vector(-vx, vy).rotate(90)
                print(ball.collided)
                ball.collided[self] = True
        else:
            ball.collided[self] = False

    def on_touch_up(self, touch):
        if self.collide_point(*touch.pos):
            self.rotate()
            print(self.angle)

    def collide_ball(self, ball):
        # get vector from center of rect to the ball
        to_ball = Vector((ball.x - self.rotate_origin_x), (ball.y - self.rotate_origin_y))

        # get x and y coordinates of above vector in rotated system
        x = to_ball.dot(self.rot_x_dir)  # along rect width
        y = to_ball.dot(self.rot_y_dir)  # along rect height

        # test for collision
        if x < -self.rect_width / 2 - ball.size[0] / 2:
            return False
        if x > self.rect_width / 2 + ball.size[0] / 2:
            return False
        if y < -self.rect_height / 2 - ball.size[1] / 2:
            return False
        if y > self.rect_height / 2 + ball.size[1] / 2:
            return False
        return True

class Object3(Widget):
    def __init__(self, *args, **kwargs):
        Widget.__init__(self, *args, **kwargs)
        self.rect_pos_x = 480
        self.rect_pos_y = 220
        self.rect_pos = self.rect_pos_x, self.rect_pos_y
        self.rect_width = 150
        self.rect_height = 15
        self.rect_size = self.rect_width, self.rect_height
        self.rotate_origin_x = self.rect_pos_x + self.rect_width / 2
        self.rotate_origin_y = self.rect_pos_y + self.rect_height / 2
        self.rotate_origin = self.rotate_origin_x, self.rotate_origin_y
        self.angle = 135
        self.rot_x_dir = Vector(1, 0).rotate(self.angle)
        self.rot_y_dir = Vector(0, 1).rotate(self.angle)
        print('rect 3')
        with self.canvas:
            PushMatrix()
            Rotate(origin=self.rotate_origin, angle=self.angle)
            Color(rgb=(0,1,1))
            Rectangle(pos=self.rect_pos, size=self.rect_size)
            PopMatrix()

    def rotate(self):
        self.canvas.clear()
        self.angle += 90
        if (self.angle > 315):
            self.angle = 225
        self.rot_x_dir = Vector(1, 0).rotate(self.angle)
        self.rot_y_dir = Vector(0, 1).rotate(self.angle)
        with self.canvas:
            PushMatrix()
            self.rot = Rotate(origin=self.rotate_origin, angle=self.angle)
            Color(rgb=(0, 255, 100))
            Rectangle(pos=self.rect_pos, size=self.rect_size)
            PopMatrix()

    def deflect_ball(self, ball):
        if self.collide_ball(ball):
            if ball.collided[self] is False:
                vx, vy = ball.velocity
                if self.angle == 135:
                    ball.velocity = Vector(-vx, vy).rotate(90)
                if self.angle == 225:
                    ball.velocity = Vector(-vx, vy).rotate(270)
                if self.angle == 315:
                    ball.velocity = Vector(-vx, vy).rotate(90)
                print(ball.collided)
                ball.collided[self] = True

        else:
            ball.collided[self] = False

    def on_touch_up(self, touch):
        if self.collide_point(*touch.pos):
            self.rotate()
            print(self.angle)

    def collide_ball(self, ball):
        # get vector from center of rect to the ball
        to_ball = Vector((ball.x - self.rotate_origin_x), (ball.y - self.rotate_origin_y))

        # get x and y coordinates of above vector in rotated system
        x = to_ball.dot(self.rot_x_dir)  # along rect width
        y = to_ball.dot(self.rot_y_dir)  # along rect height

        # test for collision
        if x < -self.rect_width / 2 - ball.size[0] / 2:
            return False
        if x > self.rect_width / 2 + ball.size[0] / 2:
            return False
        if y < -self.rect_height / 2 - ball.size[1] / 2:
            return False
        if y > self.rect_height / 2 + ball.size[1] / 2:
            return False
        return True

class Stage_2(Widget):
    ball = ObjectProperty(None)
    object2 = ObjectProperty(None)
    object3 = ObjectProperty(None)

    def start(self):
        Clock.schedule_interval(self.update, 1.0 / 60.0)
        self.ball.collided[self.object3] = False
        self.ball.collided[self.object2] = False

    def home(self):
        sm.current = 'P'

    def stage(self):
        sm.current = 'recycleview'

    def serve_ball(self, vel=(6, 0)):
        self.ball.center = 60, 475
        self.ball.velocity = vel
        Clock.unschedule(self.update)
        print('served')

    def update(self, dt):
        self.ball.move()
        self.object2.deflect_ball(self.ball)
        self.object3.deflect_ball(self.ball)

        if (self.ball.y < self.y+300) and (self.ball.x < 10):
           # self.ball.velocity_y *= -1
            self.ball.velocity_y = 0
            #show = True
            #if self.ball.y >= 49:
            Clock.unschedule(self.update)
            print('tested')
            #self.show_p()
            sm.current = 'stage comp'
           # print('Down')
            self.serve_ball()

        if (self.ball.top > self.top) or (self.ball.x > 800) :
            print('Up')
            Clock.unschedule(self.update)
            sm.current = 'loss'
            self.serve_ball()

class Object4(Widget):
    def __init__(self, *args, **kwargs):
        Widget.__init__(self, *args, **kwargs)
        self.rect_pos_x = 240
        self.rect_pos_y = 200
        self.rect_pos = self.rect_pos_x, self.rect_pos_y
        self.rect_width = 150
        self.rect_height = 15
        self.rect_size = self.rect_width, self.rect_height
        self.rotate_origin_x = self.rect_pos_x + self.rect_width / 2
        self.rotate_origin_y = self.rect_pos_y + self.rect_height / 2
        self.rotate_origin = self.rotate_origin_x, self.rotate_origin_y
        self.angle = 225
        self.rot_x_dir = Vector(1, 0).rotate(self.angle)
        self.rot_y_dir = Vector(0, 1).rotate(self.angle)
        print('rect 4')
        with self.canvas:
            PushMatrix()
            Rotate(origin=self.rotate_origin, angle=self.angle)
            Color(rgb=(0,1,1))
            Rectangle(pos=self.rect_pos, size=self.rect_size)
            PopMatrix()
        #    self.pos = self.rect_pos
         #   self.size = self.rect_size

    def rotate(self):
        self.canvas.clear()
        self.angle += 90
        if (self.angle > 315):
            self.angle = 225
        self.rot_x_dir = Vector(1, 0).rotate(self.angle)
        self.rot_y_dir = Vector(0, 1).rotate(self.angle)
        with self.canvas:
            PushMatrix()
            self.rot = Rotate(origin=self.rotate_origin, angle=self.angle)
            Color(rgb=(0, 1, 1))
            Rectangle(pos=self.rect_pos, size=self.rect_size)
            PopMatrix()

    def deflect_ball(self, ball):
        if self.collide_ball(ball):
            if not ball.collided[self]:
                vx, vy = ball.velocity
                if self.angle == 135:
                    ball.velocity = Vector(-vx, vy).rotate(90)
                if self.angle == 225:
                    ball.velocity = Vector(-vx, vy).rotate(270)
                if self.angle == 315:
                    ball.velocity = Vector(-vx, vy).rotate(90)
                ball.collided[self] = True
        else:
            ball.collided[self] = False

    def on_touch_up(self, touch):
        if self.collide_point(*touch.pos):
            self.rotate()
            print(self.angle)

    def collide_ball(self, ball):
        # get vector from center of rect to the ball
        to_ball = Vector((ball.x - self.rotate_origin_x), (ball.y - self.rotate_origin_y))

        # get x and y coordinates of above vector in rotated system
        x = to_ball.dot(self.rot_x_dir)  # along rect width
        y = to_ball.dot(self.rot_y_dir)  # along rect height

        # test for collision
        if x < -self.rect_width / 2 - ball.size[0] / 2:
            return False
        if x > self.rect_width / 2 + ball.size[0] / 2:
            return False
        if y < -self.rect_height / 2 - ball.size[1] / 2:
            return False
        if y > self.rect_height / 2 + ball.size[1] / 2:
            return False
        return True

class Object5(Widget):
    def __init__(self, *args, **kwargs):
        Widget.__init__(self, *args, **kwargs)
        self.rect_pos_x = 260
        self.rect_pos_y = 450
        self.rect_pos = self.rect_pos_x, self.rect_pos_y
        self.rect_width = 150
        self.rect_height = 15
        self.rect_size = self.rect_width, self.rect_height
        self.rotate_origin_x = self.rect_pos_x + self.rect_width / 2
        self.rotate_origin_y = self.rect_pos_y + self.rect_height / 2
        self.rotate_origin = self.rotate_origin_x, self.rotate_origin_y
        self.angle = 135
        self.rot_x_dir = Vector(1, 0).rotate(self.angle)
        self.rot_y_dir = Vector(0, 1).rotate(self.angle)
        print('rect 5')
        with self.canvas:
            PushMatrix()
            Rotate(origin=self.rotate_origin, angle=self.angle)
            Color(rgb=(0,1,1))
            Rectangle(pos=self.rect_pos, size=self.rect_size)
            PopMatrix()

    def rotate(self):
        self.canvas.clear()
        self.angle += 90
        if (self.angle > 315):
            self.angle = 225
        self.rot_x_dir = Vector(1, 0).rotate(self.angle)
        self.rot_y_dir = Vector(0, 1).rotate(self.angle)
        with self.canvas:
            PushMatrix()
            self.rot = Rotate(origin=self.rotate_origin, angle=self.angle)
            Color(rgb=(0, 1, 1))
            Rectangle(pos=self.rect_pos, size=self.rect_size)
            PopMatrix()

    def deflect_ball(self, ball):
        if self.collide_ball(ball):
            if not ball.collided[self]:
                vx, vy = ball.velocity
                if self.angle == 135:
                    ball.velocity = Vector(-vx, vy).rotate(90)
                if self.angle == 225:
                    ball.velocity = Vector(-vx, vy).rotate(270)
                if self.angle == 315:
                    ball.velocity = Vector(-vx, vy).rotate(90)
                ball.collided[self] = True
        else:
            ball.collided[self] = False

    def on_touch_up(self, touch):
        if self.collide_point(*touch.pos):
            self.rotate()
            print(self.angle)

    def collide_ball(self, ball):
        # get vector from center of rect to the ball
        to_ball = Vector((ball.x - self.rotate_origin_x), (ball.y - self.rotate_origin_y))

        # get x and y coordinates of above vector in rotated system
        x = to_ball.dot(self.rot_x_dir)  # along rect width
        y = to_ball.dot(self.rot_y_dir)  # along rect height

        # test for collision
        if x < -self.rect_width / 2 - ball.size[0] / 2:
            return False
        if x > self.rect_width / 2 + ball.size[0] / 2:
            return False
        if y < -self.rect_height / 2 - ball.size[1] / 2:
            return False
        if y > self.rect_height / 2 + ball.size[1] / 2:
            return False
        return True

class Object6(Widget):
    def __init__(self, *args, **kwargs):
        Widget.__init__(self, *args, **kwargs)
        self.rect_pos_x = 530
        self.rect_pos_y = 230
        self.rect_pos = self.rect_pos_x, self.rect_pos_y
        self.rect_width = 150
        self.rect_height = 15
        self.rect_size = self.rect_width, self.rect_height
        self.rotate_origin_x = self.rect_pos_x + self.rect_width / 2
        self.rotate_origin_y = self.rect_pos_y + self.rect_height / 2
        self.rotate_origin = self.rotate_origin_x, self.rotate_origin_y
        self.angle = 135
        self.rot_x_dir = Vector(1, 0).rotate(self.angle)
        self.rot_y_dir = Vector(0, 1).rotate(self.angle)
        print('rect 6')
        with self.canvas:
            PushMatrix()
            Rotate(origin=self.rotate_origin, angle=self.angle)
            Color(rgb=(0,1,1))
            Rectangle(pos=self.rect_pos, size=self.rect_size)
            PopMatrix()

    def rotate(self):
        self.canvas.clear()
        self.angle += 90
        if (self.angle > 315):
            self.angle = 225
        self.rot_x_dir = Vector(1, 0).rotate(self.angle)
        self.rot_y_dir = Vector(0, 1).rotate(self.angle)
        with self.canvas:
            PushMatrix()
            self.rot = Rotate(origin=self.rotate_origin, angle=self.angle)
            Color(rgb=(0, 255, 100))
            Rectangle(pos=self.rect_pos, size=self.rect_size)
            PopMatrix()

    def deflect_ball(self, ball):
        if self.collide_ball(ball):
            if not ball.collided[self]:
                vx, vy = ball.velocity
                if self.angle == 135:
                    ball.velocity = Vector(-vx, vy).rotate(90)
                if self.angle == 225:
                    ball.velocity = Vector(-vx, vy).rotate(270)
                if self.angle == 315:
                    ball.velocity = Vector(-vx, vy).rotate(90)
                ball.collided[self] = True
        else:
            ball.collided[self] = False

    def on_touch_up(self, touch):
        if self.collide_point(*touch.pos):
            self.rotate()
            print(self.angle)

    def collide_ball(self, ball):
        # get vector from center of rect to the ball
        to_ball = Vector((ball.x - self.rotate_origin_x), (ball.y - self.rotate_origin_y))

        # get x and y coordinates of above vector in rotated system
        x = to_ball.dot(self.rot_x_dir)  # along rect width
        y = to_ball.dot(self.rot_y_dir)  # along rect height

        # test for collision
        if x < -self.rect_width / 2 - ball.size[0] / 2:
            return False
        if x > self.rect_width / 2 + ball.size[0] / 2:
            return False
        if y < -self.rect_height / 2 - ball.size[1] / 2:
            return False
        if y > self.rect_height / 2 + ball.size[1] / 2:
            return False
        return True

class Stage_3(Widget):
    ball = ObjectProperty(None)
    object5 = ObjectProperty(None)
    object4 = ObjectProperty(None)
    object6 = ObjectProperty(None)

    def start(self):
        Clock.schedule_interval(self.update, 1.0 / 60.0)
        self.ball.collided[self.object4] = False
        self.ball.collided[self.object5] = False
        self.ball.collided[self.object6] = False

    def home(self):
        sm.current = 'P'

    def stage(self):
        sm.current = 'recycleview'

    def serve_ball(self, vel=(6, 0)):
        Clock.unschedule(self.update)
        self.ball.center = 60, 470
        self.ball.velocity = vel
        print('served')

    def update(self, dt):
        self.ball.move()
        self.object5.deflect_ball(self.ball)
        self.object4.deflect_ball(self.ball)
        self.object6.deflect_ball(self.ball)

        if (self.ball.y > self.y+550) and (self.ball.x > 400):
           # self.ball.velocity_y *= -1
            self.ball.velocity_y = 0
            #show = True
            #if self.ball.y >= 49:
            Clock.unschedule(self.update)
            print('tested')
            #self.show_p()
            sm.current = 'stage comp'
           # print('Down')
            self.serve_ball()

        if (self.ball.top > self.top) or (self.ball.x<-10) or (self.ball.y< 0):
            print('Up')
            Clock.unschedule(self.update)
            sm.current = 'loss'
            self.serve_ball()

class Object7(Widget):
    def __init__(self, *args, **kwargs):
        Widget.__init__(self, *args, **kwargs)
        self.rect_pos_x = 280
        self.rect_pos_y = 220
        self.rect_pos = self.rect_pos_x, self.rect_pos_y
        self.rect_width = 150
        self.rect_height = 15
        self.rect_size = self.rect_width, self.rect_height
        self.rotate_origin_x = self.rect_pos_x + self.rect_width / 2
        self.rotate_origin_y = self.rect_pos_y + self.rect_height / 2
        self.rotate_origin = self.rotate_origin_x, self.rotate_origin_y
        self.angle = 135
        self.rot_x_dir = Vector(1, 0).rotate(self.angle)
        self.rot_y_dir = Vector(0, 1).rotate(self.angle)
        print('rect 7')
        with self.canvas:
            PushMatrix()
            Rotate(origin=self.rotate_origin, angle=self.angle)
            Color(rgb=(0,1,1))
            Rectangle(pos=self.rect_pos, size=self.rect_size)
            PopMatrix()
        #    self.pos = self.rect_pos
         #   self.size = self.rect_size

    def rotate(self):
        self.canvas.clear()
        self.angle += 90
        if (self.angle > 315):
            self.angle = 225
        self.rot_x_dir = Vector(1, 0).rotate(self.angle)
        self.rot_y_dir = Vector(0, 1).rotate(self.angle)
        with self.canvas:
            PushMatrix()
            self.rot = Rotate(origin=self.rotate_origin, angle=self.angle)
            Color(rgb=(0, 255, 100))
            Rectangle(pos=self.rect_pos, size=self.rect_size)
            PopMatrix()

    def deflect_ball(self, ball):
        if self.collide_ball(ball):
            if not ball.collided[self]:
                vx, vy = ball.velocity
                if self.angle == 135:
                    ball.velocity = Vector(-vx, vy).rotate(90)
                if self.angle == 225:
                    ball.velocity = Vector(-vx, vy).rotate(270)
                if self.angle == 315:
                    ball.velocity = Vector(-vx, vy).rotate(90)
                ball.collided[self] = True
        else:
            ball.collided[self] = False

    def on_touch_up(self, touch):
        if self.collide_point(*touch.pos):
            self.rotate()
            print(self.angle)

    def collide_ball(self, ball):
        # get vector from center of rect to the ball
        to_ball = Vector((ball.x - self.rotate_origin_x), (ball.y - self.rotate_origin_y))

        # get x and y coordinates of above vector in rotated system
        x = to_ball.dot(self.rot_x_dir)  # along rect width
        y = to_ball.dot(self.rot_y_dir)  # along rect height

        # test for collision
        if x < -self.rect_width / 2 - ball.size[0] / 2:
            return False
        if x > self.rect_width / 2 + ball.size[0] / 2:
            return False
        if y < -self.rect_height / 2 - ball.size[1] / 2:
            return False
        if y > self.rect_height / 2 + ball.size[1] / 2:
            return False
        return True

class Object8(Widget):
    def __init__(self, *args, **kwargs):
        Widget.__init__(self, *args, **kwargs)
        self.rect_pos_x = 530
        self.rect_pos_y = 450
        self.rect_pos = self.rect_pos_x, self.rect_pos_y
        self.rect_width = 150
        self.rect_height = 15
        self.rect_size = self.rect_width, self.rect_height
        self.rotate_origin_x = self.rect_pos_x + self.rect_width / 2
        self.rotate_origin_y = self.rect_pos_y + self.rect_height / 2
        self.rotate_origin = self.rotate_origin_x, self.rotate_origin_y
        self.angle = 225
        self.rot_x_dir = Vector(1, 0).rotate(self.angle)
        self.rot_y_dir = Vector(0, 1).rotate(self.angle)
        print('rect 8')
        with self.canvas:
            PushMatrix()
            Rotate(origin=self.rotate_origin, angle=self.angle)
            Color(rgb=(0,1,1))
            Rectangle(pos=self.rect_pos, size=self.rect_size)
            PopMatrix()

    def rotate(self):
        self.canvas.clear()
        self.angle += 90
        if (self.angle > 315):
            self.angle = 225
        self.rot_x_dir = Vector(1, 0).rotate(self.angle)
        self.rot_y_dir = Vector(0, 1).rotate(self.angle)
        with self.canvas:
            PushMatrix()
            self.rot = Rotate(origin=self.rotate_origin, angle=self.angle)
            Color(rgb=(0, 255, 100))
            Rectangle(pos=self.rect_pos, size=self.rect_size)
            PopMatrix()

    def deflect_ball(self, ball):
        if self.collide_ball(ball):
            if not ball.collided[self]:
                vx, vy = ball.velocity
                if self.angle == 135:
                    ball.velocity = Vector(-vx, vy).rotate(90)
                if self.angle == 225:
                    ball.velocity = Vector(-vx, vy).rotate(270)
                if self.angle == 315:
                    ball.velocity = Vector(-vx, vy).rotate(90)
                ball.collided[self] = True
        else:
            ball.collided[self] = False

    def on_touch_up(self, touch):
        if self.collide_point(*touch.pos):
            self.rotate()
            print(self.angle)

    def collide_ball(self, ball):
        # get vector from center of rect to the ball
        to_ball = Vector((ball.x - self.rotate_origin_x), (ball.y - self.rotate_origin_y))

        # get x and y coordinates of above vector in rotated system
        x = to_ball.dot(self.rot_x_dir)  # along rect width
        y = to_ball.dot(self.rot_y_dir)  # along rect height

        # test for collision
        if x < -self.rect_width / 2 - ball.size[0] / 2:
            return False
        if x > self.rect_width / 2 + ball.size[0] / 2:
            return False
        if y < -self.rect_height / 2 - ball.size[1] / 2:
            return False
        if y > self.rect_height / 2 + ball.size[1] / 2:
            return False
        return True

class Object9(Widget):
    def __init__(self, *args, **kwargs):
        Widget.__init__(self, *args, **kwargs)
        self.rect_pos_x = 530
        self.rect_pos_y = 220
        self.rect_pos = self.rect_pos_x, self.rect_pos_y
        self.rect_width = 150
        self.rect_height = 15
        self.rect_size = self.rect_width, self.rect_height
        self.rotate_origin_x = self.rect_pos_x + self.rect_width / 2
        self.rotate_origin_y = self.rect_pos_y + self.rect_height / 2
        self.rotate_origin = self.rotate_origin_x, self.rotate_origin_y
        self.angle = 135
        self.rot_x_dir = Vector(1, 0).rotate(self.angle)
        self.rot_y_dir = Vector(0, 1).rotate(self.angle)
        print('rect 9')
        with self.canvas:
            PushMatrix()
            Rotate(origin=self.rotate_origin, angle=self.angle)
            Color(rgb=(0,1,1))
            Rectangle(pos=self.rect_pos, size=self.rect_size)
            PopMatrix()

    def rotate(self):
        self.canvas.clear()
        self.angle += 90
        if (self.angle > 315):
            self.angle = 225
        self.rot_x_dir = Vector(1, 0).rotate(self.angle)
        self.rot_y_dir = Vector(0, 1).rotate(self.angle)
        with self.canvas:
            PushMatrix()
            self.rot = Rotate(origin=self.rotate_origin, angle=self.angle)
            Color(rgb=(0, 255, 100))
            Rectangle(pos=self.rect_pos, size=self.rect_size)
            PopMatrix()

    def deflect_ball(self, ball):
        if self.collide_ball(ball):
            if not ball.collided[self]:
                vx, vy = ball.velocity
                if self.angle == 135:
                    ball.velocity = Vector(-vx, vy).rotate(90)
                if self.angle == 225:
                    ball.velocity = Vector(-vx, vy).rotate(270)
                if self.angle == 315:
                    ball.velocity = Vector(-vx, vy).rotate(90)
                ball.collided[self] = True
        else:
            ball.collided[self] = False

    def on_touch_up(self, touch):
        if self.collide_point(*touch.pos):
            self.rotate()
            print(self.angle)

    def collide_ball(self, ball):
        # get vector from center of rect to the ball
        to_ball = Vector((ball.x - self.rotate_origin_x), (ball.y - self.rotate_origin_y))

        # get x and y coordinates of above vector in rotated system
        x = to_ball.dot(self.rot_x_dir)  # along rect width
        y = to_ball.dot(self.rot_y_dir)  # along rect height

        # test for collision
        if x < -self.rect_width / 2 - ball.size[0] / 2:
            return False
        if x > self.rect_width / 2 + ball.size[0] / 2:
            return False
        if y < -self.rect_height / 2 - ball.size[1] / 2:
            return False
        if y > self.rect_height / 2 + ball.size[1] / 2:
            return False
        return True

class Stage_4(Widget):
    ball = ObjectProperty(None)
    object7 = ObjectProperty(None)
    object8 = ObjectProperty(None)
    object9 = ObjectProperty(None)

    def start(self):
        Clock.schedule_interval(self.update, 1.0 / 60.0)
        self.ball.collided[self.object7] = False
        self.ball.collided[self.object8] = False
        self.ball.collided[self.object9] = False

    def home(self):
        sm.current = 'P'

    def stage(self):
        sm.current = 'recycleview'

    def serve_ball(self, vel=(6, 0)):
        Clock.unschedule(self.update)
        self.ball.center = 60, 465
        self.ball.velocity = vel
        print('served')

    def update(self, dt):
        self.ball.move()
        self.object7.deflect_ball(self.ball)
        self.object8.deflect_ball(self.ball)
        self.object9.deflect_ball(self.ball)

        if (self.ball.y > self.y+550) and (self.ball.x < 450):
           # self.ball.velocity_y *= -1
            self.ball.velocity_y = 0
            #show = True
            #if self.ball.y >= 49:
            Clock.unschedule(self.update)
            print('tested')
            #self.show_p()
            sm.current = 'stage comp'
           # print('Down')
            self.serve_ball()

        if (self.ball.top > self.top) and (self.ball.x>500) or (self.ball.x> 800) or (self.ball.y<0):
            print('Up')
            Clock.unschedule(self.update)
            sm.current = 'loss'
            self.serve_ball()

class Object10(Widget):
    def __init__(self, *args, **kwargs):
        Widget.__init__(self, *args, **kwargs)
        self.rect_pos_x = 260
        self.rect_pos_y = 200
        self.rect_pos = self.rect_pos_x, self.rect_pos_y
        self.rect_width = 150
        self.rect_height = 15
        self.rect_size = self.rect_width, self.rect_height
        self.rotate_origin_x = self.rect_pos_x + self.rect_width / 2
        self.rotate_origin_y = self.rect_pos_y + self.rect_height / 2
        self.rotate_origin = self.rotate_origin_x, self.rotate_origin_y
        self.angle = 225
        self.rot_x_dir = Vector(1, 0).rotate(self.angle)
        self.rot_y_dir = Vector(0, 1).rotate(self.angle)
        print('rect 10')
        with self.canvas:
            PushMatrix()
            Rotate(origin=self.rotate_origin, angle=self.angle)
            Color(rgb=(0,1,1))
            Rectangle(pos=self.rect_pos, size=self.rect_size)
            PopMatrix()
        #    self.pos = self.rect_pos
         #   self.size = self.rect_size

    def rotate(self):
        self.canvas.clear()
        self.angle += 90
        if (self.angle > 315):
            self.angle = 225
        self.rot_x_dir = Vector(1, 0).rotate(self.angle)
        self.rot_y_dir = Vector(0, 1).rotate(self.angle)
        with self.canvas:
            PushMatrix()
            self.rot = Rotate(origin=self.rotate_origin, angle=self.angle)
            Color(rgb=(0, 255, 100))
            Rectangle(pos=self.rect_pos, size=self.rect_size)
            PopMatrix()

    def deflect_ball(self, ball):
        if self.collide_ball(ball):
            if not ball.collided[self]:
                vx, vy = ball.velocity
                if self.angle == 135:
                    ball.velocity = Vector(-vx, vy).rotate(90)
                if self.angle == 225:
                    ball.velocity = Vector(-vx, vy).rotate(270)
                if self.angle == 315:
                    ball.velocity = Vector(-vx, vy).rotate(90)
                ball.collided[self] = True
        else:
            ball.collided[self] = False

    def on_touch_up(self, touch):
        if self.collide_point(*touch.pos):
            self.rotate()
            print(self.angle)

    def collide_ball(self, ball):
        # get vector from center of rect to the ball
        to_ball = Vector((ball.x - self.rotate_origin_x), (ball.y - self.rotate_origin_y))

        # get x and y coordinates of above vector in rotated system
        x = to_ball.dot(self.rot_x_dir)  # along rect width
        y = to_ball.dot(self.rot_y_dir)  # along rect height

        # test for collision
        if x < -self.rect_width / 2 - ball.size[0] / 2:
            return False
        if x > self.rect_width / 2 + ball.size[0] / 2:
            return False
        if y < -self.rect_height / 2 - ball.size[1] / 2:
            return False
        if y > self.rect_height / 2 + ball.size[1] / 2:
            return False
        return True

class Object11(Widget):
    def __init__(self, *args, **kwargs):
        Widget.__init__(self, *args, **kwargs)
        self.rect_pos_x = 300
        self.rect_pos_y = 440
        self.rect_pos = self.rect_pos_x, self.rect_pos_y
        self.rect_width = 150
        self.rect_height = 15
        self.rect_size = self.rect_width, self.rect_height
        self.rotate_origin_x = self.rect_pos_x + self.rect_width / 2
        self.rotate_origin_y = self.rect_pos_y + self.rect_height / 2
        self.rotate_origin = self.rotate_origin_x, self.rotate_origin_y
        self.angle = 135
        self.rot_x_dir = Vector(1, 0).rotate(self.angle)
        self.rot_y_dir = Vector(0, 1).rotate(self.angle)
        print('rect 11')
        with self.canvas:
            PushMatrix()
            Rotate(origin=self.rotate_origin, angle=self.angle)
            Color(rgb=(1,0,1))
            Rectangle(pos=self.rect_pos, size=self.rect_size)
            PopMatrix()

    def rotate(self):
        self.canvas.clear()
        self.angle += 90
        if (self.angle > 315):
            self.angle = 225
        self.rot_x_dir = Vector(1, 0).rotate(self.angle)
        self.rot_y_dir = Vector(0, 1).rotate(self.angle)
        with self.canvas:
            PushMatrix()
            self.rot = Rotate(origin=self.rotate_origin, angle=self.angle)
            Color(rgb=(0, 255, 100))
            Rectangle(pos=self.rect_pos, size=self.rect_size)
            PopMatrix()

    def deflect_ball(self, ball):
        if self.collide_ball(ball):
            if not ball.collided[self]:
                vx, vy = ball.velocity
                if self.angle == 135:
                    ball.velocity = Vector(-vx, vy).rotate(90)
                if self.angle == 225:
                    ball.velocity = Vector(-vx, vy).rotate(270)
                if self.angle == 315:
                    ball.velocity = Vector(-vx, vy).rotate(90)
                ball.collided[self] = True
        else:
            ball.collided[self] = False

    def collide_ball(self, ball):
        # get vector from center of rect to the ball
        to_ball = Vector((ball.x - self.rotate_origin_x), (ball.y - self.rotate_origin_y))

        # get x and y coordinates of above vector in rotated system
        x = to_ball.dot(self.rot_x_dir)  # along rect width
        y = to_ball.dot(self.rot_y_dir)  # along rect height

        # test for collision
        if x < -self.rect_width / 2 - ball.size[0] / 2:
            return False
        if x > self.rect_width / 2 + ball.size[0] / 2:
            return False
        if y < -self.rect_height / 2 - ball.size[1] / 2:
            return False
        if y > self.rect_height / 2 + ball.size[1] / 2:
            return False
        return True

class Object12(Widget):
    def __init__(self, *args, **kwargs):
        Widget.__init__(self, *args, **kwargs)
        self.rect_pos_x = 530
        self.rect_pos_y = 210
        self.rect_pos = self.rect_pos_x, self.rect_pos_y
        self.rect_width = 150
        self.rect_height = 15
        self.rect_size = self.rect_width, self.rect_height
        self.rotate_origin_x = self.rect_pos_x + self.rect_width / 2
        self.rotate_origin_y = self.rect_pos_y + self.rect_height / 2
        self.rotate_origin = self.rotate_origin_x, self.rotate_origin_y
        self.angle = 135
        self.rot_x_dir = Vector(1, 0).rotate(self.angle)
        self.rot_y_dir = Vector(0, 1).rotate(self.angle)
        print('rect 12')
        with self.canvas:
            PushMatrix()
            Rotate(origin=self.rotate_origin, angle=self.angle)
            Color(rgb=(0,1,1))
            Rectangle(pos=self.rect_pos, size=self.rect_size)
            PopMatrix()

    def rotate(self):
        self.canvas.clear()
        self.angle += 90
        if (self.angle > 315):
            self.angle = 225
        self.rot_x_dir = Vector(1, 0).rotate(self.angle)
        self.rot_y_dir = Vector(0, 1).rotate(self.angle)
        with self.canvas:
            PushMatrix()
            self.rot = Rotate(origin=self.rotate_origin, angle=self.angle)
            Color(rgb=(0, 1, 1))
            Rectangle(pos=self.rect_pos, size=self.rect_size)
            PopMatrix()

    def deflect_ball(self, ball):
        if self.collide_ball(ball):
            if not ball.collided[self]:
                vx, vy = ball.velocity
                if self.angle == 135:
                    ball.velocity = Vector(-vx, vy).rotate(90)
                if self.angle == 225:
                    ball.velocity = Vector(-vx, vy).rotate(270)
                if self.angle == 315:
                    ball.velocity = Vector(-vx, vy).rotate(90)
                ball.collided[self] = True
        else:
            ball.collided[self] = False

    def on_touch_up(self, touch):
        if self.collide_point(*touch.pos):
            self.rotate()
            print(self.angle)

    def collide_ball(self, ball):
        # get vector from center of rect to the ball
        to_ball = Vector((ball.x - self.rotate_origin_x), (ball.y - self.rotate_origin_y))

        # get x and y coordinates of above vector in rotated system
        x = to_ball.dot(self.rot_x_dir)  # along rect width
        y = to_ball.dot(self.rot_y_dir)  # along rect height

        # test for collision
        if x < -self.rect_width / 2 - ball.size[0] / 2:
            return False
        if x > self.rect_width / 2 + ball.size[0] / 2:
            return False
        if y < -self.rect_height / 2 - ball.size[1] / 2:
            return False
        if y > self.rect_height / 2 + ball.size[1] / 2:
            return False
        return True

class Object13(Widget):
    def __init__(self, *args, **kwargs):
        Widget.__init__(self, *args, **kwargs)
        self.rect_pos_x = 530
        self.rect_pos_y = 460
        self.rect_pos = self.rect_pos_x, self.rect_pos_y
        self.rect_width = 150
        self.rect_height = 15
        self.rect_size = self.rect_width, self.rect_height
        self.rotate_origin_x = self.rect_pos_x + self.rect_width / 2
        self.rotate_origin_y = self.rect_pos_y + self.rect_height / 2
        self.rotate_origin = self.rotate_origin_x, self.rotate_origin_y
        self.angle = 225
        self.rot_x_dir = Vector(1, 0).rotate(self.angle)
        self.rot_y_dir = Vector(0, 1).rotate(self.angle)
        print('rect 13')
        with self.canvas:
            PushMatrix()
            Rotate(origin=self.rotate_origin, angle=self.angle)
            Color(rgb=(0,1,1))
            Rectangle(pos=self.rect_pos, size=self.rect_size)
            PopMatrix()

    def rotate(self):
        self.canvas.clear()
        self.angle += 90
        if (self.angle > 315):
            self.angle = 225
        self.rot_x_dir = Vector(1, 0).rotate(self.angle)
        self.rot_y_dir = Vector(0, 1).rotate(self.angle)
        with self.canvas:
            PushMatrix()
            self.rot = Rotate(origin=self.rotate_origin, angle=self.angle)
            Color(rgb=(0, 255, 100))
            Rectangle(pos=self.rect_pos, size=self.rect_size)
            PopMatrix()

    def deflect_ball(self, ball):
        if self.collide_ball(ball):
            if not ball.collided[self]:
                vx, vy = ball.velocity
                if self.angle == 135:
                    ball.velocity = Vector(-vx, vy).rotate(90)
                if self.angle == 225:
                    ball.velocity = Vector(-vx, vy).rotate(270)
                if self.angle == 315:
                    ball.velocity = Vector(-vx, vy).rotate(90)
                ball.collided[self] = True
        else:
            ball.collided[self] = False

    def on_touch_up(self, touch):
        if self.collide_point(*touch.pos):
            self.rotate()
            print(self.angle)

    def collide_ball(self, ball):
        # get vector from center of rect to the ball
        to_ball = Vector((ball.x - self.rotate_origin_x), (ball.y - self.rotate_origin_y))

        # get x and y coordinates of above vector in rotated system
        x = to_ball.dot(self.rot_x_dir)  # along rect width
        y = to_ball.dot(self.rot_y_dir)  # along rect height

        # test for collision
        if x < -self.rect_width / 2 - ball.size[0] / 2:
            return False
        if x > self.rect_width / 2 + ball.size[0] / 2:
            return False
        if y < -self.rect_height / 2 - ball.size[1] / 2:
            return False
        if y > self.rect_height / 2 + ball.size[1] / 2:
            return False
        return True

class Stage_5(Widget):
    ball = ObjectProperty(None)
    object10 = ObjectProperty(None)
    object11 = ObjectProperty(None)
    object12 = ObjectProperty(None)
    object13 = ObjectProperty(None)

    def start(self):
        Clock.schedule_interval(self.update, 1.0 / 60.0)
        self.ball.collided[self.object10] = False
        self.ball.collided[self.object11] = False
        self.ball.collided[self.object12] = False
        self.ball.collided[self.object13] = False

    def home(self):
        sm.current = 'P'

    def stage(self):
        sm.current = 'recycleview'

    def serve_ball(self, vel=(6, 0)):
        Clock.unschedule(self.update)
        self.ball.center = 60, 465
        self.ball.velocity = vel
        print('served')

    def update(self, dt):
        self.ball.move()
        self.object10.deflect_ball(self.ball)
        self.object11.deflect_ball(self.ball)
        self.object12.deflect_ball(self.ball)
        self.object13.deflect_ball(self.ball)

        if (self.ball.y > self.y+600) and (self.ball.x < 450):
            self.ball.velocity_y = 0
            Clock.unschedule(self.update)
            print('tested')
            sm.current = 'stage comp'
            self.serve_ball()

        if (self.ball.x>750) or (self.ball.x< -20) or (self.ball.y<110):
            print('Up')
            Clock.unschedule(self.update)
            sm.current = 'loss'
            self.serve_ball()

class Object14(Widget):
    def __init__(self, *args, **kwargs):
        Widget.__init__(self, *args, **kwargs)
        self.rect_pos_x = 80
        self.rect_pos_y = 150
        self.rect_pos = self.rect_pos_x, self.rect_pos_y
        self.rect_width = 150
        self.rect_height = 15
        self.rect_size = self.rect_width, self.rect_height
        self.rotate_origin_x = self.rect_pos_x + self.rect_width / 2
        self.rotate_origin_y = self.rect_pos_y + self.rect_height / 2
        self.rotate_origin = self.rotate_origin_x, self.rotate_origin_y
        self.angle = 225
        self.rot_x_dir = Vector(1, 0).rotate(self.angle)
        self.rot_y_dir = Vector(0, 1).rotate(self.angle)
        print('rect 14')
        with self.canvas:
            PushMatrix()
            Rotate(origin=self.rotate_origin, angle=self.angle)
            Color(rgb=(0,1,1))
            Rectangle(pos=self.rect_pos, size=self.rect_size)
            PopMatrix()
        #    self.pos = self.rect_pos
         #   self.size = self.rect_size

    def rotate(self):
        self.canvas.clear()
        self.angle += 90
        if (self.angle > 315):
            self.angle = 225
        self.rot_x_dir = Vector(1, 0).rotate(self.angle)
        self.rot_y_dir = Vector(0, 1).rotate(self.angle)
        with self.canvas:
            PushMatrix()
            self.rot = Rotate(origin=self.rotate_origin, angle=self.angle)
            Color(rgb=(0, 255, 100))
            Rectangle(pos=self.rect_pos, size=self.rect_size)
            PopMatrix()

    def deflect_ball(self, ball):
        if self.collide_ball(ball):
            if not ball.collided[self]:
                vx, vy = ball.velocity
                if self.angle == 135:
                    ball.velocity = Vector(-vx, vy).rotate(90)
                if self.angle == 225:
                    ball.velocity = Vector(-vx, vy).rotate(270)
                if self.angle == 315:
                    ball.velocity = Vector(-vx, vy).rotate(90)
                ball.collided[self] = True
        else:
            ball.collided[self] = False

    def on_touch_up(self, touch):
        if self.collide_point(*touch.pos):
            self.rotate()
            print(self.angle)

    def collide_ball(self, ball):
        # get vector from center of rect to the ball
        to_ball = Vector((ball.x - self.rotate_origin_x), (ball.y - self.rotate_origin_y))

        # get x and y coordinates of above vector in rotated system
        x = to_ball.dot(self.rot_x_dir)  # along rect width
        y = to_ball.dot(self.rot_y_dir)  # along rect height

        # test for collision
        if x < -self.rect_width / 2 - ball.size[0] / 2:
            return False
        if x > self.rect_width / 2 + ball.size[0] / 2:
            return False
        if y < -self.rect_height / 2 - ball.size[1] / 2:
            return False
        if y > self.rect_height / 2 + ball.size[1] / 2:
            return False
        return True

class Object15(Widget):
    def __init__(self, *args, **kwargs):
        Widget.__init__(self, *args, **kwargs)
        self.rect_pos_x = 80
        self.rect_pos_y = 310
        self.rect_pos = self.rect_pos_x, self.rect_pos_y
        self.rect_width = 150
        self.rect_height = 15
        self.rect_size = self.rect_width, self.rect_height
        self.rotate_origin_x = self.rect_pos_x + self.rect_width / 2
        self.rotate_origin_y = self.rect_pos_y + self.rect_height / 2
        self.rotate_origin = self.rotate_origin_x, self.rotate_origin_y
        self.angle = 135
        self.rot_x_dir = Vector(1, 0).rotate(self.angle)
        self.rot_y_dir = Vector(0, 1).rotate(self.angle)
        print('rect 15')
        with self.canvas:
            PushMatrix()
            Rotate(origin=self.rotate_origin, angle=self.angle)
            Color(rgb=(0,1,1))
            Rectangle(pos=self.rect_pos, size=self.rect_size)
            PopMatrix()

    def rotate(self):
        self.canvas.clear()
        self.angle += 90
        if (self.angle > 315):
            self.angle = 225
        self.rot_x_dir = Vector(1, 0).rotate(self.angle)
        self.rot_y_dir = Vector(0, 1).rotate(self.angle)
        with self.canvas:
            PushMatrix()
            self.rot = Rotate(origin=self.rotate_origin, angle=self.angle)
            Color(rgb=(0, 255, 100))
            Rectangle(pos=self.rect_pos, size=self.rect_size)
            PopMatrix()

    def deflect_ball(self, ball):
        if self.collide_ball(ball):
            if not ball.collided[self]:
                vx, vy = ball.velocity
                if self.angle == 135:
                    ball.velocity = Vector(-vx, vy).rotate(90)
                if self.angle == 225:
                    ball.velocity = Vector(-vx, vy).rotate(270)
                if self.angle == 315:
                    ball.velocity = Vector(-vx, vy).rotate(90)
                ball.collided[self] = True
        else:
            ball.collided[self] = False

    def on_touch_up(self, touch):
        if self.collide_point(*touch.pos):
            self.rotate()
            print(self.angle)

    def collide_ball(self, ball):
        # get vector from center of rect to the ball
        to_ball = Vector((ball.x - self.rotate_origin_x), (ball.y - self.rotate_origin_y))

        # get x and y coordinates of above vector in rotated system
        x = to_ball.dot(self.rot_x_dir)  # along rect width
        y = to_ball.dot(self.rot_y_dir)  # along rect height

        # test for collision
        if x < -self.rect_width / 2 - ball.size[0] / 2:
            return False
        if x > self.rect_width / 2 + ball.size[0] / 2:
            return False
        if y < -self.rect_height / 2 - ball.size[1] / 2:
            return False
        if y > self.rect_height / 2 + ball.size[1] / 2:
            return False
        return True

class Object16(Widget):
    def __init__(self, *args, **kwargs):
        Widget.__init__(self, *args, **kwargs)
        self.rect_pos_x = 530
        self.rect_pos_y = 300
        self.rect_pos = self.rect_pos_x, self.rect_pos_y
        self.rect_width = 150
        self.rect_height = 15
        self.rect_size = self.rect_width, self.rect_height
        self.rotate_origin_x = self.rect_pos_x + self.rect_width / 2
        self.rotate_origin_y = self.rect_pos_y + self.rect_height / 2
        self.rotate_origin = self.rotate_origin_x, self.rotate_origin_y
        self.angle = 135
        self.rot_x_dir = Vector(1, 0).rotate(self.angle)
        self.rot_y_dir = Vector(0, 1).rotate(self.angle)
        print('rect 16')
        with self.canvas:
            PushMatrix()
            Rotate(origin=self.rotate_origin, angle=self.angle)
            Color(rgb=(0,1,1))
            Rectangle(pos=self.rect_pos, size=self.rect_size)
            PopMatrix()

    def rotate(self):
        self.canvas.clear()
        self.angle += 90
        if (self.angle > 315):
            self.angle = 225
        self.rot_x_dir = Vector(1, 0).rotate(self.angle)
        self.rot_y_dir = Vector(0, 1).rotate(self.angle)
        with self.canvas:
            PushMatrix()
            self.rot = Rotate(origin=self.rotate_origin, angle=self.angle)
            Color(rgb=(0, 1, 1))
            Rectangle(pos=self.rect_pos, size=self.rect_size)
            PopMatrix()

    def deflect_ball(self, ball):
        if self.collide_ball(ball):
            if not ball.collided[self]:
                vx, vy = ball.velocity
                if self.angle == 135:
                    ball.velocity = Vector(-vx, vy).rotate(90)
                if self.angle == 225:
                    ball.velocity = Vector(-vx, vy).rotate(270)
                if self.angle == 315:
                    ball.velocity = Vector(-vx, vy).rotate(90)
                ball.collided[self] = True
        else:
            ball.collided[self] = False

    def on_touch_up(self, touch):
        if self.collide_point(*touch.pos):
            self.rotate()
            print(self.angle)

    def collide_ball(self, ball):
        # get vector from center of rect to the ball
        to_ball = Vector((ball.x - self.rotate_origin_x), (ball.y - self.rotate_origin_y))

        # get x and y coordinates of above vector in rotated system
        x = to_ball.dot(self.rot_x_dir)  # along rect width
        y = to_ball.dot(self.rot_y_dir)  # along rect height

        # test for collision
        if x < -self.rect_width / 2 - ball.size[0] / 2:
            return False
        if x > self.rect_width / 2 + ball.size[0] / 2:
            return False
        if y < -self.rect_height / 2 - ball.size[1] / 2:
            return False
        if y > self.rect_height / 2 + ball.size[1] / 2:
            return False
        return True

class Object17(Widget):
    def __init__(self, *args, **kwargs):
        Widget.__init__(self, *args, **kwargs)
        self.rect_pos_x = 530
        self.rect_pos_y = 460
        self.rect_pos = self.rect_pos_x, self.rect_pos_y
        self.rect_width = 150
        self.rect_height = 15
        self.rect_size = self.rect_width, self.rect_height
        self.rotate_origin_x = self.rect_pos_x + self.rect_width / 2
        self.rotate_origin_y = self.rect_pos_y + self.rect_height / 2
        self.rotate_origin = self.rotate_origin_x, self.rotate_origin_y
        self.angle = 225
        self.rot_x_dir = Vector(1, 0).rotate(self.angle)
        self.rot_y_dir = Vector(0, 1).rotate(self.angle)
        print('rect 17')
        with self.canvas:
            PushMatrix()
            Rotate(origin=self.rotate_origin, angle=self.angle)
            Color(rgb=(0,1,1))
            Rectangle(pos=self.rect_pos, size=self.rect_size)
            PopMatrix()

    def rotate(self):
        self.canvas.clear()
        self.angle += 90
        if (self.angle > 315):
            self.angle = 225
        self.rot_x_dir = Vector(1, 0).rotate(self.angle)
        self.rot_y_dir = Vector(0, 1).rotate(self.angle)
        with self.canvas:
            PushMatrix()
            self.rot = Rotate(origin=self.rotate_origin, angle=self.angle)
            Color(rgb=(0, 255, 100))
            Rectangle(pos=self.rect_pos, size=self.rect_size)
            PopMatrix()

    def deflect_ball(self, ball):
        if self.collide_ball(ball):
            if not ball.collided[self]:
                vx, vy = ball.velocity
                if self.angle == 135:
                    ball.velocity = Vector(-vx, vy).rotate(90)
                if self.angle == 225:
                    ball.velocity = Vector(-vx, vy).rotate(270)
                if self.angle == 315:
                    ball.velocity = Vector(-vx, vy).rotate(90)
                ball.collided[self] = True
        else:
            ball.collided[self] = False

    def on_touch_up(self, touch):
        if self.collide_point(*touch.pos):
            self.rotate()
            print(self.angle)

    def collide_ball(self, ball):
        # get vector from center of rect to the ball
        to_ball = Vector((ball.x - self.rotate_origin_x), (ball.y - self.rotate_origin_y))

        # get x and y coordinates of above vector in rotated system
        x = to_ball.dot(self.rot_x_dir)  # along rect width
        y = to_ball.dot(self.rot_y_dir)  # along rect height

        # test for collision
        if x < -self.rect_width / 2 - ball.size[0] / 2:
            return False
        if x > self.rect_width / 2 + ball.size[0] / 2:
            return False
        if y < -self.rect_height / 2 - ball.size[1] / 2:
            return False
        if y > self.rect_height / 2 + ball.size[1] / 2:
            return False
        return True

class Stage_6(Widget):
    ball = ObjectProperty(None)
    object14 = ObjectProperty(None)
    object15 = ObjectProperty(None)
    object16 = ObjectProperty(None)
    object17 = ObjectProperty(None)

    def start(self):
        Clock.schedule_interval(self.update, 1.0 / 60.0)
        self.ball.collided[self.object14] = False
        self.ball.collided[self.object15] = False
        self.ball.collided[self.object16] = False
        self.ball.collided[self.object17] = False

    def home(self):
        sm.current = 'P'

    def stage(self):
        sm.current = 'recycleview'

    def serve_ball(self, vel=(6, 0)):
        Clock.unschedule(self.update)
        self.ball.center = 60, 480
        self.ball.velocity = vel
        print('served')

    def update(self, dt):
        self.ball.move()
        self.object14.deflect_ball(self.ball)
        self.object15.deflect_ball(self.ball)
        self.object16.deflect_ball(self.ball)
        self.object17.deflect_ball(self.ball)

        if (self.ball.y < 350) and (self.ball.x > 800):
            self.ball.velocity_y = 0
            Clock.unschedule(self.update)
            print('tested')
            sm.current = 'stage comp'
            self.serve_ball()

        if (self.ball.x>750)and (self.ball.y> 300) or (self.ball.x< -20) or (self.ball.y>600):
            print('Up')
            Clock.unschedule(self.update)
            sm.current = 'loss'
            self.serve_ball()

class Object18(Widget):
    def __init__(self, *args, **kwargs):
        Widget.__init__(self, *args, **kwargs)
        self.rect_pos_x = 320
        self.rect_pos_y = 460
        self.rect_pos = self.rect_pos_x, self.rect_pos_y
        self.rect_width = 150
        self.rect_height = 15
        self.rect_size = self.rect_width, self.rect_height
        self.rotate_origin_x = self.rect_pos_x + self.rect_width / 2
        self.rotate_origin_y = self.rect_pos_y + self.rect_height / 2
        self.rotate_origin = self.rotate_origin_x, self.rotate_origin_y
        self.angle = 225
        self.rot_x_dir = Vector(1, 0).rotate(self.angle)
        self.rot_y_dir = Vector(0, 1).rotate(self.angle)
        print('rect 18')
        with self.canvas:
            PushMatrix()
            Rotate(origin=self.rotate_origin, angle=self.angle)
            Color(rgb=(0,197,68))
            Rectangle(pos=self.rect_pos, size=self.rect_size)
            PopMatrix()

    def rotate(self):
        self.canvas.clear()
        self.angle += 90
        if (self.angle > 315):
            self.angle = 225
        self.rot_x_dir = Vector(1, 0).rotate(self.angle)
        self.rot_y_dir = Vector(0, 1).rotate(self.angle)
        with self.canvas:
            PushMatrix()
            self.rot = Rotate(origin=self.rotate_origin, angle=self.angle)
            Color(rgb=(0, 255, 100))
            Rectangle(pos=self.rect_pos, size=self.rect_size)
            PopMatrix()

    def deflect_ball(self, ball):
        if self.collide_ball(ball):
            if not ball.collided[self]:
                vx, vy = ball.velocity
                if self.angle == 135:
                    ball.velocity = Vector(-vx, vy).rotate(90)
                if self.angle == 225:
                    ball.velocity = Vector(-vx, vy).rotate(270)
                if self.angle == 315:
                    ball.velocity = Vector(-vx, vy).rotate(90)
                print(ball.collided)
                ball.collided[self] = True
        else:
            ball.collided[self] = False

    def on_touch_up(self, touch):
        if self.collide_point(*touch.pos):
            self.rotate()
            print(self.angle)

    def collide_ball(self, ball):
        # get vector from center of rect to the ball
        to_ball = Vector((ball.x - self.rotate_origin_x), (ball.y - self.rotate_origin_y))

        # get x and y coordinates of above vector in rotated system
        x = to_ball.dot(self.rot_x_dir)  # along rect width
        y = to_ball.dot(self.rot_y_dir)  # along rect height

        # test for collision
        if x < -self.rect_width / 2 - ball.size[0] / 2:
            return False
        if x > self.rect_width / 2 + ball.size[0] / 2:
            return False
        if y < -self.rect_height / 2 - ball.size[1] / 2:
            return False
        if y > self.rect_height / 2 + ball.size[1] / 2:
            return False
        return True

class Object19(Widget):
    def __init__(self, *args, **kwargs):
        Widget.__init__(self, *args, **kwargs)
        self.rect_pos_x = 320
        self.rect_pos_y = 160
        self.rect_pos = self.rect_pos_x, self.rect_pos_y
        self.rect_width = 150
        self.rect_height = 15
        self.rect_size = self.rect_width, self.rect_height
        self.rotate_origin_x = self.rect_pos_x + self.rect_width / 2
        self.rotate_origin_y = self.rect_pos_y + self.rect_height / 2
        self.rotate_origin = self.rotate_origin_x, self.rotate_origin_y
        self.angle = 0
        self.rot_x_dir = Vector(1, 0).rotate(self.angle)
        self.rot_y_dir = Vector(0, 1).rotate(self.angle)
        print('rect 19')
        with self.canvas:
            PushMatrix()
            Rotate(origin=self.rotate_origin, angle=self.angle)
            Color(rgb=(0,1,1))
            Rectangle(pos=self.rect_pos, size=self.rect_size)
            PopMatrix()

    def rotate(self):
        self.canvas.clear()
        self.angle += 90
        if (self.angle > 315):
            self.angle = 225
        self.rot_x_dir = Vector(1, 0).rotate(self.angle)
        self.rot_y_dir = Vector(0, 1).rotate(self.angle)
        with self.canvas:
            PushMatrix()
            self.rot = Rotate(origin=self.rotate_origin, angle=self.angle)
            Color(rgb=(0, 255, 100))
            Rectangle(pos=self.rect_pos, size=self.rect_size)
            PopMatrix()

    def deflect_ball(self, ball):
        if self.collide_ball(ball):
            if ball.collided[self] is False:
                vx, vy = ball.velocity
                if self.angle == 0:
                    ball.velocity = Vector(-vx, vy).rotate(180)
                if self.angle == 225:
                    ball.velocity = Vector(-vx, vy).rotate(270)
                if self.angle == 315:
                    ball.velocity = Vector(-vx, vy).rotate(90)
                print(ball.collided)
                ball.collided[self] = True

        else:
            ball.collided[self] = False

   # def on_touch_up(self, touch):
    #    if self.collide_point(*touch.pos):
     #       self.rotate()
      #      print(self.angle)

    def collide_ball(self, ball):
        # get vector from center of rect to the ball
        to_ball = Vector((ball.x - self.rotate_origin_x), (ball.y - self.rotate_origin_y))

        # get x and y coordinates of above vector in rotated system
        x = to_ball.dot(self.rot_x_dir)  # along rect width
        y = to_ball.dot(self.rot_y_dir)  # along rect height

        # test for collision
        if x < -self.rect_width / 2 - ball.size[0] / 2:
            return False
        if x > self.rect_width / 2 + ball.size[0] / 2:
            return False
        if y < -self.rect_height / 2 - ball.size[1] / 2:
            return False
        if y > self.rect_height / 2 + ball.size[1] / 2:
            return False
        return True

class Stage_7(Widget):
    ball = ObjectProperty(None)
    object18 = ObjectProperty(None)
    object19 = ObjectProperty(None)

    def start(self):
        Clock.schedule_interval(self.update, 1.0 / 60.0)
        self.ball.collided[self.object19] = False
        self.ball.collided[self.object18] = False

    def home(self):
        sm.current = 'P'

    def stage(self):
        sm.current = 'recycleview'

    def serve_ball(self, vel=(6, 0)):
        self.ball.center = 60, 475
        self.ball.velocity = vel
        Clock.unschedule(self.update)
        print('served')

    def update(self, dt):
        self.ball.move()
        self.object18.deflect_ball(self.ball)
        self.object19.deflect_ball(self.ball)

        if (self.ball.x > 830):
           # self.ball.velocity_y *= -1
            self.ball.velocity_y = 0
            #show = True
            #if self.ball.y >= 49:
            Clock.unschedule(self.update)
            print('tested')
            #self.show_p()
            sm.current = 'stage comp'
           # print('Down')
            self.serve_ball()

        if (self.ball.top > self.top+100) or (self.ball.x < -5) :
            Clock.unschedule(self.update)
            sm.current = 'loss'
            self.serve_ball()


class P(FloatLayout):
    pass

class Manager(ScreenManager):
    pass

def show_popup():
    show = P()
    popupWindow = Popup(title="Stage Completed", content=show, size_hint=(None, None), size=(400, 400), auto_dismiss = False)
    popupWindow.open()

sm = Manager()

class ScreensApp(App):
    def build(self):
        self.settings_cls = SettingsWithSidebar
        return sm
    def build_config(self, config):
        pass

if __name__ == '__main__':
    ScreensApp().run()