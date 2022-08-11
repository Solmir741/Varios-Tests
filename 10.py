


def only_z(p, pc):
    while pc < len(p):
        if p[pc] != '*': return False
        pc += 1
    return True

def reg():
    # читаем шаблон p посимвольно и сравниваем его с входящей строкой s
    # случаи исключения
    sc = 0
    pc = 0
    if len(s) == 0: # в данном случае допускаются только паттерны p = "*******"
        return only_z(p, pc)
    while sc < len(s) and pc < len(p):
        ssym, psym = s[sc], p[pc]
        if psym not in ('*', '.'):
            if ssym != psym: 
                return False
            else:
                sc += 1
                pc += 1
        elif psym == '*':
            while pc < len(p) and p[pc] == '*':# проматываем паттерн, пока в нем не закончатся символы и будут * (для паттерна типа "a***s.f")
                pc += 1
            if pc < len(p): 
                psym = p[pc]# берем следующий важный для паттерна символ
            else:# в этом случае в конце паттерна звезда, и может быть в строке всё что угодно, поэтому True
                return True
            if psym in ('*', '.'): 
                continue
            while sc < len(s) and s[sc] != psym:# проматываем строку, пока в нем не закончатся символы и не будет найдено следущий нужный нам символ
                sc += 1
        elif psym == '.':
            sc += 1
            pc += 1
    # если выше код закончился без ошибок и строки полностью пройдены, то значит паттерн и строка совпадает
    if sc == len(s) and pc == len(p):
        return True
    elif sc == len(s):
        return only_z()
    else:# когда паттерн короче чем строка
        return False

s = "aayyisuf"
p = "a*s.f"



s = "dfsfxczd"
p = ".*.zd"
s = ""
p = "******"
s = "aab"
p = "c*a*b"



if __name__ == "__main__":
    print(reg())