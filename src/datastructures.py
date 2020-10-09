
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint
import json

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = []

    @staticmethod
    def create_member(id, first_name, age, lucky_numbers):
        return {
            "id": id,
            "first_name": first_name,
            "age": age,
            "lucky_numbers": lucky_numbers
        }

    # read-only: Use this method to generate random members ID's when adding members into the list
    @staticmethod
    def _generate_id():
        return randint(0, 99999999)

    def add_member(self, member):
        self._members.append(member)
        return member["id"]

    def get_member_by_id(self, id):
        for i in range(len(self._members)): 
            if self._members[i]['id'] == id: 
                return i

    def delete_member(self, id):
        index = self.get_member_by_id(id)
        del self._members[index] 

    def update_member(self, id, member):
        index = self.get_member_by_id(id)
        self._members[index] = member 
        
    def get_member(self, id):
        index = self.get_member_by_id(id)
        return self._members[index]

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members