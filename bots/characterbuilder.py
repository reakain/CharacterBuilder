import random
import pycorpora
import inflect

inf = inflect.engine()
print(pycorpora.get_files('materials'))
# Character statics
namesMin = 1
namesMax = 6
firstNames = pycorpora.humans.firstNames['firstNames']
lastNames = pycorpora.humans.lastNames['lastNames']
middleNames = firstNames + lastNames
genders = [
    "male",
    "female",
    "non-binary",
    "neuter",
    "genderless"
]
familySizeMin = 0
familySizeMax = 15
familyMemberRelations = ["grandparent","parent","child","grandchild","sibling"]
descriptorList = pycorpora.humans.descriptions['descriptions']
descriptorsMin = 3
descriptorsMax = 8
occupations = pycorpora.humans.occupations['occupations']
hobbyList = [ 
    "pottery",
    "woodworking",
    "metalworking",
    "programming",
    "writing",
    "scrapbooking",
    "making costumes",
    "photography",
    "making Christmas decorations",
    "painting",
    "sketching",
    "movie making",
    "coin collecting",
    "stamp collecting",
    "bird watching",
    "reading",
    "theatre",
    "gambling",
    "visiting museums",
    "hiking",
    "bicycling",
    "running",
    "weight lifting",
    "fencing",
    "soccer",
    "sightseeing"
    ]
hobbyMin = 0
hobbyMax = 20

# Country statics
countryNames = firstNames
cityNames = firstNames
govTypes = ["Autocracy",
        "Democracy",
        "Oligarchy",
        "Anarchy",
        "Confederation",
        "Federation",
        "Unitary State",
        "Demarchy",
        "Electocracy",
        "Constitutial Republic",
        "Democratic Republic",
        "Parliamentary Republic",
        "Republic",
        "Theocracy",
        "Plutocracy",
        "Technocracy",
        "Absolute Monarchy",
        "Dictatorship",
        "Constitutional Monarchy",
        "City-State",
        "Commune",
        "Empire",
        "Colony"]
countryPopMin = 1000
countryPopMax = 1000000000
importExportList = pycorpora.materials['layperson-metals']['layperson metals']
importExportList += pycorpora.materials['natural-materials']['natural materials']
countryExportsMin = 0
countryExportMax = 5
countryImportsMin = 0
countryImportsMax = 5
geoFeaturesMin = 1
geoFeaturesMax = 4
geoFeaturesList = pycorpora.geography.geographic_features['entries']
geoFeatureNames = firstNames


class GeoFeature(object):
    def __init__(self):
        self.type = random.choice(geoFeaturesList)
        self.name = random.choice(geoFeatureNames)

class Country(object):
    def __init__(self):
        self.name = ""
        self.features = []
        self.govType = ""
        self.exports = []
        self.imports = []
        self.population = 0
        self.capital = ""
    
    def build_country(self):
        self.name = random.choice(countryNames)
        self.population = random.randint(countryPopMin,countryPopMax)
        self.capital = random.choice(cityNames)
        self.govType = random.choice(govTypes)
        num_feat = random.randint(geoFeaturesMin,geoFeaturesMax)
        for x in range(num_feat):
            self.features.append(GeoFeature())
        self.imports = self.build_list(countryImportsMin,countryImportsMax,importExportList)
        self.exports = self.build_list(countryExportsMin,countryExportMax,importExportList)

    def country_bio(self):
        info = "Name: " + self.name.capitalize() + "\n" \
            + "Population: " + str(self.population) + "\n" \
            + "Government: " + self.govType.capitalize() + "\n" \
            + "Capital: " + self.capital.capitalize() + "\n" \
            + "Description: " + self.desc() + "\n" \
            + "Exports: " + inf.join(self.exports).capitalize() + "\n" \
            + "Imports: " + inf.join(self.imports).capitalize()
        return info

    def desc(self):
        countrySize = ""
        if(self.population <= int(countryPopMax/3)):
            countrySize = "small"
        elif (self.population > int(countryPopMax - countryPopMax/3)):
            countrySize = "large"
        else:
            countrySize = "medium"
        desc = "{} is a {} {} nation. The {} {} is a notable landmark" \
            + " near the capital."
        
        desc_full = desc.format(self.name.capitalize(), countrySize, self.govType, \
            self.features[0].name.capitalize(), self.features[0].type)
        return desc_full


    def build_list(self, min, max, full_list):
        num = random.randint(min,max)
        buildList = []
        
        if(num == 0):
            buildList.append("None")
            return buildList
        
        buildList.append(random.choice(full_list))
        for x in range(num-1):
            buildList.append(self.get_check_list(buildList,full_list))
        return buildList

    def get_check_list(self, build_list, full_list):
        new_item = random.choice(full_list)
        while new_item in build_list:
            new_item = random.choice(full_list)
        return new_item


class Gender(object):
    def __init__(self):
        self.gender = ""
        self.they = ""
        self.them = ""
        self.their = ""

class Character(object):
    def __init__(self):
        self.names = []
        self.gender = ""
        self.age = ""
        self.race = ""
        self.occupation = ""
        self.country = Country()
        self.hobbies = []
        self.descriptors = []
        self.family = []

    def build_character(self, family = True):
        self.build_name()
        self.age = random.randint(1,1000)
        self.gender = random.choice(genders)
        self.occupation = random.choice(occupations)
        self.descriptors = self.build_list(descriptorsMin,descriptorsMax,descriptorList)
        self.country.build_country()
        self.hobbies = self.build_list(hobbyMin,hobbyMax,hobbyList)
        if family:
            self.build_family()

    def build_family(self):
        num = random.randint(familySizeMin,familySizeMax)
        family_list = []
        for x in range(num):
            member = Character()
            member.build_character(False)
            family_list.append((member,random.choice(familyMemberRelations)))
        self.family = family_list


    def build_list(self, min, max, full_list):
        num = random.randint(min,max)
        buildList = []
        if(num == 0):
            buildList.append("None")
            return buildList

        buildList.append(random.choice(full_list))
        for x in range(num-1):
            buildList.append(self.get_check_list(buildList,full_list))
        return buildList

    def build_name(self):
        num = random.randint(namesMin-1,namesMax-1)
        self.names.append(random.choice(firstNames))

        for x in range(num):
            if x != num-1:
                new_name = self.get_check_list(self.names, middleNames)
            else:
                new_name = self.get_check_list(self.names, lastNames)
            
            self.names.append(new_name)

    def get_check_list(self, build_list, full_list):
        new_item = random.choice(full_list)
        while new_item in build_list:
            new_item = random.choice(full_list)
        return new_item
    
    def full_name(self):
        return " ".join(self.names)
    
    def family_info(self):
        fam_info = ""
        if(len(self.family) == 0):
            return "    None\n"

        for fam in self.family:
            fam_info += "    " + fam[1].capitalize() + ": " + fam[0].full_name() + "\n"

        return fam_info

    def character_bio(self):
        info = "Name: " + self.full_name() + "\n" \
            + "Age: " + inf.number_to_words(self.age).capitalize() + "\n" \
            + "Gender: " + self.gender.capitalize() + "\n" \
            + "Occupation: " + self.occupation.capitalize() + "\n" \
            + "Race: " + "\n" \
            + "Country: " + self.country.name.capitalize() + "\n" \
            + "Family: " + "\n" + self.family_info() \
            + "Qualities: " + inf.join(self.descriptors).capitalize() + "\n" \
            + "Hobbies: " + inf.join(self.hobbies).capitalize()

        return info

if __name__ == "__main__":
    charry = Character()
    charry.build_character()
    print(charry.character_bio())
    print(charry.country.country_bio())