'''
解密
'''

def zeng_gongliang_decryption(text: str) -> str:
    """TODO # 加上TODO这个东东，git会提醒你，这个还挺不错的诶
    """
    key_dict = {'1':'请弓', '2':'请箭', '3':'请刀', '4':'请甲', '5':'请枪旗',
                '6':'请锅幕', '7':'请马', '8':'请衣赐', '9':'请粮料', '10':'请草料',
                '11':'请车牛', '12':'请船', '13':'请攻城守县', '14':'请添兵', '15':'请移营',
                '16':'请进军', '17':'请退军', '18':'请固定', '19':'未见军', '20':'见贼',
                '21':'贼多', '22':'贼少', '23':'贼相敌', '24':'贼添兵', '25':'贼移营',
                '26':'贼进军', '27':'贼退军', '28':'贼固守', '29':'围得贼城', '30':'解围城',
                '31':'被贼围', '32':'贼围解', '33':'战不胜', '34':'战大胜', '35':'战大捷',
                '36':'将士投降', '37':'将士叛', '38':'士卒病', '39':'部将病', '40':'战小胜',}

    decryption_text = ''
    poem = "城阙辅三秦风烟望五津与君离别意同是宦游人海内存知己天涯若比邻无为在歧路儿女共沾巾"
    num = poem.find(text)
    if num != -1:
        decryption_text = key_dict[str(num + 1)]
    else:
        decryption_text = None
    print(decryption_text)
    # return decryption_text


zeng_gongliang_decryption("请弓")
