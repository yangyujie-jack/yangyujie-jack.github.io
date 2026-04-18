---
permalink: /
title: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

I am a Ph.D. student at [Intelligent Driving Lab (iDLab)](http://www.idlab-tsinghua.com/thulab/labweb/), School of Vehicle and Mobility, Tsinghua University, where I am fortunate to be advised by Prof. [Shengbo Eben Li](http://www.svm.tsinghua.edu.cn/essay/80/1812.html) and Prof. [Bo Cheng](http://www.svm.tsinghua.edu.cn/essay/80/1799.html). Prior to that, I received my B.E. degree in Vehicle Engineering from the School of Vehicle and Mobility, Tsinghua University in 2021. My research interests include decision and control of autonomous vehicles and safe reinforcement learning.

<h2 id="news">News</h2>
{% for post in site.posts %}
  {% include archive-single.html %}
{% endfor %}

<h2 id="publications">Publications</h2>
{% for post in site.publications %}
  {% include archive-single.html %}
{% endfor %}

<h2 id="talks">Talks</h2>
{% for post in site.talks %}
  {% include archive-single.html %}
{% endfor %}

<h2 id="teaching">Teaching</h2>
{% for post in site.teaching %}
  {% include archive-single.html %}
{% endfor %}

