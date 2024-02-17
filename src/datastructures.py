
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = []
    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member): 
        if not member.get("id"):
          member["id"] = self._generateId()
        self._members.append(member)

        print("añadir miembro",member)
        pass

    def delete_member(self, id):
        print(id)
        for member in self._members:
            if member["id"] == id :
                self._members.remove(member)
                return True
        return False
        # fill this method and update the return
    

    def update_member(self, id, member):
        print("actualizando", id)
        for family_member in self._members:
            if family_member["id"] == id:
                self._members.remove(family_member)
                member["id"] = id
                self._members.append(member)
                print("son iguales")
                return True
        return False
    pass



    def get_member(self, id):
        # fill this method and update the return
        for family_member in self._members:
            if family_member["id"] == id:
                return family_member
        return False
        pass

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members



# """
# update this file to implement the following already declared methods:
# - add_member: Should add a member to the self._members list
# - delete_member: Should delete a member from the self._members list
# - update_member: Should update a member from the self._members list
# - get_member: Should return a member from the self._members list
# """

# class FamilyStructure:
#     def __init__(self, last_name):
#         self.last_name = last_name
#         self._next_id = 1
#         self._members = []

#     # This method generates a unique 'id' when adding members into the list (you shouldn't touch this function)
#     def _generate_id(self):
#         generated_id = self._next_id
#         self._next_id += 1
#         return generated_id

#     def add_member(self, member):
#         member["last_name"] = self.last_name
#         member["id"] = self._generate_id()
#         member["lucky_numbers"] = list(member.get("lucky_numbers", set()))
#         self._members.append(member)

#         return member

#     def delete_member(self, id):
#         for position in range(len(self._members)):
#             if self._members[position]["id"] == id:
#                 self._members.pop(position)
                
#                 return None
            

#     def get_member(self, id):
#         for member in self._members:
#             if member["id"] == int(id):
#                 return member
            
#         return None

#     # This method is done, it returns a list with all the family members
#     def get_all_members(self):
#         return self._members