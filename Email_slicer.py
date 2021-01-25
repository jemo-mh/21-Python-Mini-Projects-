email =input("input ur email adress").strip()
user_name =email[:email.index("@")]
domain_name = email[email.index("@")+1 :]
res = f"your user name is '{user_name}' and your domain is '{domain_name}'"

print(res)
