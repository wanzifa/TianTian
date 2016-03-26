#coding:utf-8
import requests
from bs4 import BeautifulSoup
"""
爬取果壳网小组热帖的科技，人文，生活，娱乐板块热帖各一篇
"""

"""
爬取科技板块热帖第一篇
标题，时间，作者，作者个人主页链接
"""

contents = []
titles = []
times = []
authors = []
author_urls = []
r = requests.get('http://www.guokr.com')
soup = BeautifulSoup(r.content, 'lxml')

def guoke_tech():
    url1 = soup.find_all('div', class_='contents-l')[1].div.ul.li.a['href']
    r1 = requests.get(url1)
    titles.append(soup.find_all('div', class_='contents-l')[1].div.ul.li.a.img['alt'])
    soup1 = BeautifulSoup(r1.content, 'lxml')
    contents.append(soup1.find('div', id='articleContent').prettify())
    times.append(soup1.find('p', class_='gfr').get_text())
    authors.append(soup1.find('p', class_='gfl').a['title'])
    author_urls.append(soup1.find('p', class_='gfl').a['href'])
    #print content
    #print title
    #print time
    #print author
    #print author_url


"""
爬取人文板块热帖第一篇
标题，时间，内容,作者，作者个人主页链接
"""
def guoke_people():
    url2 = soup.find_all('div', class_='contents-r')[1].div.ul.li.a['href']
    r2 = requests.get(url2)
    titles.append(soup.find_all('div', class_='contents-r')[1].div.ul.li.a.img['alt'])
    soup2 = BeautifulSoup(r2.content, 'lxml')
    times.append(soup2.find('p', class_='gfr').get_text())
    contents.append(soup2.find('div', id='articleContent').prettify())
    authors.append(soup2.find('p', class_='gfl').a['title'])
    author_urls.append(soup2.find('p', class_='gfl').a['href'])
#print title
#print time
#print author
#print author_url
#print content

"""
爬取生活板块热帖第一篇
标题，时间，内容，作者，作者个人主页链接
"""
def guoke_life():
    url3  = soup.find_all('div', class_='content')[5].ul.li.a['href']
    r3 = requests.get(url3)
    titles.append(soup.find_all('div', class_='content')[5].ul.li.a.img['alt'])
    soup3 = BeautifulSoup(r3.content, 'lxml')
    times.append(soup3.find('p', class_='gfr').get_text())
    contents.append(soup3.find('div', id='articleContent').prettify())
    authors.append(soup3.find('p', class_='gfl').a['title'])
    author_urls.append(soup3.find('p', class_='gfl').a['href'])
    #print title
    #print time
    #print author
    #print author_url

"""
爬取娱乐板块热帖第一篇
标题，时间，内容，作者，作者个人主页链接
"""
def guoke_happy():
    url4  = soup.find_all('div', class_='content')[7].ul.li.a['href']
    r4 = requests.get(url4)
    titles.append(soup.find_all('div', class_='content')[7].ul.li.a.img['alt'])
    soup4 = BeautifulSoup(r4.content, 'lxml')
    contents.append(soup4.find('div', id='articleContent').prettify())
    times.append(soup4.find('p', class_='gfr').get_text())
    authors.append(soup4.find('p', class_='gfl').a['title'])
    author_urls.append(soup4.find('p', class_='gfl').a['href'])
#print title
#print time
#print author
#print author_url

guoke_tech()
guoke_people()
guoke_life()
guoke_happy()