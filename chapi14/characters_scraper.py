# coding:utf8 

import scrapy 

class BlogSpider(scrapy.Spider): 
  name = 'characerspider' 
  start_urls = ['https://fr.wikipedia.org/wiki/Catégorie:Personnage_d\'animation']

  def parse(self, response):
    for link in response.css('div#mw-pages div.mw-content-ltr li'):
      yield {'character': link.css('a ::text').extract_first()}