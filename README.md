# scrapping-emobile
This article is meant for learning web scraping using various libraries avaialable from Python. If you are good with Python you can refer this article, it is a complete guide started from scratch
consider this situation,

a person wants to print two numbers in a console/terminal in python he/she will use some thing like this,

Hide   Copy Code
print("1 2")
so what do you he/she wants to print about 10 numbers? well, he/she can use looping. ok now we can come to our sitution if a website contains information about a person and you want it in an excel? what do you do? you will copy the info of a person and add his contact info other other stuffs in several rows. what do you do when there are infos about 1000 persons? well you have to code a bot to do this work.

There are various libraries out there available for Python I will try to explain all the important stuffs to become a fully fledged web scrapper.



==========================================

import urllib.request
and type the following code,

Hide   Copy Code
# SWAMI KARUPPASWAMI THUNNAI
import urllib.request
source = urllib.request.urlopen("http://www.codeproject.com")
print(source)

==================================================================
