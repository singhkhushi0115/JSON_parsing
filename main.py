import json  #imports Python's built-in JSON library

with open("data_dump.json", "r") as file:   #opens file in read mode and stores file in a variable "file"
    json_string = file.read()           #Reads the entire contents of the file and stores them as text
print("Type of json_string:", type(json_string))  #checks datatype of json_string, i.e, "string"
data = json.loads(json_string)    #converts str to dict and stores it in variable "data"
print("Type of data:", type(data))      #checks datatype of data, i.e, "dictionary"
answers = {}        
print("\n")


#Convert the file data to string and assign it to variable here, read using loads

def solve_q1_to_q5(data, answers):

    # Q1 - What is the company's short name and which city is it located in?
    short_name = data["company"]["short_name"]
    city = data["company"]["location"]["city"]

    answers["Q1"] = (
        f"The short name of the company is {short_name} and it is located in {city}."
    )

    print("The Short name of the Company is:", short_name)
    print("The City in which the company is located is:", city)
    print("\n")


    # Q2 - How many platforms does the company have? Print all their names.
    no_of_platforms = len(data["company"]["platforms"])
    platforms = data["company"]["platforms"]

    answers["Q2"] = (
        f"The company has {no_of_platforms} platforms: {', '.join(platforms)}"
    )

    print("The Number of platforms, the company has is:", no_of_platforms)
    print("The company has the following platforms:")

    for platform in platforms:
        print(platform)

    print("\n")


    # Q3 - How many employees are there in total?
    no_of_employees = len(data["employees"])

    answers["Q3"] = (
        f"Total number of employees in the company: {no_of_employees}"
    )

    print("Total number of employees in the company are:", no_of_employees)
    print("\n")


    # Q4 - Is the company currently active?
    company_active = data["company"]["active"]

    answers["Q4"] = f"Company active status: {company_active}"

    if company_active:
        print("Yes, the company is currently active.")
    else:
        print("No, the company is not currently active.")

    print("\n")


    # Q5 - What is Ravi Kumar's role and department?
    for employee in data["employees"]:
        if employee["name"] == "Ravi Kumar":

            answers["Q5"] = (
                f"Ravi Kumar works as a {employee['role']} "
                f"in the {employee['department']} department."
            )

            print(
                f"Ravi Kumar works as a {employee['role']} "
                f"in the {employee['department']} department."
            )

    print("\n")


def solve_employee_questions(data, answers):
    #Q6 - What is the first skill listed for Sneha Reddy?
    for employee in data["employees"]:
        if employee["name"] == "Sneha Reddy":
            answers["Q6"] = f"First skill for Sneha Reddy is {employee['skills'][0]}"
            print("First skill for Sneha Reddy is:", employee["skills"][0])
    print("\n")
    
    #Q9 - List the names of all employees who are currently active?
    print("Below is the list of Active Employees:")
    active_employees = []
    for employee in data["employees"]:
        if employee["active"]:
            active_employees.append(employee["name"])
            print(employee["name"])
    answers["Q9"] = f"Active employees: {', '.join(active_employees)}"
    print("\n")

    #10 - What is Kiran Babu's total salary (basic + allowances)?
    for employee in data["employees"]:
        if employee["name"]== "Kiran Babu":
            total_salary = employee['salary']['basic'] + employee['salary']['allowances']
            answers["Q10"] = f"Kiran Babu's total salary is ₹{total_salary}"
            print(f"The total salary of Kiran Babu (basic + allowances) is {employee['salary']['basic'] + employee['salary']['allowances']}")
    print("\n")

    #14 - Find the employee with ID EMP003. Print their name, status, and department.
    for employee in data["employees"]:
        if employee["id"] == "EMP003":
            print("Name:", employee["name"])
            print("Status:", employee["active"])
            print("Department:", employee["department"])
            answers["Q14"] = (
                f"Name: {employee['name']}, "
                f"Status: {employee['active']}, "
                f"Department: {employee['department']}"
                )
    print("\n")

    #15 - Which employees have 'Flutter' listed as one of their skills?
    flutter_employees = []
    print("Employees with Flutter skills:")
    for employee in data["employees"]:
        if "Flutter" in employee["skills"]:
            print(employee["name"])
            flutter_employees.append(employee["name"])
    answers["Q15"] = (
                f"Employees with Flutter skills: {', '.join(flutter_employees)}"
                )
    print("\n")

    #18 - Group all employees by department. For each department, list the employee names under it.
    departments = {} #creates empty dictionary
    for employee in data["employees"]:   #loops through every employee
        department = employee["department"]   #extracts the department of each employee
        name = employee["name"]   #extracts the employee name
        if department not in departments:    #Is this department new to us? 
            departments[department] = []   #If yes, add it to the department dictionary
        departments[department].append(name)    #Adds the employee name to the department's list.

    for department, employees in departments.items():  #loops through each key-value pair
        print(f"\n{department}:")   #prints department
        
        for employee in employees:
            print(f"- {employee}")  #prints employees under the respective department
    answers["Q18"] = departments        
    print("\n")

    #19 - Collect all unique skills across every employee and print them as one deduplicated list (no repeats).
    skills = set()   #empty set    #Why set? Set ignores duplicates
    for employee in data["employees"]:   #loop iterates through employees
        for skill in employee["skills"]: #loop iterates through employee skills
            skills.add(skill)   #adds skill to set
    print(skills)
    answers["Q19"] = list(skills)
    print("\n")

    #20 - Sort all employees by total salary (basic + allowances) in descending order. Print name and total salary for each.
    employee_salaries = []    #empty list
    for employee in data["employees"]:        #iterates through all employees
        total_salary = employee["salary"]["basic"] + employee["salary"]["allowances"]   #calculates total salary
        employee_salaries.append((employee["name"], total_salary))  #adds to the list

    employee_salaries.sort(key=lambda x: x[1], reverse=True)   #sorts the list  #reverse=True means highest first
    for name, salary in employee_salaries:     #tuple unpacking
        print(f"{name}: ₹{salary}")           #what initially exists as ("Kiran babu", 26500), will now exist as (Kiran Babu: ₹26500)
    answers["Q20"] = [
        f"{name}: ₹{salary}"
        for name, salary in employee_salaries
    ]
    print("\n")

def solve_project_questions(data, answers):

    #Q7 - What is the status of the Telangana Air Quality Dashboard project?
    for project in data["projects"]:
        if project["name"] == "Telangana Air Quality Dashboard":
            answers["Q7"] = f"The status of the Telangana Air Quality Dashboard project is {project['status']}"
            print(f"The staus of the Telangana Air Quality Dashboard is {project['status']}")
    print("\n")

    #11 - From the C2C project, list all features that are NOT yet completed.
    not_completed_features = []
    for project in data["projects"]:
        if project["name"] == "College 2 Connect (C2C)":
            print("Features not yet completed:")
            for feature in project["features"]:
                if not feature["completed"]:
                    print(feature["name"])
                    not_completed_features.append(feature["name"])

    answers["Q11"] = f"Features not yet completed: {', '.join(not_completed_features)}"
    print("\n")

    #16 - For the C2C project, replace each team_id with the actual employee name by looking up the employees array. Print the result.
    team_members = []
    for project in data["projects"]:
        if project["name"] == "College 2 Connect (C2C)":
            print("Team Members for C2C Project:")
            for team_id in project["team_ids"]:
                for employee in data["employees"]:
                    if employee["id"] == team_id:
                        print(employee["name"])
                        team_members.append(employee["name"])

    answers["Q16"] = f"Team members for C2C project: {', '.join(team_members)}"
    print("\n")

    #17 - Calculate total budget allocated vs total budget spent across ALL projects. Also print the remaining budget.
    total_allocated = 0           #creates variable and initializes it to 0
    total_spent = 0               #creates another variable and initializes it to 0
    for project in data["projects"]:       #loops through all the projects
        total_allocated += project["budget"]["allocated"]   #total_allocated = total_allocated + project["budget"]["allocated"]
        total_spent += project["budget"]["spent"]           #total_spent = total_spent + 180000
    budget_remaining = total_allocated - total_spent        #calculates remaining budgets
    print("Total budget allocated:", total_allocated)
    print("Total budget spent:", total_spent)
    print("Total budget remaining:", budget_remaining)
    answers["Q17"] = (
        f"Total allocated budget: {total_allocated}, "
        f"Total spent budget: {total_spent}, "
        f"Remaining budget: {budget_remaining}"
    )
    print("\n")

def solve_company_api_questions(data, answers):
    #Q8 - What is the company's website URL?
    url = data["company"]["contact"]["website"]
    answers["Q8"] = f"The company's website URL is {url}"
    print("The company's URL is:", url)
    print("\n")

    #12 - Which API endpoints do NOT require authentication? List their routes.
    routes = []
    print("The following API endpoints do not require authentication:")
    for api_endpoint in data["api_endpoints"]:
        if not api_endpoint["auth_required"]:
            print(api_endpoint["route"])
            routes.append(api_endpoint["route"])

    answers["Q12"] = f"API endpoints that do not require authentication: {', '.join(routes)}"
    print("\n")

def solve_partner_questions(data, answers):
    #13 - How many college partners are verified? How many are not?
    verified_partners = []
    unverified_partners = []
    print("Following are the verified college partners:")
    for partner in data["college_partners"]:
        if partner["verified"]:
            print(partner["name"])
            verified_partners.append(partner["name"])
    print("Following are the un-verified college partners:")
    for partner in data["college_partners"]:
        if not partner["verified"]:
            print(partner["name"])
            unverified_partners.append(partner["name"])

    answers["Q13"] = (
        f"Verified partners: {', '.join(verified_partners)}. "
        f"Unverified partners: {', '.join(unverified_partners)}."
    )
    print("\n")

solve_q1_to_q5(data, answers)
solve_employee_questions(data, answers)
solve_project_questions(data, answers)
solve_company_api_questions(data, answers)
solve_partner_questions(data, answers)

print(answers)                                    
with open("output_data.json", "w", encoding="utf-8") as file:
    json.dump(answers, file, indent=4, ensure_ascii=False)

print("Answers written successfully to output_data.json")


print("\n===== JSON.DUMPS() DEMO =====")

json_output_string = json.dumps(
    answers,
    indent=4,
    ensure_ascii=False
)

print("Type of json_output_string:", type(json_output_string))

with open("answers_string.txt", "w", encoding="utf-8") as file:
    file.write(json_output_string)

print("JSON string written successfully to answers_string.txt")






