# Ranscombe Holiday Cottage

This repository contains the source code for the website of Ranscombe Holiday Cottage, which is a self-catering cottage in Devon.

The site is hosted on Github pages.

All you need to do to edit the site is to use ```git clone``` to download the code, edit it as you wish and then push it back to Github with ```git push```.

I tend to push the code to Github using HTTP, and enter a password, rather than using SSH. Github will not allow the same SSH key to be used for multiple accounts. I work with multiple websites, each in their own Github account. There is probably some way to use multiple SSH keys, but it is less trouble to just type the password.

All the assets are hosted in one place, except the video on the home page, which is hosted on Youtube. I tried hosting the video on Github Pages with the rest, using an HTML <video> tag, but it was stuttery. I think Youtube have fancy software that can deliver the right quality for the connection. Or perhaps Github Pages is just not very good and can't cope with large files.

# Code structure

There is an HTML document for each page. All the CSS styles are in 'styles.css'. The site is handcoded HTML, CSS and Javascript.

The Javascript is for the automatic slideshow at the top of the main page.

Most of the site is images.

# Fonts

The site uses two web fonts from Google Fonts. It was found that loading them from Google took a long time on a slow connection, so I downloaded the font style files and the woff files they link to, and hosted them with the site, in the 'fonts' directory.
