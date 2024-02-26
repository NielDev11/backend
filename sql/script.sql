create database backend

use backend

create table modulo(
    id int auto_increment,
    nombre varchar(30) unique not null,
    descripcion text not null,
    primary key(id)
)

create table perfil(
    id int auto_increment,
    nombre varchar(30) unique not null,
    descripcion text not null,
    primary key(id)
)

create table atributo(
    id int auto_increment,
    nombre varchar(30) unique not null,
    descripcion text not null,
    primary key(id)
)

create table nivel(
    id int auto_increment,
    nombre varchar(30) unique not null,
    descripcion text not null,
    primary key(id)
)

create table competencia(
    id int auto_increment,
    nombre varchar(30) unique not null,
    descripcion text not null,
    primary key(id)
)

create table tipoevaluacion(
    id int auto_increment,
    nombre varchar(30) unique not null,
    descripcion text not null,
    primary key(id)
)


create table moduloxperfil(
    id int auto_increment,
    idmodulo int not null,
    idperfil int not null,
    descripcion text not null,
    primary key(id),
    foreign key(idmodulo) references modulo(id),
    foreign key(idperfil) references perfil(id)
)


create table usuario(
    id int auto_increment,
    usuario varchar(30) unique not null,
    contrasena varchar(100) not null,
    nombres varchar(20) not null,
    apellido1 varchar(20) not null,
    apellido2 varchar(20) not null,
    tipodocumento varchar(20) not null,
    identificacion varchar(20) unique not null,
    telefono varchar(20) not null,
    idperfil int not null,
    primary key(id),
    foreign key(idperfil) references perfil(id)
)

create table cargo(
    id int auto_increment,
    nombre varchar(30) unique not null,
    descripcion text not null,
    idnivel int not null,
    primary key(id),
    foreign key(idnivel) references nivel(id)
)


create table comportamiento(
    id int auto_increment,
    nombre varchar(30) unique not null,
    descripcion text not null,
    idcompetencia int not null,
    primary key(id),
    foreign key(idcompetencia) references competencia(id)
)

create table bancopregunta(
    id int auto_increment,
    idnivel int not null,
    idcomportamiento int not null,
    pregunta text not null,
    primary key(id),
    foreign key(idnivel) references nivel(id),
    foreign key(idcomportamiento) references comportamiento(id)
)


create table facultad(
    id int auto_increment,
    nombre varchar(30) unique not null,
    descripcion text not null,
    primary key(id)
)

create table programa(
    id int auto_increment,
    nombre varchar(30 )unique not null,
    descripcion text not null,
    idfacultad int not null,
    primary key(id),
    foreign key(idfacultad) references facultad(id)
)

create table asignatura(
    id int auto_increment,
    nombre varchar(30) unique not null,
    codigo varchar(30) not null,
    descripcion text not null,
    idprograma int not null,
    primary key(id),
    foreign key(idprograma) references programa(id)
)

create table grupo(
    id int auto_increment,
    nombre varchar(30) unique not null,
    descripcion text not null,
    idasignatura int not null,
    primary key(id),
    foreign key(idasignatura) references asignatura(id)
)

create table evaluacionadmon(
    id int auto_increment,
    idtrabajador int not null,
    idjefe int not null,
    idcargo int not null,
    fecha date not null,
    periodo varchar(30) not null,
    idtipoevaluacion int not null, 
    primary key(id),
    foreign key(idtrabajador) references usuario(id),
    foreign key(idjefe) references usuario(id),
    foreign key(idcargo) references cargo(id),
    foreign key(idtipoevaluacion) references tipoevaluacion(id)
    
)

create table detalleevadmon(
    id int auto_increment,
    idevaluacionadmon int not null,
    idbancopregunta int not null,
    calificacion int not null,
  
    primary key(id),
    foreign key(idevaluacionadmon) references evaluacionadmon(id),
    foreign key(idbancopregunta) references bancopregunta(id)
    
)

create table evaluaciondoc(
    id int auto_increment,
    iddocente int not null,
    periodo varchar(30) not null,
    idtipoevaluacion int not null, 
    primary key(id),
    foreign key(iddocente) references usuario(id),
    foreign key(idtipoevaluacion) references tipoevaluacion(id)
    
)

create table eva_doc_asig_est(
    id int auto_increment,
    idestudiante int not null,
    idgrupo int not null,
    fecha date,
    idevaluaciondoc int not null,
    primary key(id),
    foreign key(idestudiante) references usuario(id),
    foreign key(idgrupo) references grupo(id),
    foreign key(idevaluaciondoc) references evaluaciondoc(id)
    
)

create table detalleevadoc(
    id int auto_increment,
    ideva_doc_asig_est int not null,
    idbancopregunta int not null,
    calificacion int not null,
    primary key(id),
    foreign key(ideva_doc_asig_est) references eva_doc_asig_est(id),
    foreign key(idbancopregunta) references bancopregunta(id)
    
)


create table eva_doc_director(
    id int auto_increment,
    idejefe int not null,
    fecha date,
    idevaluaciondoc int not null,
    primary key(id),
    foreign key(idejefe) references usuario(id),
    foreign key(idevaluaciondoc) references evaluaciondoc(id)
    
)

create table detalle_evadoc_director(
    id int auto_increment,
    ideva_doc_director int not null,
    idbancopregunta int not null,
    calificacion int not null,
    primary key(id),
    foreign key(ideva_doc_director) references eva_doc_director(id),
    foreign key(idbancopregunta) references bancopregunta(id)
    
)