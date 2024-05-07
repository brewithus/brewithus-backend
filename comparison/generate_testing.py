
from utility import chat, parse_json_string
from utility import save_variable_to_file
import random

# descriptors used to generate random testing data by seeding the prompt randomly
DESCRIPTORS = [
    "Delicious",
    "Fresh",
    "Flavorful",
    "Inviting ambiance",
    "Attentive service",
    "Impeccable presentation",
    "Wide selection",
    "Comfortable seating",
    "Clean environment",
    "Great value for money",
    "Innovative",
    "Cozy atmosphere",
    "Exceptional hospitality",
    "Locally sourced ingredients",
    "Warm and welcoming staff",
    "Exquisite flavors",
    "Charming decor",
    "Memorable dining experience",
    "Consistent quality",
    "Well-paced service",
    "Standard menu",
    "Moderate prices",
    "Convenient location",
    "Casual atmosphere",
    "Average service",
    "Simple decor",
    "Adequate portion sizes",
    "Typical dining experience",
    "Accessible parking",
    "Acceptable cleanliness",
    "Varied menu options",
    "Reasonable wait times",
    "Standard decor",
    "Decent portion sizes",
    "Acceptable ambiance",
    "Friendly staff",
    "Convenient hours",
    "Average prices",
    "Satisfactory cleanliness",
    "Accessible facilities",
     "Decent menu selection",
    "Fair pricing",
    "Clean facilities",
    "Comfortable seating arrangements",
    "Average atmosphere",
    "Standard service",
    "Convenient location",
    "Ordinary decor",
    "Typical menu offerings",
    "Adequate parking facilities",
    "Poor hygiene standards",
    "Unpleasant odor",
    "Slow service",
    "Limited menu options",
    "Uncomfortable seating",
    "High prices for low quality",
    "Inattentive staff",
    "Stale or expired ingredients",
    "Dirty utensils or tableware",
    "Unappetizing presentation",
    "Unsanitary conditions",
    "Rude staff",
    "Limited seating space",
    "Poorly cooked dishes",
    "Unprofessional service",
    "Overpriced menu items",
    "Lack of cleanliness",
    "Inconsistent quality",
    "Long wait times",
    "Unorganized management",
    "Exceptional cuisine",
    "Outstanding service",
    "Warm and inviting atmosphere",
    "Gourmet dishes",
    "Attentive and knowledgeable staff",
    "Elegant decor",
    "Fantastic value for money",
    "Scenic views",
    "Innovative menu offerings",
    "Award-winning chef"

]

def get_random_descriptors(n = 3):
    # NOTE: m = len(DESCRIPTORS)
    descriptors = []

    # NOTE: inefficient for larger n and/or small m
    # NOTE: fine for general application
    for i in range(min(len(DESCRIPTORS), n)):
        descriptor = random.choice(DESCRIPTORS)
        while descriptor in descriptors:
            descriptor = random.choice(DESCRIPTORS)
        descriptors.append(descriptor)

def get_prompt(descriptors):
    

# generate random cafes
def get_random_data(n = 100):
    return []
