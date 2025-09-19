from credit import Credit
from list import List


class App:
    def run(self):

        credit = Credit('meezan', '1232424', 'nofil', '5000')
        credit1 = Credit('meezan', '1232424', 'nofil', '4000')


        list = List()
        list.append(credit)
        list.append(credit1)
        print(list.list)
        
        list.remove(credit)
        print(list.list)

        # for i in range(len(list.list)):
        #     if (list.list[i].balance == credit.balance):
        #         print(list.list[i].balance)

        # print(list.list)
        # l1 = [1, 2, 'hi']
        # # l1.remove(1)
        # print(l1)

        # for i in range(3):
        #     print()






