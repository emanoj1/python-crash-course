person_age = 2

if person_age < 2:
    life_stage = "You are a baby!"
elif person_age < 4:
    life_stage = "You are a toddler."
elif person_age <13:
    life_stage = "You are a kid."
elif person_age < 20:
    life_stage = "You are a teenager!"
elif person_age < 65:
    life_stage = "You are an adult."
elif person_age >= 65:
    life_stage = "You are an elder."

print(life_stage)