
'''
test
'''

import politics_lab as ii

def main():
    f= open('voting_record_dump109.txt')
    mylist = list(f)

    votDic = ii.create_voting_dict(mylist)
    nameD = namelist(mylist)

    print(ii.most_similar('Chafee',votDic))
    print(ii.least_similar('Santorum',votDic))


def namelist(strlist):
    return {x.split()[0] for x in strlist }

if __name__ == '__main__':
    main()



