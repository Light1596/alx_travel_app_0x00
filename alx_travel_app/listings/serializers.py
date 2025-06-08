# alx_travel_app_0x00/alx_travel_app/listings/serializers.py
from rest_framework import serializers
from .models import Listing, Booking, Review

class ListingSerializer(serializers.ModelSerializer):
    owner_username = serializers.ReadOnlyField(source='owner.username') # To display owner's username

    class Meta:
        model = Listing
        fields = [
            'id', 'title', 'description', 'address', 'city', 'country',
            'price_per_night', 'max_guests', 'owner', 'owner_username',
            'amenities', 'created_at', 'updated_at'
        ]
        read_only_fields = ['owner'] # Owner will be set by the view based on logged-in user

class BookingSerializer(serializers.ModelSerializer):
    listing_title = serializers.ReadOnlyField(source='listing.title')
    guest_username = serializers.ReadOnlyField(source='guest.username')

    class Meta:
        model = Booking
        fields = [
            'id', 'listing', 'listing_title', 'guest', 'guest_username',
            'check_in_date', 'check_out_date', 'total_price', 'status',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['guest', 'total_price', 'status'] # Guest and total_price will be set by the view

class ReviewSerializer(serializers.ModelSerializer):
    reviewer_username = serializers.ReadOnlyField(source='reviewer.username')
    listing_title = serializers.ReadOnlyField(source='listing.title')

    class Meta:
        model = Review
        fields = [
            'id', 'listing', 'listing_title', 'reviewer', 'reviewer_username',
            'rating', 'comment', 'created_at'
        ]
        read_only_fields = ['reviewer']