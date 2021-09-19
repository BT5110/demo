from collections import namedtuple


def namedtuplefetchall(cursor):
    "Return all rows from a cursor as a namedtuple"
    nt_result = namedtuple('Result', [col[0] for col in cursor.description])
    return [nt_result(*row) for row in cursor.fetchall()]
