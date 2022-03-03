name = "Moon"
gravity = 0.00162 # in kms
planet = "Earth"

title = f"gravity facts about {name}"

print(title)

facts = f"""{'-'*80}
Planet Name: {planet}
Gravity on {name}: {gravity * 1000} m/s2
"""

print(facts)

template = f"""{title.title()}
{facts}
"""
print(template)
