mailing_list = [
    ["Chilli", "chilli@thechihuahua.com"],
    ["Roary", "roary@moth.catchers"],
    ["Remus", "remus@kapers.dog"],
    ["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"],
    ["Ivy", "noreply@goldendreamers.xyz"],
]

print(f"{mailing_list[0][0]}: {mailing_list[0][1]}")
print(f"{mailing_list[1][0]}: {mailing_list[1][1]}")
print(f"{mailing_list[2][0]}: {mailing_list[2][1]}")
print(f"{mailing_list[3][0]}: {mailing_list[3][1]}")
print(f"{mailing_list[4][0]}: {mailing_list[4][1]}")

# for number in range(len(mailing_list)):
#     print(f"{mailing_list[number][0]}: {mailing_list[number][1]}")

for item in mailing_list:
    print(f"{item[0]}: {item[1]}")
