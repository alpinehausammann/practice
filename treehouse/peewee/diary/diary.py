#!/usr/bin/env python3
import sys
import datetime
from clear_screen import *
from collections import OrderedDict
from peewee import *

db = SqliteDatabase('diary.db')


class Entry(Model):
    timestamp=DateTimeField(default=datetime.datetime.now)
    content=TextField()

    class Meta:
        database = db

def initialize():
    """build database and table if they don't exist"""
    db.connect()
    db.create_tables([Entry], safe=True)


def main_menu():
    """While loop for menu."""
    choice = None

    while choice != 'q':
        print("Enter 'q' to quit.")
        for key, value in menu.items():
            print("{}) {}".format(key, value.__doc__))
        choice = input("> ").lower().strip()
        clear_screen()
        if choice in menu:
            menu[choice]()


def create_entry():
    """Create an entry."""
    print("You may now start entry. Enter CTRL-D to exit.")
    data = sys.stdin.read().strip

    if data:
        if input('Save entry?[Y/n] ').lower() != "n":
            Entry.create(content=data)
            print("Save Successful!")
            clear_screen()
        else:
            clear_screen()


def delete_entry():
    """Delete an entry."""


def review_entries():

    entries = Entry.select().order_by(Entry.id)
    for i, entry in enumerate(entries):
        timestamp = entry.timestamp.strftime('%c')
        if i == 0:
            print("\n"," "*int(((len(timestamp)+(len(str(i))+2))/2)-(len("entries")/2)),"Entries",sep="")
            print("_"*int(len(timestamp)+len(str(i))+4),"\n")
            print("{i}. ".format(i=i+1),timestamp)
        else:
            print("{i}. ".format(i=i+1),timestamp)

    print("_"*int(len(timestamp)+len(str(i))+4),"\n")

def review_menu():
    """Review and modify entries."""
    choice = None

    while choice !="q":
        print("Enter 'q' to return to the main menu.")
        review_entries()
        for key, value in modify_menu.items():
            print("{}) {}".format(key, value.__doc__))
        choice=input(">").lower().strip()
        clear_screen()
        if choice in modify_menu:
            modify_menu[choice]()



def modify_entry(entries):
    """Modify an entry."""

def view_entry():
    """View a specific entry."""
    choice = None
    while choice != "q":
        review_entries()
        print("Please enter the number entry you would like to view.\n")
        choice = input("> ")

        view = Entry.select().where(id == choice).get()
        print(view[content])


menu = OrderedDict([
    ('c', create_entry),
    ('r', review_menu),
])

modify_menu = OrderedDict([
    ("v", view_entry),
    ("m", modify_entry),
    ("d", delete_entry),
])


if __name__ == "__main__":
    initialize()
    main_menu()
