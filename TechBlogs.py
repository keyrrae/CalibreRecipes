from calibre.web.feeds.news import BasicNewsRecipe

class XuansCollection(BasicNewsRecipe):
    title          = u"Tech Blogs"
    oldest_article = 7
    max_articles_per_feed = 20
    auto_cleanup = True
    no_stylesheets = True
    language = 'en'

    __author__ = "Xuan Wang"
    #INDEX = 'http://www.economist.com/printedition'

    use_embedded_content = False
    remove_empty_feeds = True
    description = ('A personal collection of essays fetched from the Internet, concerning art, literature, science, and book reviews')

    extra_css = 'body { font-family: verdana, helvetica, sans-serif; } \
                 .introduction, .first { font-weight: bold; } \
                 .cross-head { font-weight: bold; font-size: 125%; } \
                 .cap, .caption { display: block; font-size: 80%; font-style: italic; } \
                 .cap, .caption, .caption img, .caption span { display: block; text-align: center; margin: 5px auto; } \
                 .byl, .byd, .byline img, .byline-name, .byline-title, .author-name, .author-position, \
                    .correspondent-portrait img, .byline-lead-in, .name, .bbc-role { display: block; \
                    text-align: center; font-size: 80%; font-style: italic; margin: 1px auto; } \
                 .story-date, .published { font-size: 80%; } \
                 table { width: 100%; } \
                 td img { display: block; margin: 5px auto; } \
                 ul { padding-top: 10px; } \
                 ol { padding-top: 10px; } \
                 li { padding-top: 5px; padding-bottom: 5px; } \
                 h1 { text-align: center; font-size: 175%; font-weight: bold; } \
                 h2 { text-align: center; font-size: 150%; font-weight: bold; } \
                 h3 { text-align: center; font-size: 125%; font-weight: bold; } \
                 h4, h5, h6 { text-align: center; font-size: 100%; font-weight: bold; }'

    feeds= [(u'',u''),
            (u'Lucumr',u'http://www.devtacular.com/utilities/atomtorss/?url=http%3a%2f%2flucumr.pocoo.org%2ffeed.atom'),
            (u'Planet Python','http://planetpython.org/rss20.xml'),
            (u'Edwin Chen - Clear and Practical Examples of Data Analyses',u'http://blog.echen.me/feeds/all.rss.xml'),
            (u'John Langford - Machine Learning',u'http://hunch.net/?feed=rss2'),
            (u'FastML',u'http://fastml.com/atom.xml')]
            #(u'R-bloggers',u'')]
            #(u'',u''),
            #(u'',u''),
            #(u'',u''),]

    def get_cover_url(self):
        #cover_url = 'http://www.aldaily.com/wp-content/themes/aldaily/images/header.gif'
        cover_url = 'http://img3.douban.com/view/photo/photo/public/p2192928273.jpg'
        #soup = self.index_to_soup('http://www.lrb.co.uk/')
        #cover_item = soup.find('p',attrs={'class':'cover'})
        #if cover_item:
        #   cover_url = cover_item.a.img['src']
        return cover_url
