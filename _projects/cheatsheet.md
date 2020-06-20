---
layout: page
title: Cheat sheet
---

Collecting programming related examples of things I find hard to remember

# Linux cli tools

`grep -i -A 1 -B 2 -e "herp"`

- A: # lines after match
- B: # lines before match
- i: ignore case

`grep -r "herp" .`

- r: recursive grep in folder specified.


`find ${path} -name ${name-pattern}`


# Markdown
[Markdown Cheat sheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)


# Java


Extracting exception stack trace as string:

```java
try{

}catch(Exception e) {
    StringWriter sw = new StringWriter();
    PrintWriter pw = new PrintWriter(sw);
    e.printStackTrace(pw);
    String res = sw.toString();
}
```


# Kotlin

MainClass is renamed from Name to NameKt.

```
    set v (echo $argv[1] | cut -f1 -d'.')
    kotlinc "$v".kt
    echo "Running $v"
    kotlin "$v"Kt
```

# Android
List all apps on connected device:

`adb shell pm list packages -f`

