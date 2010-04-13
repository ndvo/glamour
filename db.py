# -*- coding: utf-8 -*-
import obj_images
import princess
import pygame
import drapes
import os
import db
import sqlite3
import messages
from pygame.locals import *

def connect_db(url, universe):
        universe.db = db = sqlite3.connect(url)
        universe.db.row_factory = sqlite3.Row
        universe.db_cursor = db_cursor = universe.db.cursor()

def create_save_db(url,name = None, hairback = None, hair = None, skin= None, arm = None, universe = None):
        print "creating or connecting to the database"
        universe.db = db = sqlite3.connect(url)
        universe.db.row_factory = sqlite3.Row
        universe.db_cursor = db_cursor = universe.db.cursor()
        print "creating save table"
        db_cursor.execute("""
          CREATE TABLE save (
              name                VARCHAR(30)    PRIMARY KEY,
              dirt                INTEGER,
              points              INTEGER,
              level               VARCHAR(30),
              position            REAL,
              center_distance     REAL
              );
            """)
        garment = """
              id INTEGER PRIMARY KEY,
              hair_back           REAL,
              skin                VARCHAR(30),
              face                VARCHAR(30),
              hair                VARCHAR(30),
              shoes               VARCHAR(30),
              dress               VARCHAR(30),
              arm                 VARCHAR(30),
              armdress            REAL,
              accessory           VARCHAR(30)
                """
        print "creating garment tables"
        db_cursor.execute("""CREATE TABLE princess_garment("""+ garment +""");""")
        db_cursor.execute("""CREATE TABLE rapunzel("""+ garment + """);""")
        db_cursor.execute("""CREATE TABLE snow_white("""+ garment + """);""")
        db_cursor.execute("""CREATE TABLE cinderella("""+ garment + """);""")
        db_cursor.execute("""CREATE TABLE sleeping_beauty("""+ garment + """);""")
        print "creating stage enemies table"
        db_cursor.execute("""
          CREATE TABLE  stage_enemies (
            id              INTEGER         PRIMARY KEY,
            stage           VARCHAR(30),
            schnauzer       INTEGER,
            carriage        INTEGER,
            butterfly       INTEGER,
            old_lady        INTEGER,
            lion            INTEGER,
            elephant        INTEGER,
            monkey          INTEGER,
            viking_ship     INTEGER,
            footboy         INTEGER,
            bird            INTEGER,
            hawk            INTEGER);
            """)
        print "create messages table"
        db_cursor.execute("""CREATE TABLE messages(
            id              INTEGER     PRIMARY KEY,
            type            VARCHAR(30),
            name            VARCHAR(30),
            message         VARCHAR(600),
            count           INTEGER);
            """)
        [db_cursor.execute("INSERT INTO messages VALUES ("+str(i[0])+",'"+ i[1]+"','"+ i[2]+"','"+ messages.enemy[i[2]].replace("'","''")+"',0);") for i in (
            [1, "enemy", "birdy"],          [2, "enemy", "butterflies"],        [3, "enemy", "carriage"],
        
        [db_cursor.execute("INSERT INTO messages VALUES ("+ str(i[0])+",'"+ i[1]+"','"+ i[2]+"','"+ messages.place[i[2]].replace("'","''")+"',0);") for i in (
            [14,"place", "bathhouse"  ],    [15,"place", "accessory hall"],     [16,"place", "cinderellas castle"],
        [db_cursor.execute("INSERT INTO messages VALUES ("+ str(i[0])+",'"+ i[1]+"','"+ i[2]+"','"+ messages.event[i[2]].replace("'","''")+"',0);") for i in (
            [28,"event", "dirty"],[29,"event", "dirty 2"],[30,"event", "dirty 3"],[31,"event", "save game"],
        [db_cursor.execute("INSERT INTO messages VALUES ("+ str(i[0])+",'"+ i[1]+"','"+ i[2]+"','"+ messages.intro[i[2]].replace("'","''")+"',0);") for i in (
            [46,"intro", "first day a"],[47,"intro", "first day b"],[48,"intro", "first day c"],[49,"intro", "first day d"],
            [54,"intro", "first day i"])]
        db_cursor.execute("INSERT INTO save VALUES('"+name+"', 0 , 0 ,'level','(0,0)',5220)")
        db_cursor.execute("INSERT INTO princess_garment VALUES(1,'"+
                        str(hairback)+"','"+skin+"','face_simple','"+hair+"','shoes_slipper','dress_plain','"+arm+"', 'None','accessory_ribbon')")
        db_cursor.execute("INSERT INTO cinderella VALUES(1,0,'skin_tan','face_eyeshades','hair_cinderella','shoes_crystal', 'dress_red','arm_tan',0,'accessory_shades')")
        db_cursor.execute("INSERT INTO snow_white VALUES(1,0,'skin_pink','face_eyelids','hair_snowwhite','shoes_red','dress_yellow','arm_pink',0,'accessory_purse')")
        db_cursor.execute("INSERT INTO sleeping_beauty VALUES(1,0,'skin_pink','face_simple','hair_sleeping','shoes_slipper','dress_plain','arm_pink',0,'accessory_crown')")
        db_cursor.execute("INSERT INTO rapunzel VALUES(1,1,'skin_pink','face_simple','hair_rapunzel','shoes_white','dress_yellow','arm_pink',0,'accessory_ribbon')")
        db_cursor.execute("INSERT INTO stage_enemies VALUES(1,'BathhouseSt',0,0,1,0,0,0,0,0,0,1,0)")
        db_cursor.execute("INSERT INTO stage_enemies VALUES(2,'AccessorySt',1,0,0,0,0,0,0,0,0,0,0)")
        db_cursor.execute("INSERT INTO stage_enemies VALUES(3,'DressSt',    0,0,0,0,0,0,0,0,0,1,1)")
        db_cursor.execute("INSERT INTO stage_enemies VALUES(4,'MakeupSt',   0,0,0,1,0,0,0,0,0,0,0)")
        db_cursor.execute("INSERT INTO stage_enemies VALUES(5,'ShoesSt',    0,0,0,0,0,0,0,0,1,0,0)")
        db.commit()


