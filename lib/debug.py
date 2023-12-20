#!/usr/bin/env python3

from config import CONN, CURSOR
from song import Song


if __name__ == '__main__':
    import ipdb; ipdb.set_trace()

from lib import CONN, CURSOR
from lib.song import Song

def reset_db():
    Song.drop_table()
    Song.create_table()
    

import pytest; pytest.set_trace()

