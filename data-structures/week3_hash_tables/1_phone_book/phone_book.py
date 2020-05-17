# python3


import sys


class HashMap:
    """ This is a class for the HashMap data structure built on an arrays """

    def __init__(self):
        self.n = None
        self.query = None
        self.arguments = None
        self.PhoneBook = None
        self.a = 34
        self.b = 24
        self.p = 100019
        self.m = 1000
        self.hashkey = None

    def read(self):
        self.n = int(sys.stdin.readline())
        self.PhoneBook = [{} for _ in range(self.m)]
        for _ in range(self.n):
            self.query, *self.arguments = sys.stdin.readline().rstrip('\n').split(' ')
            self.hashkey = (
                ((self.a * int(self.arguments[0]))+self.b) % self.p) % self.m
            if self.query == "add":
                self.add()
            elif self.query == "del":
                self.delete()
            elif self.query == "find":
                self.find()

    def add(self):
        self.PhoneBook[self.hashkey][int(
            self.arguments[0])] = self.arguments[1]

    def delete(self):
        if int(self.arguments[0]) in self.PhoneBook[self.hashkey]:
            del self.PhoneBook[self.hashkey][int(self.arguments[0])]

    def find(self):
        if int(self.arguments[0]) in self.PhoneBook[self.hashkey]:
            print(self.PhoneBook[self.hashkey][int(self.arguments[0])])
        else:
            print('not found')


if __name__ == "__main__":
    phone_book = HashMap()
    phone_book.read()



# class Query:
#     def __init__(self, query):
#         self.type = query[0]
#         self.number = int(query[1])
#         if self.type == 'add':
#             self.name = query[2]


# def read_queries():
#     n = int(input())
#     return [Query(input().split()) for i in range(n)]


# def write_responses(result):
#     print('\n'.join(result))


# def process_queries(queries):
#     result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    # contacts = {}
    # for cur_query in queries:
    #     if cur_query.type == 'add':
    # if we already have contact with such number,
    # we should rewrite contact's name
    #     contacts[cur_query.number] == cur_query.name
    # elif cur_query.type == 'del':
    #     contacts.pop(cur_query.number, None)
    # for contact in contacts:
    #     if contact.number == cur_query.number:
    #         contact.name = cur_query.name
    #         break
    # otherwise, just add it
    # else:
    #     if cur_query.number in contacts:
    #         result.append(contacts[cur_query.number])
    #     else:
    #         result.append("not found")
    # contacts.append(cur_query)
    # elif cur_query.type == 'del':
    #     for j in range(len(contacts)):
    #         if contacts[j].number == cur_query.number:
    #             contacts.pop(j)
    #             break
    # else:
    #     response = 'not found'
    #     for contact in contacts:
    #         if contact.number == cur_query.number:
    #             response = contact.name
    #             break
    #     result.append(response)
#     return result


# if __name__ == '__main__':
#     write_responses(process_queries(read_queries()))
