# alx_travel_app_0x00/alx_travel_app/listings/models.py
from django.db import models
from django.contrib.auth.models import User  # Assuming User model for owner/booker/reviewer


class Listing(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    max_guests = models.IntegerField()
    # Assuming an owner for the listing
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='listings')
    amenities = models.TextField(blank=True, null=True)  # e.g., "WiFi, Pool, Parking"
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Booking(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='bookings')
    guest = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    # Statuses could be: pending, confirmed, cancelled, completed
    status = models.CharField(max_length=50, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('listing', 'check_in_date', 'check_out_date')  # Prevent double booking for same dates

    def __str__(self):
        return f"Booking for {self.listing.title} by {self.guest.username}"


class Review(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='reviews')
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])  # 1 to 5 stars
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('listing', 'reviewer')  # One review per user per listing

    def __str__(self):
        return f"Review for {self.listing.title} by {self.reviewer.username} - Rating: {self.rating}"


from django.db import models

# Create your models here.
