import json
import requests
import urllib.parse
import subprocess

# curl -s \
#     -X POST \
#     "localhost:50021/audio_query?speaker=1"\
#     --get --data-urlencode text@text.txt \
#     > query.json


def makeAudioQuery(text, speaker):
    url = 'http://voice:50021/audio_query'
    encodeText = urllib.parse.quote(text)
    url = url + '?' + 'speaker=' + speaker + '&' + 'text=' + encodeText
    response = requests.post(url)
    return response

# curl -s \
#     -H "Content-Type: application/json" \
#     -X POST \
#     -d @query.json \
#     localhost:50021/synthesis?speaker=1 \
#     > audio.wav


def makeAudioWav(query, speaker, wav):
    url = 'http://voice:50021/synthesis' + '?speaker=' + speaker
    header = {
        "Content-Type": "application/json"
    }
    res = requests.post(url, headers=header, json=query)
    f = open(wav, 'wb')
    f.write(res.content)
    f.close

# start audio


def playAudio(wav):
    subprocess.run(['paplay', wav])

# play input text


def playText(text):
    wav = 'test.wav'
    res = makeAudioQuery(text, '2')
    jsonQuery = json.loads(res.text)
    makeAudioWav(jsonQuery, '2', wav)
    playAudio(wav)


# playText('四国めたんちゃんはおちんぽミルクが大好物なのだ')
