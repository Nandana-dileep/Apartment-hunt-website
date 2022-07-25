"""Defines all the functions related to the database"""
from app import db

#all this should do is create the initial list, a bunch of apartment offers. 
#It can be reproduced by searching for rooms with nothing in the search field.
#This block is the basic way for the functions to take their query outputs and display
#   them on the home page.

conn = db.connect()
query_results = conn.execute("SELECT u.id AS offerId, p.email, u.rentCost, u.moveIn, b.address, b.city, b.state, b.zip FROM Units u JOIN Buildings b ON u.unitOf=b.id JOIN Providers p ON u.postedBy=p.id WHERE NOT EXISTS (SELECT * FROM Tracking t WHERE t.trackedUnit = u.id AND t.accepted>0);").fetchall()
conn.close()
currAttr = ["Offer Id", "Contact Email", "Rent", "Move-in Date", "Address", "City", "State", "ZIP"]
currTuples = [currAttr, []] #the currtuples return object is 2 arrays, first array is the names of the attributes, second array is the data.
for result in query_results:
    currTuples[1].append(result)

def fetch_todo() -> dict:
    """Reads all tasks listed in the todo table

    Returns:
        A list of dictionaries
    """
    # this is how I created the currTuples, but I am not sure how I will get it to start if it doesn't have currTuples to start with
    # conn = db.connect()
    # query_results = conn.execute("SELECT u.id AS offerId, p.email, u.rentCost, u.moveIn, b.address, b.city, b.state, b.zip FROM Units u JOIN Buildings b ON u.unitOf=b.id JOIN Providers p ON u.postedBy=p.id WHERE NOT EXISTS (SELECT * FROM Tracking t WHERE t.trackedUnit = u.id AND t.accepted>0);").fetchall()
    # conn.close()
    # currAttr = ["Offer Id", "Contact Email", "Rent", "Move-in Date", "Address", "City", "State", "ZIP"]
    # currTuples = [currAttr, []] #the currtuples return object is 2 arrays, first array is the names of the attributes, second array is the data.
    # for result in query_results:
    #     currTuples[1].append(result)

    return currTuples


def update_task_entry(task_id: int, text: str) -> None:
    """Updates task description based on given `task_id`

    Args:
        task_id (int): Targeted task_id
        text (str): Updated description

    Returns:
        None
    """

    conn = db.connect()
    query = 'Update tasks set task = "{}" where id = {};'.format(text, task_id)
    conn.execute(query)
    conn.close()


def update_status_entry(task_id: int, text: str) -> None:
    """Updates task status based on given `task_id`

    Args:
        task_id (int): Targeted task_id
        text (str): Updated status

    Returns:
        None
    """

    conn = db.connect()
    query = 'Update tasks set status = "{}" where id = {};'.format(text, task_id)
    conn.execute(query)
    conn.close()


def insert_new_task(text: str) ->  int:
    """Insert new task to todo table.

    Args:
        text (str): Task description

    Returns: The task ID for the inserted entry
    """

    conn = db.connect()
    query = 'Insert Into tasks (task, status) VALUES ("{}", "{}");'.format(
        text, "Todo")
    conn.execute(query)
    query_results = conn.execute("Select LAST_INSERT_ID();")
    query_results = [x for x in query_results]
    task_id = query_results[0][0]
    conn.close()

    return task_id


def remove_task_by_id(task_id: int) -> None:
    """ remove entries based on task ID """
    conn = db.connect()
    query = 'Delete From tasks where id={};'.format(task_id)
    conn.execute(query)
    conn.close()
