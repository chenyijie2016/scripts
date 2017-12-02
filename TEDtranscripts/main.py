import json
import requests

url = 'https://www.ted.com/talks/{ted_id}/transcript.json?language=zh-cn'

def main():
    ted_id = input('input scritpt ted_id:')
    res = requests.get(url.format(ted_id=ted_id))
    transcript= json.loads(res.content.decode('utf-8'), encoding='utf-8')
    res = ['']
    for parahraph in transcript["paragraphs"]:
        # print(parahraph)
        for item in parahraph["cues"]:
            if res[-1] == item['text']:
                continue
            else:
                res.append(item["text"])
        res.append('\n')

    f = open(str(ted_id) + 'script.txt', 'w')
    for line in res:
        try:
            f.write(line + ' ')
        except UnicodeEncodeError:
            continue
    f.close()

    print(json.dumps(transcript, indent=2))


if __name__ == '__main__':
    main()
