---
layout: post
title:  "Glucose Errors"
date:   2019-03-12 11:00:00 +0100
img: /img/2019/20190312-real-glucose.jpg

---

I've been working on a side project for quite some time now - [Erbil](https://github.com/exoji2e/Erbil). It's an app that reads glucose values off an nfc sensor hat I have on my arm. The manufacturer of the sensors also have an app, but my conclusion is that they are neither very good with software development nor fitting data to reality.

Actually the nfc sensor only measures the glucose in the tissue fluid and not in the blood directly. It is known to be delayed in time compared to the blood. Also I have noticed that what is reported from the sensor is in some arbitrary unit, so there is a problem of translating from that unit to the standard glucose unit.

As a diabetic I control my blood sugar(glucose) value by injecting insulin. In Europe the unit `mmol/L` is used, and the goal is to have a glucose value between `4.0` and `9.0`. The manufacturer seems to not care what they show to me if I'm outside this boundary. If I'm at `3.8` their app frequently shows me `3.0`, and if I'm at `12.0` the app can show anything between `13.0` and `17.0`. It seems that they really don't want their app to show a value within the goal when I'm outside the goal, but don't care very much about the accuracy (how much outside the goal I am). This is absurd to me. If I'm too low I need to eat sugar, and I need to know how much sugar to eat. If I'm too high I need to take insulin, and I need to know how much insulin I should take.

Have a look at my values this morning:

![freestyle](/img/2019/20190312-freestyle.jpg){: width="49%"}
![erbil](/img/2019/20190312-erbil.jpg){: width="49%"}

The left image is the manufacturer's app, it says I'm at `17.8`, while my app says I'm at `10.3` - going down. If my app is correct I'd not take any insulin to compensate, but If the freestyle-app is correct I'd take at least `3.0` units of compensation insulin. Note that the time-axis is not over the same time interval in the two screen shots.

Luckily I have a real blood-test device, let's see what my real glucose value is:

![real-value](/img/2019/20190312-real-glucose.jpg){: width="100%"}

Notice: I have not set the time on the manual device in a long time, so it has drifted a bit, but the image is taken at the same time as the screen shots.

This is indeed quite dangerous. If I would have trusted the freestyle app and taken extra insulin I would have became very low.

Now, half an hour later when I'm finished with his blog post the apps show quite similar values again, when I'm inside the goal:

![freestyle-30](/img/2019/20190312-freestyle-30.jpg){: width="49%"}
![erbil-30](/img/2019/20190312-erbil-30.jpg){: width="49%"}

The `17+`-values were just guesses from the freestyle app, since they are now removed in the plot. However it's quite clear that the freestyle app shows worse values than they really are, probably to be on the "safe side" - not showing values within the goal when you are outside. However that comes with the unsafe disadvantage of showing values really off when outside the goal.



