# alx_travel_app_0x00/alx_travel_app/listings/management/commands/seed.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from listings.models import Listing, Booking, Review
from faker import Faker
import random
from datetime import timedelta, date

class Command(BaseCommand):
    help = 'Seeds the database with sample data for listings, bookings, and reviews.'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Seeding database...'))
        fake = Faker()

        # Clear existing data
        Review.objects.all().delete()
        Booking.objects.all().delete()
        Listing.objects.all().delete()
        User.objects.filter(username__startswith='testuser').delete() # Clear test users

        # Create some test users
        users = []
        for i in range(5):
            user, created = User.objects.get_or_create(
                username=f'testuser{i}',
                defaults={'email': f'testuser{i}@example.com', 'password': 'password123'}
            )
            if created:
                user.set_password('password123') # Hash the password
                user.save()
            users.append(user)
        self.stdout.write(self.style.SUCCESS(f'Created {len(users)} test users.'))

        # Create sample listings
        listings = []
        for _ in range(10):
            owner = random.choice(users)
            listing = Listing.objects.create(
                title=fake.sentence(nb_words=4).replace('.', ''),
                description=fake.paragraph(nb_sentences=5),
                address=fake.street_address(),
                city=fake.city(),
                country=fake.country(),
                price_per_night=random.uniform(50.00, 500.00),
                max_guests=random.randint(1, 10),
                owner=owner,
                amenities=', '.join(random.sample(['WiFi', 'Pool', 'Parking', 'Gym', 'Kitchen', 'TV', 'Air Conditioning'], k=random.randint(1, 5)))
            )
            listings.append(listing)
        self.stdout.write(self.style.SUCCESS(f'Created {len(listings)} listings.'))

        # Create sample bookings
        bookings = []
        for _ in range(20):
            listing = random.choice(listings)
            guest = random.choice(users)
            # Ensure guest is not the owner for a booking
            while guest == listing.owner:
                guest = random.choice(users)

            check_in_date = fake.date_between(start_date='-30d', end_date='+60d')
            check_out_date = check_in_date + timedelta(days=random.randint(1, 7))
            total_price = listing.price_per_night * (check_out_date - check_in_date).days
            status = random.choice(['pending', 'confirmed', 'cancelled', 'completed'])

            try:
                booking = Booking.objects.create(
                    listing=listing,
                    guest=guest,
                    check_in_date=check_in_date,
                    check_out_date=check_out_date,
                    total_price=total_price,
                    status=status
                )
                bookings.append(booking)
            except Exception as e:
                self.stdout.write(self.style.WARNING(f"Skipping booking due to error: {e}"))
                continue # In case of unique_together constraint violation

        self.stdout.write(self.style.SUCCESS(f'Created {len(bookings)} bookings.'))

        # Create sample reviews
        reviews = []
        for _ in range(15):
            listing = random.choice(listings)
            reviewer = random.choice(users)
            # Ensure reviewer is not the owner for a review
            while reviewer == listing.owner:
                reviewer = random.choice(users)

            rating = random.randint(1, 5)
            comment = fake.paragraph(nb_sentences=2) if random.random() > 0.3 else None # Some reviews might not have comments

            try:
                review = Review.objects.create(
                    listing=listing,
                    reviewer=reviewer,
                    rating=rating,
                    comment=comment
                )
                reviews.append(review)
            except Exception as e:
                self.stdout.write(self.style.WARNING(f"Skipping review due to error: {e}"))
                continue # In case of unique_together constraint violation

        self.stdout.write(self.style.SUCCESS(f'Created {len(reviews)} reviews.'))
        self.stdout.write(self.style.SUCCESS('Database seeding complete!'))