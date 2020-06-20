import pymorphy2, pymorphy2_dicts_ru
import string

def getType(data):
    count = 0
    keywords = ["коллега", "преподаватель", "сотрудник"]
    keywords2 = ["студент", "учащийся", "обучающийся", "ученик"]
    tt = str.maketrans(dict.fromkeys(string.punctuation))
    morph = pymorphy2.MorphAnalyzer()
    data['type'] = "anybody"
    lst = data['text'].lower().translate(tt).split()
    text = []
    for word in lst:
        p = morph.parse(word)[0]  # приводим слово в нормальную форму
        text.append(p.normal_form)
    for i in keywords:
        if text.count(i) != -1:
            data['type'] = 'teacher'
            count+=text.count(i)
    for i in keywords2:
        if text.count(i) != -1:
            data['type'] = 'student'
            count-=text.count(i)
    if count > 0:
        data['type'] = 'teacher'
    elif count < 0:
        data['type'] = 'student'
    if data['tags'].find('Студент') != -1:
        data['type'] = "student"
    if data['tags'].find('НовостиДляАбитуриента') != -1:
        data['type'] = "nobody"
    return data



