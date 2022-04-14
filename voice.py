import json
import requests
import urllib.parse
import playsound

# curl -s \
#     -X POST \
#     "localhost:50021/audio_query?speaker=1"\
#     --get --data-urlencode text@text.txt \
#     > query.json
def makeAudioQuery(text):
    url = 'http://voice:50021/audio_query'
    encodeText = urllib.parse.quote(text)
    url = url + '?' + 'speaker=1' + '&' + 'text=' + encodeText
    response = requests.post(url)
    return response

# curl -s \
#     -H "Content-Type: application/json" \
#     -X POST \
#     -d @query.json \
#     localhost:50021/synthesis?speaker=1 \
#     > audio.wav
def makeAudioWav(query):
    url = 'http://voice:50021/synthesis' + '?speaker=1'
    header = {
        "Content-Type": "application/json"
    }
    res = requests.post(url, headers=header, json=query)
    return res

res = makeAudioQuery('おっぱい')
jsonQuery = json.loads(res.text)
res = makeAudioWav(jsonQuery)

f = open('test.wav', 'wb')
f.write(res.content)
f.close

playsound.playsound('test.wav')