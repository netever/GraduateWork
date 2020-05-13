def getType(data):
    count = 0
    keywords = ["коллег", "преподавател", "сотрудник"]
    keywords2 = ["студент", "учащи", "обучающ"]
    data['type'] = "anybody"
    for i in keywords:
        str = data['text'].lower()
        if str.find(i) != -1:
            data['type'] = 'teacher'
            count+=1
    for i in keywords2:
        str = data['text'].lower()
        if str.find(i) != -1:
            data['type'] = 'student'
            count-=1
    if count > 0:
        data['type'] = 'teacher'
    elif count < 0:
        data['type'] = 'student'
    if data['tags'].find('Студент') != -1:
        data['type'] = "student"
    if data['tags'].find('НовостиДляАбитуриента') != -1:
        data['type'] = "nobody"
    return data