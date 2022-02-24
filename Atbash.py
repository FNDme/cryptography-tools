def atbashEncrypt(txt):
    txt = txt.upper()
    N = ord('Z') + ord('A')
    ans = ''
    for i in txt:
        if i.isalpha():
            ans += chr(N - ord(i))
        else:
            ans += i
    return ans