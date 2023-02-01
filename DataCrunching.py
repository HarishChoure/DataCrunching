import  csv
result_ip = {}
with open('ip_1m.tsv', "r") as file:
    reader = csv.reader(file, delimiter="\t")
    for row in reader:
        id, ip = row
        result_ip[id] = ip


result_plan = {}
with open('plan_32m.tsv', "r") as file:
    reader = csv.reader(file, delimiter="\t")
    for row in reader:
        email_, pasw = row
        result_plan[email_] = pasw

resulr_user = {}
with open('user_email_hash.1m.tsv','r') as file:
    reader = csv.reader(file, delimiter="\t")
    for row in reader:
        id, usernam,email,hashed_pasword = row
        resulr_user[id] = [id,usernam,email,hashed_pasword]

common_keys = set(result_ip.keys()).intersection(resulr_user.keys())


common_values = []
for value in result_plan.values():
    if value in result_user.values():
        common_values.append(value)
