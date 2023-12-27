# the mcdonald's sage

Every so often (a few times per year), the fast food chain McDonald's releases a simple game to play and win some prices. These games are a copy of an existing game with a McDonald's twist.
And almost every time I try to program a bot to beat the game. This isn't so much for the prices, but more for the challenge.
I do this by using Vysor to control my phone from my laptop, and the python libraries mss and pyautogui to grab a screenshot and control the mouse. It is very important to set the pyautogui pause default to 0.

```
import pyautogui
pyautogui.PAUSE = 0
```

Fastest way to grab a screenshot with python:
```
with mss() as sct:
    monitor = {"top": TOP/2, "left": LEFT/2,
               "width": WIDTH/2, "height": HEIGHT/2}
    screenshot = np.array(sct.grab(monitor))
```

## big mac game

## flappy wacko

## keeping up
Dec 2022
[GitHub](https://github.com/Arno1235/McDo_KeepingUp)

In this game the goal is to keep the Christmas ball high by clicking on it. If you click on the left side of the ball it will move to the right, clicking on the bottom will make it jump up.
After some testing, I found that I could quickly locate the Christmas ball using Hough Circles Detection. After locating the Christmas ball, the bot clicks using the formula below.

```
x_og, y_og, r = circle

y = y_og + (y_og - (HEIGHT/2)) * 2*r/HEIGHT

x = x_og + (x_og - WIDTH/2) * 2*r/WIDTH

pyautogui.moveTo((x+LEFT)/2, (y+TOP)/2)
pyautogui.click()
```

This formula simply says that the further the ball is from the center of the screen the further it should click from the center of the bauble.

![](https://raw.githubusercontent.com/Arno1235/Arno1235.github.io/main/images/mcdo_keepingup.png "screeshot keeping up")

## burger building

## candy crush


