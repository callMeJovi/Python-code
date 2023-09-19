use music_db;

# add user information insert into t_user 
insert into t_user
VALUES(0, 'bz', '123');

-- # get user's playlist

-- SELECT m.mname from playlist p left join t_music m on p.m_id=m.id where u_id=1;

# get path of the music according to the name
select m.path
from t_music m
    left join playlist p on p.m_id = m.id
where u_id = 1 and m.mname = 'blue';