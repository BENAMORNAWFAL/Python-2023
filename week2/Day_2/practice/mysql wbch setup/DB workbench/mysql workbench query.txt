SELECT * FROM names;

INSERT INTO names(id, name, created_at, updated_at)
value (1,'nawfal',now(),now());

INSERT INTO names(name, created_at, updated_at)
value ('aymen',now(),now()),('mourad',now(),now()),('yassine',now(),now());

update  names
set name='alii'
where id=4;

delete from names
where id=2;