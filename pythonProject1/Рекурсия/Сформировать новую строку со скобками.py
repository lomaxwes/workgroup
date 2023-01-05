def rec(text):
    if len(text) == 0:
        return text
    else:
        return text[0] + rec(text[1:]) + text[0].replace("(", ")")

print(rec("(abc(def(g"))
print(rec("(((t((p((y((kx((((e(((((((vw((v(e((v(m(((h(mlx((s((((d(y((((((((mtk(d(umi((s((sx(p((m(r((kqo"))