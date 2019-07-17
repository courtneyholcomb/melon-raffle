"""Randomly pick customer and print customer info"""

from random import choice
from customers import get_customers_from_file


def pick_winner(customers):
    """Choose a random winner from list of customers."""

    chosen_customer = choice(customers)

    print(f"Tell {chosen_customer.name} at {chosen_customer.email} "\
           "that they've won")


def run_raffle():
    """Run the weekly raffle."""

    customers = get_customers_from_file("customers.txt")
    pick_winner(customers)


if __name__ == "__main__":
    run_raffle()