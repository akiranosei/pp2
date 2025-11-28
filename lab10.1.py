"""
CREATE TABLE IF NOT EXISTS public.phonebook
(
    id integer NOT NULL DEFAULT nextval('phonebook_id_seq'::regclass),
    name character varying(200) COLLATE pg_catalog."default" NOT NULL,
    phone character varying(20) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT phonebook_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.phonebook
    OWNER to postgres;



Microsoft Windows [Version 10.0.26100.6584]
(c) Microsoft Corporation. All rights reserved.

C:\Program Files\PostgreSQL\18\pgAdmin 4\runtime>"C:\Program Files\PostgreSQL\18\pgAdmin 4\runtime\psql.exe"
 "host=localhost port=5432 dbname=Phonebook user=postgres sslmode=prefer connect_timeout=10" 2>>&1
psql (18.1)
WARNING: Console code page (866) differs from Windows code page (1251)
         8-bit characters might not work correctly. See psql reference
         page "Notes for Windows users" for details.
Type "help" for help.

Phonebook=# \copy phonebook(name, phone) FROM 'C:/Users/User/Downloads/phonbook.csv' DELIMITER ',' CSV HEADE
R;
ERROR:  missing data for column "phone"
CONTEXT:  COPY phonebook, line 2: ""Bilbo Baggins,931737927527""
Phonebook=# \copy phonebook(name, phone) FROM 'C:/Users/User/Downloads/phonb.csv' DELIMITER ',' CSV HEADER;
ERROR:  missing data for column "phone"
CONTEXT:  COPY phonebook, line 2: ""Bilbo Baggins,931737927527""
Phonebook=# \copy phonebook(name, phone) FROM 'C:/Users/User/Downloads/phonb.csv' DELIMITER ',' CSV HEADER;
ERROR:  missing data for column "phone"
CONTEXT:  COPY phonebook, line 2: ""Bilbo Baggins,931737927527""
Phonebook=# \copy phonebook(name, phone) FROM 'C:/Users/User/OneDrive/Рабочий стол/hibye.csv' DELIMITER ','
CSV HEADER;
C:/Users/User/OneDrive/? ЎRзЁc бвR</hibye.csv: No such file or directory
Phonebook=# \copy phonebook(name, phone) FROM 'C:/Users/User/OneDrive/Рабочий стол/hibye.csv' DELIMITER ','
C:/Users/User/OneDrive/? ЎRзЁc бвR</hibye.csv: No such file or directory
Phonebook=# CSV HEADER;
ERROR:  syntax error at or near "CSV"
LINE 1: CSV HEADER;
        ^
Phonebook=# \copy phonebook(name, phone) FROM 'C:/Users/User/Downloads/hibye.csv' DELIMITER ',' CSV HEADER;
C:/Users/User/Downloads/hibye.csv: No such file or directory
Phonebook=# \copy phonebook(name, phone) FROM 'C:/Users/User/Downloads/hibye.csv' DELIMITER ',' CSV HEADER;
ERROR:  missing data for column "phone"
CONTEXT:  COPY phonebook, line 2: ""hi,2981749374""
Phonebook=# \copy phonebook(name, phone) FROM 'C:/Users/User/Downloads/hibye.csv' DELIMITER ',' CSV HEADER;
COPY 2
Phonebook=# \copy phonebook(name, phone) FROM 'C:/Users/User/Downloads/phonb.csv' DELIMITER ',' CSV HEADER;
COPY 14
Phonebook=#
Phonebook=#
Phonebook=#
Phonebook=# DELETE FROM phonebook WHERE name='hi';
DELETE 1
Phonebook=# DELETE FROM phonebook WHERE phone='389429478';
DELETE 1
Phonebook=#
Phonebook=# UPDATE phonebook SET name='Darby' WHERE name='Amanda';
UPDATE 1
Phonebook=#

Phonebook=# SELECT * FROM phonebook;
 id |        name        |      phone
----+--------------------+-----------------
  1 | Alina              | 123456789
  2 | Amina              | 6286862386
  3 | Laura              | 904758134751375
  4 | Dayana             | 832798374938489
  5 | Linda              | 64647282827464
  7 | Luo Binghe         | 919133744
  8 | Shen Qingqiu       | 74783743974
  9 | Shang Qinghua      | 92137489742
 10 | Mo Bei             | 8132747418974
 13 | Bilbo Baggins      | 931737927527
 14 | Thorin Oakenshield | 943175439857398
 15 | Dwalin             | 74839798795
 16 | Balin              | 478593475975
 17 | Ori                | 43957394579375
 18 | Dori               | 74339534954
 19 | Nori               | 4395349579375
 20 | Gloin              | 2739532952595
 21 | Oin                | 3859237592375
 22 | Bifur              | 3927472394732
 23 | Bofur              | 394297492374
 24 | Bombur             | 382387293875
 25 | Fili               | 3847237428397
 26 | Kili               | 3849249273492
  6 | Darby              | 6463728293
(24 rows)

Phonebook=# SELECT * FROM phonebook WHERE name='Bilbo Baggins';
 id |     name      |    phone
----+---------------+--------------
 13 | Bilbo Baggins | 931737927527
(1 row)
"""