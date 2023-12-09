# TV Mount Height Calculator
I never thought I'd need trig again, but here I am. 

### Overview
I needed to mount a TV in my apartment. I have some experience mounting art, and computer monitors, but never TVs.
As a result, I wanted to make sure I mounted it at a proper viewing angle. For instance, if it was perfectly
level with my eyes, the angle would be zero. But is that appropriate / comfortable for a TV bed?

### Approach
In order to answer this question, I did some quick Googling. Turns out the proper angle is anywhere between
0 and 15 degrees. This led me to wondering how I could calculate the height to mount the TV to achieve 
this angle. 

If you think about how you're laying in bed watching tv, the height of the TV above your body can
be calculated doing the following:

`y_a = dist*tan($\theta$)`

However, this isn't the total height of the TV. There's an additional measurement that needs to
be added on, which is how high you are up from the ground. This can be simply added to the above
to get total height

```text
tv_height = dist*tan($\theta$) + height
```

With the above established, all you need to know how high to mount your TV is how far your face is from the TV's wall, 
and how high your face is off the ground while you're sleeping.

### How to Use
This is designed to be interactive from the command line. Simple pass in arguments for `dist` and `height` as shown
below. 

```bash
python3 tv-stuff.py --dist 12 --height 3
```
