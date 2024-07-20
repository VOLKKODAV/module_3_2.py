def send_email(mes, recipient, *, sender='university.help@gmail.com'):
    if recipient == sender:
        print('Нельзя отправить письмо самому себе! - А жаль:(')
    elif ("@" and (".com" or ".ru" or ".net")) not in recipient and ("@" and (".com" or ".ru" or ".net")) not in sender:
        print(f'Невозможно отправить письмо с адреса: {sender} на адрес: {recipient}')
    elif sender == 'university.help@gmail.com':
        print('Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
    else:
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')


send_email('mes', 'vasyok1337@gmail.com')
send_email('mes', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('mes', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('mes', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
