#How many total Characters are there?
    A:  entries = Character.objects.all()
        len(entries)

#How many of each subclass?
    A: from charactercreator.models import cleric #etc, all subclasses
        clerics = Cleric.objects.all()
        len(clerics) #useable for any subclass

#How many total items?
    A: from armory.models import *
        items = Item.objects.all()
        len(items)

#How many of the Items are weapons? How many are not?
    from armory.models import *
        weapons = Weapon.objects.all()
        items = Item.objects.all()
        len(weapons)
        len(items) - len(weapons)

#On average, how many Items does each Character have?
    from charactercreator.models import *
        entries = Character.objects.all()
        count = 0
        for char in entries:
            count += len(char.inventory.all())

        count / len(entries) #answer

#On average, how many Weapons does each character have?
    # I believe the data may need to be modified to make this query. The ManyToMany field in the items seems to limit characters to only have Item class weapons, not Weapon class.
        
