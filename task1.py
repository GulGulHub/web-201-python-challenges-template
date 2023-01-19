# #for i in range(1,11):
#  #   print(i)
#
# # sort alphabetically
# presidents = ["Washington", "Adams", "Jefferson", "Madison", "Monroe", "Adams_the2nd", "Jackson"]
# #print(sorted(presidents))
# #for president in range(len(presidents)):
#  #   print(presidents[president], president)
#
# # print all presidents in key:value pairs, the index being the value
# pres_dict = {}
#
# for president in presidents:
#     print(f"Name:{president}")
#
#
# # for president in range(len(presidents)):
# #     pres_dict[presidents[president]]= president
# #
# #
# # pres_dict["Obama"]=7
# # pres_dict["Trump"]=8
# # pres_dict["Biden"]=9
#
# # add
# #
# # def add_a_pres(**kwargs):
# #     global pres_dict
# #     pres_dict.update(kwargs)
# # #
# # add_a_pres("Obama"=7, )
#
# # Code from Jyosna
# # # add more presidents - Obama -7, Trump - 8, Biden - 9
# # def add_pres(pres_dict, entry):
# #     pres_dict.update(entry)
# # # president_dict["Obama"]=7
# # # president_dict.update({"Trump": 8})
# # # president_dict.update({"Biden": 9})
# # new_millenial_presidents =["Obama", "Trump", "Biden"]
# # i = 7
# # for each in new_millenial_presidents:
# #     add_pres(president_dict, {each:i})
# #     i = i+1
#
#
# # The update() method updates the dictionary with the elements from another dictionary object or from an iterable of key/value pairs.
# pres_dict.update()
#
# #The items() method returns a view object that displays a list of dictionary's (key, value) tuple pairs.
# pres_dict.items()
# # The items() method returns a view object that displays a list of dictionary's (key, value) tuple pairs.
# pres_dict.copy()
# # The fromkeys() method creates a dictionary from the given sequence of keys and values.
# pres_dict.fromkeys()
#
# #- removes all items
# pres_dict.clear()
# # The pop() method removes and returns an element from a dictionary having the given key.
# pres_dict.pop("key")
# #The Python popitem() method removes and returns the last element (key, value) pair inserted into the dictionary.
# pres_dict.popitem()
# # del statement will delete anything with dictionarys = give key it will del both


def extract_integers(mixed_list):
    new_list = (item for item in list if item == int)

extract_integers([1, 'apple', 2, 'banana',3, 4]) == [1,2,3,4]



