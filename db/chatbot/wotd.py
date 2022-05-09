from bs4 import BeautifulSoup
import requests

html_text=requests.get('https://www.merriam-webster.com/word-of-the-day').text

soup = BeautifulSoup(html_text,'lxml')
wotd = soup.find("h1").text
definition = soup.find("p").text
definitions = soup.find_all("p")

def wrap_by_word(s, n=6):
    '''returns a string where \\n is inserted between every n words'''
    a = s.split()
    ret = ''
    for i in range(0, len(a), n):
        ret += ' '.join(a[i:i+n]) + '\n'

    return ret

x = wrap_by_word('There is a dog and fox fighting in the park and there is an apple falling down.', 4)
print(x)

f = open("WOTD.txt", "w")
f.write(f'''
{wrap_by_word(definitions[0].text)}

{wrap_by_word(definitions[1].text)}
'''
)
f.close()