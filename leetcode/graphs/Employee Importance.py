"""
# Employee info
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        return self.get_importance(self.find_emp(id,employees),employees)
            
    def get_importance(self,emp,employees):
        imp=emp.importance
        for employee in emp.subordinates:
            imp+=self.get_importance(self.find_emp(employee,employees),employees)
        return imp
    
    def find_emp(self,id,employees):
         for emp in employees:
            if emp.id==id:
                return emp
        