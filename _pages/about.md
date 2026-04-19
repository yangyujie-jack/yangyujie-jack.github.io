---
permalink: /
layout: archive
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

<h2 id="about">About Me</h2>
I am a Ph.D. student at [Intelligent Driving Lab (iDLab)](http://www.idlab-tsinghua.com/thulab/labweb/), School of Vehicle and Mobility, Tsinghua University, where I am fortunate to be advised by Prof. [Shengbo Eben Li](http://www.svm.tsinghua.edu.cn/essay/80/1812.html) and Prof. [Bo Cheng](http://www.svm.tsinghua.edu.cn/essay/80/1799.html). During my Ph.D., I spent wonderful time as a visiting student at Carnegie Mellon University, working with Prof. [Changliu Liu](https://icontrol.ri.cmu.edu/people/changliu.html). Prior to that, I received my B.E. degree from the School of Vehicle and Mobility, Tsinghua University in 2021.

<h2 id="research">Research Interests</h2>
My research lies in safe reinforcement learning theories, algorithms, and applications to autonomous driving and robotics.

<h2 id="news">News</h2>
<ul>
  <li><strong>2026.02</strong> &nbsp; Our paper: <a href="https://ieeexplore.ieee.org/document/11419867">On the Equilibrium between Feasible Zone and Uncertain Model in Safe Exploration</a> is accepted by IEEE T-PAMI!</li>
  <li><strong>2026.01</strong> &nbsp; Our paper: <a href="https://openreview.net/forum?id=BHSSV1nHvU">Breaking safety paradox with feasible dual policy iteration</a> is accepted by ICLR 2026!</li>
</ul>

<h2 id="publications">Selected Publications</h2>
<p>A full list of publications can be found on my <a href="https://scholar.google.com/citations?user=2T7-s0MAAAAJ&hl=en">Google Scholar page</a>.<br>
(* denotes equal contribution)</p>
{% assign sorted_pubs = site.publications | sort: 'collection_order' %}
{% for post in sorted_pubs %}
  {% include archive-single.html %}
{% endfor %}

<!--
<h2 id="talks">Talks</h2>

<h2 id="teaching">Teaching</h2>
{% for post in site.teaching %}
  {% include archive-single.html %}
{% endfor %}
-->

