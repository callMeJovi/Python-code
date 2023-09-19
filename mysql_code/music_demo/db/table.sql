-- Active: 1687809328456@@127.0.0.1@3306

CREATE DATABASE music_db DEFAULT CHARACTER SET = 'utf8mb4';

use music_db;

# create user table
create TABLE
    t_user(
        id int primary key AUTO_INCREMENT,
        uname VARCHAR(32),
        passwd VARCHAR(32)
    );

# create music TABLE
CREATE TABLE
    t_music(
        id int primary key AUTO_INCREMENT,
        mname VARCHAR(32),
        singer VARCHAR(32),
        path VARCHAR(512)
    );

# create playlist TABLE
CREATE TABLE
    playlist(
        id int primary key AUTO_INCREMENT,
        u_id int,
        m_id int,
        # create foreign key to bond the user id in user_table
        FOREIGN key (u_id) REFERENCES t_user(id),
        FOREIGN key (m_id) REFERENCES t_music(id)
    )