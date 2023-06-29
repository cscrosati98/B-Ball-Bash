import time
import thumby
import math
from random import randrange
# BITMAP: width: 32, height: 32
basher_arr = bytearray([192,192,192,128,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
           1,3,7,15,31,62,124,248,48,160,254,130,130,146,130,130,130,146,130,130,254,0,0,0,0,0,0,0,0,0,0,0,
           0,0,0,0,0,0,0,1,2,2,255,67,194,131,130,131,130,131,130,67,255,0,0,0,0,0,0,0,0,0,0,0,
           0,0,0,0,0,0,0,0,0,0,255,144,159,144,160,192,0,0,255,144,159,144,160,192,0,0,0,0,0,0,0,0])
basher = thumby.Sprite(32, 32, basher_arr)

basher_hit1_arr = bytearray([0,0,0,0,0,0,0,0,128,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
           0,0,96,112,240,228,194,201,36,160,254,130,130,18,130,130,186,42,58,130,254,0,0,0,0,0,0,0,0,0,0,0,
           0,0,0,0,0,1,1,1,2,2,255,67,202,136,135,135,135,131,128,67,255,0,0,0,0,0,0,0,0,0,0,0,
           0,0,0,0,0,0,0,0,0,0,255,144,159,144,160,192,0,0,255,144,159,144,160,192,0,0,0,0,0,0,0,0])
basher_hit1 = thumby.Sprite(32, 32, basher_hit1_arr)

# BITMAP: width: 32, height: 32
basher_hit_bad_arr = bytearray([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
           0,254,130,58,42,58,2,58,170,186,130,254,128,192,192,192,192,192,192,192,192,192,0,0,0,0,0,0,0,0,0,0,
           0,255,67,193,129,132,132,132,128,192,67,255,3,7,7,7,7,7,7,7,7,7,0,0,0,0,0,0,0,0,0,0,
           0,255,144,159,144,160,192,0,0,255,144,159,144,160,192,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
basher_hit_bad=thumby.Sprite(32, 32, basher_hit_bad_arr)

bat_arr = bytearray([31,31,31,31,31,31,31,31,31,31,31])
bat=thumby.Sprite(11, 5, bat_arr)

basher_hit_good_arr = bytearray([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
           0,254,130,58,42,58,2,58,170,186,130,254,128,192,192,192,192,192,192,192,192,192,0,0,0,0,0,0,0,0,0,0,
           0,255,67,193,129,132,132,132,128,192,67,255,3,7,7,7,7,7,7,7,7,7,0,0,0,0,0,0,0,0,0,0,
           0,255,144,159,144,160,192,0,0,255,144,159,144,160,192,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
basher_hit_good=thumby.Sprite(32, 32, basher_hit_good_arr)
# BITMAP: width: 8, height: 8
ball_arr = bytearray([0,28,62,62,62,28,0])
ball = thumby.Sprite(7,7, ball_arr)
# Set the FPS (without this call, the default fps is 30)
basher.x = 0
basher.y = 8
basher_hit1.x = 0
basher_hit1.y = 8
basher_hit_good.x = 9
basher_hit_good.y = 8
bat.x=100
bat.y=100
thumby.display.setFPS(40)
noball=True
swing=0
#thumby.display.setFont("/lib/font5x7.bin", 5, 7, 1)
thumby.display.setFont("/lib/font3x5.bin", 3, 5, 1)
#w 72
#h 40
smack=False
great_hit=False
good_hit=False
miss=False
gr_count=0
gd_count=0
miss_count=0
banner=0
disp=""
count=0
while(1):
    t0 = time.ticks_ms()   # Get time (ms)
    thumby.display.fill(0) # Fill canvas to black
    if((not noball)and(ball.y<=40)and(ball.y>=-21)):
        if(not smack):
            ball.x=int((ball_throw_h*100/((t0-ball_start)))+ball_throw_off)
            ball.y=int((t0-ball_start)/ball_throw_v)
        else:
            ball.x=ball.x+2
            ball.y=ball.y-3
    elif(noball):
        noball=False
        ball_throw_h=randrange(68,88)
        ball_throw_v=randrange(35,55)
        ball_throw_off=randrange(20,40)
        ball.x=100#thumby.display.width
        ball.y=-20#thumby.display.height
        ball_start=t0
    else:
        noball=True
        smack=False
    # Center the sprite using screen and bitmap dimensions and apply bob offset
        # Display the bitmap using bitmap data, position, and bitmap dimensions
    if(not swing):
        if(thumby.buttonA.justPressed()|thumby.buttonB.justPressed()):
            swing=1
            thumby.display.drawSprite(basher_hit1)
            count=0
        else:
            thumby.display.drawSprite(basher)
    else:
        bat.x=31
        bat.y=22
        thumby.display.drawSprite(basher_hit_good)
        if((ball.y+3>=22) and (ball.x+3<=41) and (ball.y+3<=27)):
            thumby.audio.play(440, 300)
            swing=10
            if((ball.y+3>=24) and (ball.x+3<=40) and (ball.y+3<=25)):
                banner=3
                great_hit=True
                miss=False
            else:
                banner=2
                good_hit=True
                miss=False
            smack=True
        else:
            miss=True
        if(swing>=10):
            swing=0
            bat.x=100
            bat.y=100
            if(miss):
                banner=1
                miss_count=miss_count+1
                thumby.audio.play(180, 300)
        else:
            swing=swing+1
    if(smack):
        if(great_hit):
            gr_count=gr_count+1
        if(good_hit):
            gd_count=gd_count+1
    if(banner==3):
        disp="GREAT HIT"
    if(banner==2):
        disp="GOOD HIT"
    if(banner==1):
        disp="MISS"
    if(banner==0):
        disp=""
    count+1
    if (count==80):
        banner=0
        count=0
    great_hit=False
    good_hit=False
    miss=False
    thumby.display.drawText(disp, 5, 5, 1)
    thumby.display.drawSprite(ball)
    thumby.display.drawSprite(bat)

    thumby.display.drawText("GR:"+str(gr_count), 55, 21, 1)
    thumby.display.drawText("GD:"+str(gd_count), 55, 28, 1)
    thumby.display.drawText("MI:"+str(miss_count), 55, 35, 1)
    thumby.display.update()
