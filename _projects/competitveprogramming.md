---
layout: page
title: Competitive Programming
---

One large interest I have is competitive programming. I find it very fun to challenge myself by solving algorithmic problems under time pressure.


Here is a list of yearly programming competitions open to everyone. Some consists of multiple competitions like qualifiers and finals. In those cases the start month is the month of the first qualifier.


<table class="table"> 
<tr>
<th> Name </th> <th> Start Month </th> <th> Type </th> <th> Tags </th>
</tr>
{% for comp in site.data.competitions %}
    <tr>
        <td> <a href="{{comp.url}}">{{ comp.name }}</a> </td>
        <td> {{ comp.month }} </td>
        <td>{{ comp.type }} </td>
        <td> 
        {% for tag in comp.tags %} 
            {% if forloop.first != true %}
                <span>, </span> 
            {% endif %} 
            <span style="padding:2px;border-radius:5px;background:#FF5050;"> {{ tag }} </span> 
        {% endfor %} 
        </td>
    </tr>
{% endfor %}
</table>

For a very up to date list of upcoming competitions, including almost everything, visit [https://clist.by/](https://clist.by/).

One becomes a lot better by practicing. If you are very new to this I suggest you go to [open.kattis.com](https://open.kattis.com/problems?order=problem_difficulty), and start solving some problems ordered by difficulty.

Most competitions are quite friendly to beginners, starting with solvable problems for newcomers, but some are extra friendly, which I have marked with the `beginner`-tag in the table above.

### Resources
Also, there are a lot of resources online where you can practice. Some also hosts weekly or even hourly competitions, where you can test your skills.

- [Kattis](https://open.kattis.com/)
- [Code Forces](https://codeforces.com/)
- [AtCoder](https://atcoder.jp/)
- [Code Chef](https://codechef.com)
- [Project Euler](https://projecteuler.net/)

### Hall of fame:

These contests are discontinued, but I enjoyed them very much when they still existed. I hope some of them will come back!

- [Distributed Google Code Jam](https://codingcompetitions.withgoogle.com/past-competitions/distributed)
- [Internet Problem Solving Contest](https://ipsc.ksp.sk/)

