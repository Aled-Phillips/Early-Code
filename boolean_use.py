#You own an online shop where you sell rings with custom engravings. You offer both gold plated and solid gold rings.

#Gold plated rings have a base cost of $50, and you charge $7 per engraved unit.
#Solid gold rings have a base cost of $100, and you charge $10 per engraved unit.
#Spaces and punctuation are counted as engraved units.
#Write a function cost_of_project() that takes two arguments:

#engraving - a Python string with the text of the engraving
#solid_gold - a Boolean that indicates whether the ring is solid gold

def cost_of_project(engraving, solid_gold):
    cost = (len(engraving)*7+50)*int(not(solid_gold)) + (len(engraving)*10+100)*int(solid_gold)
    return cost

#haven't learnt if/else statements yet