import youtube_dl
import json

search_results = []

ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    search_result = ydl.extract_info('https://www.youtube.com/watch?v=GIDoQsQyS0s',download=False)
    # ydl.download(['https://www.youtube.com/watch?v=GIDoQsQyS0s'])
# print(search_result)
search_results.append(search_result)

ydl_opts1 = {}
with youtube_dl.YoutubeDL(ydl_opts1) as ydl:
    search_result_1 = ydl.extract_info('https://www.youtube.com/watch?v=Wv2rLZmbPMA', False)
search_results.append(search_result_1)

# var = "ant"
# with open('a.txt', "a" ) as out: # par2 => 'a' = all, 'w'= write 'r' = read
#     out.write(var + "\n")
pp = {
    "a": 1,
}
with open('test.json','w') as out:
    json.dump(search_result_1, out)

with open('test.json', encoding = 'utf-8') as data:
    dataRead = json.loads(data.read())

print(dataRead['title'])