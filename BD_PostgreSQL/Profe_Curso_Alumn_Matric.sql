select * from profesores;
select * from cursos;
select * from alumnos;
select * from matriculas; 

--Insert table profesores
INSERT INTO profesores(id,name,last_name,email) VALUES (1, 'Paul', 'Rodriguez', 'paul1992@gmail.com');
INSERT INTO profesores(id,name,last_name,email) VALUES (2, 'James', 'Polo', 'james524@gmail.com');
INSERT INTO profesores(id,name,last_name,email) VALUES (3, 'Pavel', 'Burgos', 'pavel384@gmail.com');
INSERT INTO profesores(id,name,last_name,email) VALUES (4, 'Piero', 'Ulloa', 'piero2006@gmail.com');

--insert table cursos
INSERT INTO cursos(id,name,id_profesor) VALUES (1,'Lenguaje',3);
INSERT INTO cursos(id,name,id_profesor) VALUES (2,'Matematicas',4);
INSERT INTO cursos(id,name,id_profesor) VALUES (3,'Quimica',1);

--inserte table alumnos
INSERT INTO alumnos(id,name,last_name,email) VALUES(1,'Elvis','Cotrina','elvis06@gmail.com');
INSERT INTO alumnos(id,name,last_name,email) VALUES(2,'Darlin','Cotrina','darlin07@gmail.com');
INSERT INTO alumnos(id,name,last_name,email) VALUES(3,'Juan','Roldan','juan134@gmail.com');
INSERT INTO alumnos(id,name,last_name,email) VALUES(4,'Frack','Baltazar','baltazar28@gmail.com');

-- insert table matriculas
INSERT INTO matriculas(id,alumno_id,curso_id) VALUES(1,4,2);
INSERT INTO matriculas(id,alumno_id,curso_id) VALUES(2,2,1);
INSERT INTO matriculas(id,alumno_id,curso_id) VALUES(3,3,2);
INSERT INTO matriculas(id,alumno_id,curso_id) VALUES(4,1,3);

--Mostrar el nombre, apellido y que curso enseña cada profesor

select profesores.name as nombre_profesor , profesores.last_name as apellido_profesor ,
cursos.name as curso from cursos
JOIN profesores ON profesores.id = cursos.id_profesor;

-- Mostrar en que cursos se encuentran matriculados cada alumno

SELECT alumnos.name as nombre, alumnos.last_name as apellido,
cursos.name as curso_matriculado From matriculas
JOIN alumnos ON alumnos.id = matriculas.alumno_id
JOIN cursos ON cursos.id = matriculas.curso_id;

-- Mostrar solo los alumnos matriculados a 'matematicas'

SELECT alumnos.name, cursos.name FROM matriculas
JOIN alumnos ON alumnos.id = matriculas.alumno_id
JOIN cursos ON cursos.id = matriculas.curso_id
WHERE cursos.name = 'Matematicas';