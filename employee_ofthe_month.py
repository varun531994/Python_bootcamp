def employee_tab(work_hours):
        current_max = 0
        employee_of_the_month = ''
        
        for employee,hours in work_hours:
            if hours > current_max:
                current_max = hours
                employee_of_the_month = employee
            else:
                pass
        return (employee_of_the_month,current_max)

work_hours = [('Jack',130),('Jill',120),('Max',200),('Bill',230),('Joey',280)]

a = 'Who is the employee of the month?/Who'
b = input('')
work_hours = [('Jack',130),('Jill',120),('Max',200),('Bill',230),('Joey',280)]

if b.lower() == "who":
 print(employee_tab(work_hours))
else:
 pass
 
 
   

