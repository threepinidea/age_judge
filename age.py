driving = input('是否開過車(請輸入有/沒有): ')
if driving != '有' and driving != '沒有':
    print('只能輸入 有/沒有')
    raise SystemExit

age = int(input('請輸入你的年齡: '))
if driving == '有':
    if age >= 18:
        print('通過測驗')
    else:
        print('這年齡開車 是不是違規偷開阿 ?')
elif driving =='沒有':
    if age >= 18:
        print('你可以考駕照開車了, 怎麼沒去考')
    else:
        print('很好, 再過幾年就可以考駕照了')