def reverse(text: str) -> str:
    return (text[::-1])
    pass


def first_to_upper(text: str) -> str:
    l=text.split()
    l1=[]
    for i in l:
        l1.append(i[0].capitalize()+i[1:])
    s=" ".join(l1)
    return(s)
    pass


def count_vowels(text: str) -> int:
    s=list(text)
    k=0
    for i in s:
        if (i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='y' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U' or i=='Y' or i=='Ą' or i=="ą" or i=='Ę' or i=="ę" or i=='Ó' or i=="ó" ):
            k+=1
    return(k)
    pass


def sum_digits(text: str) -> int:
    s = list(text)
    k = 0
    for i in s:
        if (i=='1' or i=='2' or i=='3' or i=='4' or i=='5' or i=='6' or i=='7' or i=='8' or i=='9'):
            k += int(i)
    return (k)
    pass


def search_substr(text: str, sub: str) -> int:
    n=len(text)
    m=len(sub)
    for i in range(n - m + 1):
        if text[i: i + m] == sub:
            return (i)

    pass
