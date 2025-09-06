from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import TravelOption, Booking
from .forms import UserRegisterForm, BookingForm

def home(request):
    travels = TravelOption.objects.all()
    ttype = request.GET.get('type') or ''
    src = request.GET.get('source') or ''
    dst = request.GET.get('destination') or ''
    date = request.GET.get('date') or ''
    if ttype: travels = travels.filter(type=ttype)
    if src: travels = travels.filter(source__icontains=src)
    if dst: travels = travels.filter(destination__icontains=dst)
    if date: travels = travels.filter(date_time__date=date)
    return render(request, 'core/travel_list.html', {'travels': travels, 'filters': {'type': ttype, 'source': src, 'destination': dst, 'date': date}})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful.')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'core/register.html', {'form': form})

@login_required
def book_travel(request, pk):
    travel = get_object_or_404(TravelOption, pk=pk)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            if booking.number_of_seats <= 0:
                messages.error(request, 'Number of seats must be positive.'); return redirect('book_travel', pk=pk)
            if booking.number_of_seats > travel.available_seats:
                messages.error(request, 'Not enough seats available.'); return redirect('book_travel', pk=pk)
            booking.user = request.user
            booking.travel_option = travel
            booking.total_price = booking.number_of_seats * travel.price
            travel.available_seats -= booking.number_of_seats
            travel.save(); booking.save()
            messages.success(request, 'Booking confirmed!'); return redirect('my_bookings')
    else:
        form = BookingForm()
    return render(request, 'core/booking_form.html', {'form': form, 'travel': travel})

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user).select_related('travel_option').order_by('-booking_date')
    return render(request, 'core/my_bookings.html', {'bookings': bookings})

@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id, user=request.user)
    if request.method == 'POST':
        if booking.status == 'Confirmed':
            t = booking.travel_option
            t.available_seats += booking.number_of_seats
            t.save()
            booking.status = 'Cancelled'
            booking.save()
            messages.info(request, 'Booking cancelled and seats restored.')
        else:
            messages.warning(request, 'Booking already cancelled.')
    return redirect('my_bookings')
