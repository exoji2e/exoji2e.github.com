---
layout: page
title: projects
permalink: /projects/
intopnav: true
---

<div class="row">
{% assign projects = site.projects | sort: "title" %}
{% for project in projects %}
    <div class="col-xs-6 col-sm-4 col-md-4 col-lg-4">
        {% if project.redirect %}
        <div class="project">
            <h1 style="height:60px;" class="project-title" >{{ project.title }}</h1>
            <div class="thumbnail">
                <a href="{{ project.redirect }}" target="_blank">
                {% if project.img %}
                <img class="thumbnail" src="{{ project.img }}"/>
                {% else %}
                <div class="thumbnail blankbox"></div>
                {% endif %}    
                <span>
                    <p>{{ project.description }}</p>
                </span>
                </a>
            </div>
        </div>
        {% else %}

        <div class="project ">
            <h1 class="project-title">{{ project.title }}</h1>
            <div class="thumbnail">
                <a href="{{ site.baseurl }}{{ project.url }}">
                {% if project.img %}
                <img class="thumbnail" src="{{ project.img }}"/>
                {% else %}
                <div class="thumbnail blankbox"></div>
                {% endif %}    
                <span>
                    <p>{{ project.description }}</p>
                </span>
                </a>
            </div>
        </div>

        {% endif %}
    </div>
    {% assign mod4 = forloop.index | modulo:4 %}
    {% assign mod3 = forloop.index | modulo:3 %}
    {% assign mod2 = forloop.index | modulo:2 %}
    {% if mod2 == 0 %}
    <div class="clearfix visible-xs-block"></div>
    <div class="clearfix visible-sm-block"></div>
    {% endif %}
    {% if mod3 == 0 %}
    <div class="clearfix visible-md-block"></div>
    <div class="clearfix visible-lg-block"></div>
    {% endif %}
{% endfor %}
</div>
