import requests
from bs4 import BeautifulSoup

class GetI(object):
     def __init__(self):
         response = requests.get('https://m.hupu.com/nba')
         con = response.content.decode('utf-8')
         # with open(r'E:\work\hupu.txt', 'w') as f:
         #     f.write(con)
         self._soup = BeautifulSoup(con, 'lxml')

     def get_hot_lines(self):
         hot_lines = []
         hot_count = []
         href = []
         for link in self._soup.find_all(attrs={'class': 'text-list focus'}):
             for link in link.find_all('dd'):
                 if link.find('h2') is not None:
                     hot_lines.append(link.find('h2').get_text())
                     if link.find('span') is not None:
                         hot_count.append(link.find('span').get_text()[1:])
                         if link.find('a') is not None:
                             href.append(link.find('a').get('href'))
         # print(hot_lines)
         # print(hot_count)
         # print(href)

         return hot_lines, hot_count, href

     def get_selected_lines(self, subarea):
         selected_lines = []
         selected_count = []
         href = []
         for link in self._soup.find_all(attrs={'class': 'text-list'}):
             for link in link.find_all('dd'):
                 if link.find('sub')is not None:
                     if link.find('sub').string == subarea:
                         if link.find('h2') is not None:
                             selected_lines.append(link.find('h2').get_text())
                             if link.find('span') is not None:
                                 selected_count.append(link.find('span').get_text()[1:])
                                 if link.find('a') is not None:
                                     href.append(link.find('a').get('href'))
         # print(hot_lines)
         # print(hot_count)
         # print(href)

         return selected_lines, selected_count, href

 # print(new_title[:-6])

     def get_game_result(self):
         game_result = {}
         result = []
         team =[]
         state = []
         for link in self._soup.find_all(attrs={'class': 'result'}):
             result.append(link.get_text()[1:-1])
         for link in self._soup.find_all(attrs={'class': 'team'}):
             team.append(link.get_text()[1:-1])
         for link in self._soup.find_all(attrs={'class': 'game-status'}):
             state.append(link.get_text().replace('\n', ''))
         for i in range(len(result)):
             game_result[team[i]] = [result[i], state[i]]
         return game_result

def main():

    get_in = GetI()
    print(get_in.get_game_result())
    # print(get_in.get_hot_lines())
    # print(get_in.get_selected_lines('火箭专区'))

if __name__ == "__main__":
    main()
