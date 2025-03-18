import datetime

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
        # find_user = get_user_model().objects.get(username=username)
        # new_order = Order.objects.create(
        #     user=find_user
        # )
        # # new_order.save()
        # if date:
        #     print(date)
        #     # new_order.created_at = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M")
        #     print(new_order)
        #     Order.objects.filter(pk=new_order.id).update(created_at=date)
        #     print(new_order)


        new_order = Order.objects.create(
            user=get_user_model().objects.get(username=username)
        )

        if date:
            print(date)
            # new_order.created_at = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M")
            print(new_order)
            Order.objects.filter(pk=new_order.id).update(created_at=date)
            print(new_order)


        out_ticket = []
        print(tickets)

        # for ticket in tickets:
        #     out_ticket.append(Ticket(
        #         movie_session_id=ticket["movie_session"],
        #         order=new_order,
        #         row=ticket["row"],
        #         seat=ticket["seat"]
        #     )
        #     )

        # for ticket in tickets:
        #     out_ticket.append(Ticket(
        #         order=new_order,
        #         **ticket
        #     )
        #     )

        for ticket in tickets:

            Ticket.objects.create(
                movie_session_id=ticket["movie_session"],
                order=new_order,
                row=ticket["row"],
                seat=ticket["seat"]
            )


        # Ticket.objects.bulk_create(out_ticket)

def get_orders(
        username: str = None
) -> QuerySet:
    queryset = Order.objects.all()

    if username:
        queryset = queryset.filter(user__username=username)
    return queryset

