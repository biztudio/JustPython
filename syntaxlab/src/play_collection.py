names_list1 = ['sTevEn lOBs',
               'coCo lee',
               'JAck zhaNG',
               'LiSa ChEn',
               'elSA Y Shen',
               'georgE w bUsH',
               'PETER cHeN',
               'brUce Ho',
               'biLL W clinTON',
               'ciRAlI Clinton',
               'Yang SHEN',
               'robin zhAng',
               'Bruce LEE']

# 练习一，把一组大小写不规范的名字 names_list1 转成首字母大写的一组名字
# 练习二，把练习一中大小写规范好的名字列表姓氏(最后一个词作为姓氏)分组, 组名就是姓氏
# 形如 {'Jobs':{'Steven Jobs'}, 'Zhang':{'Robin Zhang','Jack Zhang'} ... }


def get_normalize_names(names_list):
    return [' '.join([n[0].upper() + n[1:].lower() for n in name.split(' ')]) for name in names_list]


def get_names_group(names_list):
    names_group = {}
    for fname in {name.split(' ')[-1] for name in set(names_list)}:
        names_group[fname] = {name for name in names_list if name.split(' ')[-1] == fname}
        # [x[0] for x in zip(a,a[1:]+[None]) if x!=(0,2)]
    return names_group


names_list2 = get_normalize_names(names_list1)
names_grouped = get_names_group(names_list2)
print(names_list1)
print(names_list2)
print(names_grouped)
print(names_grouped['Shen'])



