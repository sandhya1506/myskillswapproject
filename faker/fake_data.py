import os
import sys
import django
import random
from faker import Faker
from faker.providers import DynamicProvider

# TC, CR, LN, OT

TC_provider = DynamicProvider(
     provider_name="Technical",
     elements=["Python", "Physics", "Math", "Electrical Engineering", "Computer Science", "C programming", "AGI"],
)
CR_provider = DynamicProvider(
     provider_name="Craft",
     elements=["Sewing", "Sculpting", "Painting", "Origami", "Set Design", "Woodcarving", "Knitting"],
)

LN_provider = DynamicProvider(
    provider_name ="Language",
    elements=["English", "Swedish", "Spanish", "Chinese", "Hindi", "Urdu", "French"],
)

OT_provider = DynamicProvider(
    provider_name ="Others",
    elements=["Violin", "Weight Lifting", "Job Search", "Communication", "Leadership", "Habits", "Meditation"],
)

category_provider = DynamicProvider(
    provider_name="category",
    elements=["TC", "CR", "LN", "OT"],
)

fake = Faker()

# then add new provider to faker instance
fake.add_provider(TC_provider)
fake.add_provider(CR_provider)
fake.add_provider(LN_provider)
fake.add_provider(OT_provider)
fake.add_provider(category_provider)

# now you can use:

# Django setup environment
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.insert(0, project_root)


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "skillswap.settings")
django.setup()

from user_authentication.models import UserProfile
from skills.models import AddSkills, RequestSkills
from contactapp.models import ContactMessage
from reviewsapp.models import Review



def create_fake_data(num_users=4, num_skills=4, num_reviews=4, num_contacts=2):

    for _ in range(num_users):
        username = fake.user_name()
        email = fake.unique.email()
        password = fake.sentence(8, 20)
        UserProfile.objects.create(
            username=username,
            email=email,
            password=password,
        )
        users = list(UserProfile.objects.all())

    for _ in range(num_skills):
        user = random.choice(users)
        date = fake.date()
        cat = fake.category()
        title = fake.cat()
        availability = fake.pybool()
        location = fake.country()
        description = fake.sentence()
        AddSkills.objects.create(
            user=user,
            date=date,
            category=cat,
            title=title,
            availability=availability,
            location=location,
            description=description
        )
        skills = list(AddSkills.objects.all())
    
    for _ in range(num_contacts):
        sender = random.choice(users)
        recipient = random.choice(users)
        skill = random.choice(skills)
        email = sender.user.email
        submitted_add = fake.date()
        ContactMessage.objects.create(
            sender=sender,
            recipient=recipient,
            skill=skill,
            email=email,
            submitted_add=submitted_add
        )
        messages = list(ContactMessage.objects.all())

    for _ in range(num_reviews):
        skill = random.choice(skills)
        name = skill.user.username
        email = skill.user.email
        rating = random.randrange(0,6)
        comment = fake.sentence()
        created_at = fake.date()
        Review.objects.create(
            name=name,
            skill=skill,
            email=email,
            rating=rating,
            comment=comment,
            created_at=created_at
        )



        
    print(f"Created {num_users} user profiles with {num_skills} skills, written {num_reviews} and created {num_contacts} of contacts.")

if __name__ == "__main__":
    create_fake_data()