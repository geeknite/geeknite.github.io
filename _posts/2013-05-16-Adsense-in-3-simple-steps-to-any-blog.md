---
layout: post
title: 'How to create a site: Add Adsense in 3 simple steps to any blog or page that allows frames'
date: '2013-05-16T13:41:00.000+01:00'
tags:
- adsense
- computing
- google
---


The idea is to use a **frame** to show AdSense from another website so you can show them in your blog page, in wordpress.com even frames are limited so this solution won't work. Basically, we can achieve it in 3 simple steps:

1. Get the AdSense Javascript code If you know how to get the AdSense Javascript, just skip this step. Otherwise, you should enter the AdSense website, click in "My ads" tab, "Content", "Ad units", and create a *new ad unit* , configure the block as you wish, so it is compatible to your site layout and get the code to insert AdSense to your page.

2. Create a free page Searching in Google for a free hosting website service, you can use a page in for example a free blog service like Tumblr, where you can add simple web pages to your blog, this pages can be html so you can add anything, at least I tried with ads.

3. Insert an iFrame in your Blog, this might be the hardest part since it requires some basic [HTML knowledge](https://{{ site.constants[0].wsib }}/html manual/). You should access the manual theme customization and select where you want to insert the ads. Then you have to insert the following code snippet:

        <div class="ads">
            <iframe src="http://youradaddres" width="600" height="100" scrolling="no" frameborder="0">
            </iframe>
        </div>

[![HTML and CSS: Design and Build Websites](https://m.media-amazon.com/images/I/41WznOEKmAL._SL160_.jpg)](<https://www.amazon.com/dp/1118008189?tag={{ site.constants[0].amazon_com }}&linkCode=ogi&th=1&psc=1>)

You should replace "http://youradaddres" with the address of the page you created in the previous step. The width and height parameters should be adjusted for your layout, add some **extra space** to the teoric size of the ad because if it's too adjusted it may create scrolling bars.

~~Also if you want to add ads in your feed you can use **feedburner** to add it automagically :)~~

**Edit:** Since this new year (2013) feedburner has stopped serving ads in feeds so if you are interested in keeping them you should have to look for a custom solution.
