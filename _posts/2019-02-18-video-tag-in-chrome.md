---
layout: post
title:  "Video tag in Chrome"
date:   2019-02-18 14:40:00 +0100

---

**Update:** There seems to be a problem for me when running the web server locally. Live on github pages both videos seems to work without problems also in Chrome. Tip for tomorrow: preview videos hosted on jekyll with Firefox and not Chrome.

This is mostly a test too see if I just have a local jekyll problem or not.

I found out that including:

```html
<video width="100%" controls>
    <source src="path-to-video.mp4" type="video/mp4" >
    Your browser does not support the video tag.
</video>
```

Displays fine in Firefox, but on Chrome a black screen shows up, or some times half a second of the video gets loaded. I think it might have to do with the `width="100%`.


I recently picked upp picklocking. It's quite fun. Here is a video of me unlocking a test lock with just one tool.

<video width="100%" controls>
    <source src="/vids/20190218-lockpick.mp4" type="video/mp4" >
    Your browser does not support the video tag.
</video>

```html
<video width="100%" controls>
    <source src="/vids/20190218-lockpick.mp4" type="video/mp4" >
    Your browser does not support the video tag.
</video>
```

However maybe it's just a problem with my ruby installation on my mac, since it also creates the following jekyll error:
```
[2019-02-18 14:53:48] ERROR Errno::ECONNRESET: Connection reset by peer @ io_fillbuf - fd:14
	/usr/local/Cellar/ruby/2.6.1/lib/ruby/2.6.0/webrick/httpserver.rb:82:in `eof?'
	/usr/local/Cellar/ruby/2.6.1/lib/ruby/2.6.0/webrick/httpserver.rb:82:in `run'
	/usr/local/Cellar/ruby/2.6.1/lib/ruby/2.6.0/webrick/server.rb:307:in `block in start_thread'
```

I however get these messages both when viewing the video in Firefox and Chrome. Here the video is with it's original size specified.

<video width="640px" controls>
    <source src="/vids/20190218-lockpick.mp4" type="video/mp4" >
    Your browser does not support the video tag.
</video>

```html
<video width="640px" controls>
    <source src="/vids/20190218-lockpick.mp4" type="video/mp4" >
    Your browser does not support the video tag.
</video>
```
