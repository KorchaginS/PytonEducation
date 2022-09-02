# TODO: complete this class

class PaginationHelper:

    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page

    def item_count(self):
        return len(self.collection)

    def page_count(self):
        return len(self.collection) // self.items_per_page + 1

    def page_item_count(self, page_index):
        if page_index <= PaginationHelper.page_count(self) - 1:
            return len(self.collection[self.items_per_page * page_index:
                                       self.items_per_page * page_index + self.items_per_page])
        else:
            return -1

    def page_index(self, item_index):
        if item_index <= self.items_per_page * PaginationHelper.page_count(self) and  item_index > -1 and self.collection:
            return item_index // self.items_per_page
        else:
            return -1

def high_and_low(numbers):

    nums = numbers.split(' ')
    min = int(nums[0])
    max = int(nums[0])

    for x in nums:
        if int(x) > max:
            max = int(x)

        if int(x) < min:
            min = int(x)

    numbers = str(max) + ' ' + str(min)
    return numbers

print(high_and_low("1 9 3 4 -5"))