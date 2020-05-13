def getType(data):
    keywords = ["коллег", "преподавател", "сотрудник"]
    keywords2 = ["студент", "учащи", "обучающ"]
    data['type'] = "anybody"
    if data['tags'].find('Студент') != -1:
        data['type'] = "student"
    for i in keywords:
        str = data['text'].lower()
        if str.find(i) != -1:
            data['type'] = "teacher"
    if data['type'] == "anybody":
        for i in keywords2:
            str = data['text'].lower()
            if str.find(i) != -1:
                data['type'] = "student"
    if data['tags'].find('НовостиДляАбитуриента') != -1:
        data['type'] = "nobody"
    return data