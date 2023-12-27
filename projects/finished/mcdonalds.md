# the mcdonald's sage

Every so often (a few times per year), the fast food chain McDonald's releases a simple game to play and win some prizes. These games are a copy of an existing game with a McDonald's twist.
And almost every time I try to program a bot to beat the game. This isn't so much for the prices, but more for the challenge.

## big mac game
31 Aug 2023

## flappy wacko
6 Jun 2023

## keeping up
[git](https://github.com/Arno1235/McDo_KeepingUp)
In this game the goal is to keep the Christmas ball high by clicking on it. If you click on the left side of the ball it will move to the right, clicking on the bottom of the ball will make it jump up.
After some testing, I found that I could quickly locate the Christmas bauble using Hough Circles Detection. After locating the Christmas bauble, I click using the formula below.

```
    x_og, y_og, r = circle

    y = y_og + (y_og - (HEIGHT/2)) * 2*r/HEIGHT

    x = x_og + (x_og - WIDTH/2) * 2*r/WIDTH

    pyautogui.moveTo((x+LEFT)/2, (y+TOP)/2)
    pyautogui.click()
```

This formula simply says that the further the ball is from the center of the screen the further it should click from the center of the bauble.

## burger building

## candy crush


