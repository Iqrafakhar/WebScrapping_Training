
import scrapy

class ScrapySpider(scrapy.Spider):
    name = 'university'
    allowed_domains = ['studieren.de']
    start_urls = ['https://studieren.de/dresden-international-university.hochschule.t-0.a-2509.html']

    base_url = 'https://studieren.de/hochschulliste.t-0.filter-3.s-{}.html'

    def parse(self, response):
        for i in range(23):
            yield response.follow(self.base_url.format(i), self.parse_university, dont_filter=True)

    def parse_university(self, response):
        for url in response.css('.page-course-listing .item-main-link::attr("href")'):
            yield response.follow(url, self.parse_info, dont_filter=True)

    def parse_info(self, response):
        course = {}
        course = {
        'url' : response.url,
        'School Type' : response.css('.slim::text').get(),
        'School Name': response.css('h1::text').get(),
        'Stadt' : response.css('.label:contains("Stadt")+.value ::text').get() or 'None',
        'Sekretariat' : response.css('.label:contains("Sekretariat")+.value ::text').get() or 'None',
        'Telefon' : response.css('.label:contains("Telefon")+.value ::text').get() or 'None',
        'E-Mail' : response.css('.label:contains("E-Mail")+.value ::text').get() or 'None',
        'Trägerschaft' : response.css('.label:contains("Trägerschaft")+.value ::text').get() or 'None',
        'Gründungsjahr' : response.css('.label:contains("Gründungsjahr")+.value ::text').get() or 'None',
        'Studierende' : response.css('.label:contains("Studierende")+.value ::text').get() or 'None',
        'Internet' : response.css('.label:contains("Internet")+.value ::text').get() or 'None',
        }
        return course

#def main():
    #ScrapySpider.multiple_pages_link()
    #for i in range(1,22):
        #print(ScrapySpider.Multiple_Page_Links[i])

#if __name__ == '__main__':
    #main()