cipher = open("output.txt", "r").read().replace("\n", "")

cipher = list(cipher)
print(cipher)

# crt([x1, x2, x3, x4], [2, 3, 5, 7]) --> flag_n
palette = '.=w-o^*'

X = []
flag = ""
while len(cipher) != 0:
    c = cipher.pop(0)
    if c == " ":
        continue
    X.append(palette.index(c))
    if len(X) == 4:
        flag += chr(crt(X, [2, 3, 5, 7]))
        X = []


print(flag)
# DUCTF{r3c0nstruct10n_0f_fl4g_fr0m_fl4g_4r7_by_l00kup_t4bl3_0r_ch1n3s3_r3m41nd3r1ng?}
