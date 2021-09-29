from sqlalchemy import insert, create_engine

engine = create_engine('sqlite:///db.sqlite', echo=True)

connection = engine.connect()

def add_reminder():
    connection.execute(
        insert('reminders').values(
            id=10,
            remind_msg="Gello",
        )
    )

add_reminder()