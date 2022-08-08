##Libraries
import csv
import requests

from bs4 import BeautifulSoup

##list to containing pages links
list_of_Pages_Links = []
list_of_Pages_Data_Links = []

##links with for all pages
def Retrive_Main_Pages(url):
  for i in range(1,23):
    Link_Page = url.format(i)
    list_of_Pages_Links.append(Link_Page)




##getting html soup
def get_soup(url):
    res = requests.get(url)
    return BeautifulSoup(res.text, 'html.parser')




##getting links from each html soup and saving it in a list
def Retrive_Data_Pages():
  for link in list_of_Pages_Links:
    soup = get_soup(link)
    for ull in soup.select('.page-course-listing-entry.university a'):
      list_of_Pages_Data_Links.append(ull.get("href"))




##getting data uni name from links in list
def Retrive_Data():
  with open('links.csv', 'w') as f:
        writer = csv.writer(f)
        for i in range(len(list_of_Pages_Data_Links)):
          soup = get_soup(list_of_Pages_Data_Links[i])
          #university_Name = soup.select('.headlines')
          if soup.select_one('.headlines h1') is not None:
            university_Name = soup.select_one('.headlines h1').text
            #tile = soup.find('.simple-inline-table-cell.value div').text
            print(university_Name)
            writer.writerow([university_Name])
          else:
            university_Name = None




def main():
    Retrive_Main_Pages('https://studieren.de/hochschulliste.t-0.filter-3.s-{}.html')
    Retrive_Data_Pages()
    Retrive_Data()
    print(len(list_of_Pages_Data_Links))


if __name__ == '__main__':
    main()