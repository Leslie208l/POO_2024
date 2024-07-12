-- CREATE DATABASE IF NOT EXISTS bd_notas;
-- use bd_notas;

-- create table usuarios(
--    id int(25) auto_increment not null, 
--     nombre varchar(100),
--     apellidos varchar(100),
--     email varchar(100),
--     password varchar(100),
--     fecha date not null,
--     CONSTRAINT pk_usuarios primary key (id),
--     CONSTRAINT uq_email  unique(email)
-- )engine=InnoDB;


-- create table notas(
--    id int(25) auto_increment not null,
--    usuario_id  int(25) not null,
--    titulo varchar(200) not null,
--    descripcion mediumtext,
--    fecha date not null,
--    CONSTRAINT pk_notas primary key (id),
--    CONSTRAINT fk_notas_usuarios foreign key(usuario_id) references usuarios(id)
-- )engine=InnoDB;