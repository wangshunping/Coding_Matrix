
'''
test
'''

import politics_lab as ii

def main():
    f= open('voting_record_dump109.txt')
    mylist = list(f)

    votDic = ii.create_voting_dict(mylist)
    nameD = namelist(mylist)

    tmplist = [ii.find_average_similarity(x,nameD,votDic) for x in list(nameD)]
    #tmplist = [ii.find_average_similarity(x,nameD,votDic) for x in list(nameD)]
    p = tmplist.index(max(tmplist))
    print(list(nameD)[p])

    print(ii.find_average_record(nameD,votDic))



def namelist(strlist):
    return {x.split()[0] for x in strlist if x.split()[1] == 'D'}

if __name__ == '__main__':
    main()



