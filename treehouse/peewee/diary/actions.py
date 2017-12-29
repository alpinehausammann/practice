from peewee import *


def modify_entry(entries):
    """Modify an entry."""


def view_entry():
    """View a specific entry."""
    choice = None
    while choice != "q":

        review_entries()

        print("Please enter the number entry you would like to view.\n")

        choice = input("> ")

        view = Entry.select().where(Challenge.id == choice).get()

        print(view[content])


def delete_entry():
    """Delete an entry."""


def review_entries():
    """View and manage previous entries"""
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
