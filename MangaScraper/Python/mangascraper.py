__author__ = 'dfranklin'
import requests
import bs4
import sys

'''
    A linear scraper for mangareader.net
'''

def scrapePage(url):
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text,"lxml")
    next_page = soup.find('span',{'class':'next'}).find('a')
    image = soup.find('img',{'id':'img'})
    # print image.attrs['src']
    # print image.attrs['alt']
    # print next_page.attrs['href']
    save_image(image.attrs['src'], image.attrs['alt'])
    return next_page.attrs['href']

def save_image(url, file_name):
    r = requests.get(url)
    with open(file_name+'.jpg', "wb") as f:
        f.write(r.content)

def can_parse_image(url):
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text)
    image = soup.find('img',{'id':'img'})
    if image:
        return True
    return False

def split_url(url):
     return url.split('/')

def get_last_chapter(url):
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text)
    chapters = [str(x.text) for x in soup.find(id="chapterMenu").find_all('option')]
    return chapters[-1]

def main(argv):
    manga_name = ''
    start_chapter = 1
    end_chapter = -1
    root_url = 'http://www.mangareader.net'
    index_url = ''
    next_page = ''
    if len(sys.argv) < 3:
        print 'Not enough arguments'
        print 'Manga_Name Start_Chapter'
        print 'Manga_Name Start_Chapter End_Chapter'

    else:
        manga_name = sys.argv[1]
        start_chapter = sys.argv[2]
        end_chapter = sys.argv[3]
        index_url = root_url + '/'+ manga_name +'/' + start_chapter
        next_page = scrapePage(index_url)
        current_chapter = split_url(next_page)[-2]
        while(can_parse_image(root_url + next_page)):
            current_chapter = split_url(next_page)[-2]
            print current_chapter + ' ' + next_page
            if current_chapter < end_chapter:
                next_page = scrapePage(root_url + next_page)
            else:
                break

if __name__ == "__main__":
   main(sys.argv[1:])