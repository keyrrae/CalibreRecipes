from calibre.web.feeds.news import BasicNewsRecipe

class XuansCollection(BasicNewsRecipe):
    title          = u"Xuan's Collection of Book Reviews, Opinions, and Essays"
    oldest_article = 7
    max_articles_per_feed = 20
    auto_cleanup = True
    no_stylesheets = True
    language = 'en'

    __author__ = "Xuan Wang"
    #INDEX = 'http://www.economist.com/printedition'

    use_embedded_content = False
    remove_empty_feeds = True
    description = ('The '
            ' perspective. Best downloaded on Friday mornings (GMT)')

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

    feeds          = [(u'The Smart Set', u'http://thesmartset.com/rss/default.xml'), (u'The New York Review of Books', u'http://feeds.feedburner.com/nybooks'), (u'B&N review', u'http://bnreview.barnesandnoble.com/bnreview/plugins/custom/barnesandnoble/bnreview/rss_full'),(u'LA Review of Books', u'http://lareviewofbooks.org/feed/?ver=2'), (u'Public Books', u'http://www.publicbooks.org/rss'),(u'The Scientist',u'http://www.the-scientist.com/?rss.feed/'),(u"Harper's Magazine",u'http://harpers.org/feed/')]

    def get_cover_url(self):
        #cover_url = 'http://www.aldaily.com/wp-content/themes/aldaily/images/header.gif'
        cover_url = 'http://img3.douban.com/view/photo/photo/public/p2192884675.jpg'
        #soup = self.index_to_soup('http://www.lrb.co.uk/')
        #cover_item = soup.find('p',attrs={'class':'cover'})
        #if cover_item:
        #   cover_url = cover_item.a.img['src']
        return cover_url
