Source of my [personal blog](http://solring.github.io) built by Python Pelican site-gen.
Theme: [Flex](https://github.com/alexandrevicenzi/Flex)

# Build

Based on the method mentioned in [offical doc](http://docs.getpelican.com/en/3.7.1/install.html)
and [here](https://fedoramagazine.org/make-github-pages-blog-with-pelican/):

1. Prepare submodule which contains the output site.
    1. ```$ git submodule init```
    2. ```$ git submodule update```
2. Prepare the theme
    1. Clone [my theme](https://github.com/solring/Flex).
    2. Modify ```THEME``` in ```pelicanconf.py``` to the path of your theme.
3. Prepare Python environment (if not ready)
    * Linux: the virtualenv env is embedded for convenient, just use it with ```pelican-env/bin/activate```
    * Windows: use Windows virtualenv to build a env and install the required packages in the [doc](http://docs.getpelican.com/en/3.7.1/install.html).
4. Build and run the site
    * Linux: ```$ make publish && make server```
    * Windows: Since the fabric v2 API is not ported yet, use the pelican cmd directly: ```pelican content -s publishconf.py``` and then go to ```output/``` and run the server.

# Write article

The new article should be placed in ```content/```.

For detailed format please refer to [doc](http://docs.getpelican.com/en/3.7.1/content.html)

# Deploy the Site

Go to ```output/``` directory and make sure that it has the remote branch to [github page](https://github.com/solring/solring.github.io) and is up to date. 
(This should be done during the submodule init time.)

Commit and push the updated website after build.
