from django.db.models import QuerySet

from db.models import MovieSession, Ticket, Order
from django.contrib.auth import get_user_model
from django.db import transaction

def create_order(
        tickets: list,
        username: str,
        date: str=None

):
    with transaction.atomic():
        find_user = get_user_model().objects.get(username=username)
        new_order = Order(
            user=find_user
        )
        if date:
            new_order.created_at = date
        new_order.save()
        out_ticket = []

        for ticket in tickets:
            out_ticket.append(Ticket(
                movie_session=ticket["rows"],
                order=new_order,
                row=ticket["row"],
                seat=ticket["seat"]
            )
            )

        Ticket.objects.bulk_create(out_ticket)

def get_orders(
        username: str = None
) -> QuerySet:
    queryset = Order.objects.all()

    if username:
        queryset = queryset.filter(user__username=username)
    return queryset

