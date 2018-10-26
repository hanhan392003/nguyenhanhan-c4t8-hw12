from youtube_dl import YoutubeDL
import json

options = {
    'default_search': 'ytsearch5'
}

ydl = YoutubeDL(options)
search_result = ydl.extract_info('that girl', False)
# print(search_result)

with open('test1.json','w') as out:
    json.dump(search_result, out)

with open('test1.json', encoding = 'utf-8') as data:
    dataRead = json.loads(data.read())

print(dataRead['entries'][0]['title'])

for i in range(5):
    print(dataRead['entries'][i]['title'])

print(dataRead['entries'][0]['duration'])
print(dataRead['entries'][0]['id'])
print(dataRead['entries'][0]['webpage_url'])
