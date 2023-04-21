#1491. Average Salary Excluding the Minimum and Maximum Salary

class Solution:
    def average(self, salary: List[int]) -> float:
        min_salary = min(salary)
        max_salary = max(salary)
        sum_salary = sum(salary) - min_salary - max_salary
        count = len(salary) - 2

        average_salary = sum_salary / count

        return average_salary
        
