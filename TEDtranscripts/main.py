import json
import requests

_url = 'https://www.ted.com/talks/'
url_ = '/transcript.json?language=zh-cn'


def main():
    number = input('input scritpt number:')
    res = requests.get(_url + str(number) + url_)
    transcript = json.loads(res.content.decode('utf-8'), encoding='utf-8')

    res = ['']
    for parahraph in transcript["paragraphs"]:
        # print(parahraph)
        for item in parahraph["cues"]:
            if res[-1] == item['text']:
                continue
            else:
                res.append(item["text"])
        res.append('\n')

    f = open(str(number) + 'script.txt', 'w')
    for line in res:
        try:
            f.write(line + ' ')
        except UnicodeEncodeError:
            continue
    f.close()

    print(json.dumps(transcript, indent=2))


if __name__ == '__main__':
    main()
