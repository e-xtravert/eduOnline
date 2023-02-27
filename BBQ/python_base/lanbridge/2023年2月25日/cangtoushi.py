'''
藏头诗
'''
poem_input = "芦花丛中一扁舟，俊杰俄从此地游，义士若能知此理，反躬难逃可无忧。"


def acrostic_poetry_decryption(poem: str) -> str:
    """TODO  # 加上TODO这个东东，git会提醒你，这个还挺不错的诶
    """
    lis = []
    # lis = [poem[i + 1] for i in poem if poem[i] == "，" or poem[i] == "。"]
    decryption_text: str = ''
    if poem == None:
        decryption_text = None
    n = poem.find("，")
    lis.append(poem[n + 1])
    while n != -1:
        n = poem.find("，", n + 1)
        lis.append(poem[n + 1])
    # st = lis.pop(-1)
    # lis[0] = lis.pop(-1)
    lis.insert(0, lis.pop(-1))
    res = ''.join(lis)
    print('"' + res + '"')
    # decryption_text : str = ''
    return decryption_text


acrostic_poetry_decryption(poem_input)
