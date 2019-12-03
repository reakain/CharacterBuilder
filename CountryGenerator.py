import random
import pycorpora
import inflect

inf = inflect.engine()

# Country statistics
countryNames = pycorpora.humans.firstNames['firstNames']
cityNames = countryNames
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
geoFeatureNames = countryNames


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



if __name__ == "__main__":
    nation = Country()
    nation.build_country()
    print(nation.country_bio())