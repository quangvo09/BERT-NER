import json
from collections import defaultdict
from bert import Ner
model = Ner("out/")


def main():
    data = load_data()

    key = 'B-INV'
    # key = 'B-ADDR'
    percent = test(data[0:1000], key)
    print(key, percent)


def test(data, key):
    total = 0
    checked = 0
    failed = []
    for row in data:
        valid = validate(row['Content'], key, row[key])
        checked += 1
        if valid is True:
            total += 1
            percent = total / checked
            print('OK ', percent)
        else:
            failed.append(row)
            print('F')

    with open('data/failed.json', 'w') as outfile:
        json.dump(failed, outfile)

    percent = total / len(data)
    return percent


def load_data():
    with open('data/test.json', encoding='utf-8-sig') as json_file:
        data = json.load(json_file)
        return data


def validate(text, test_key, expected):
    result = model.predict(text)
    res = defaultdict(list)
    for word in result:
        key, value = list(word.items())[0]
        if value['confidence'] > 0.9:
            res[value['tag']].append(key)

    if expected == "" and len(res[test_key]) == 0:
        return True

    if str(expected) in res[test_key]:
        return True

    print(text, expected, res[test_key])
    return False


if __name__ == '__main__':
    main()
