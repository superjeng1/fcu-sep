DROP TABLE IF EXISTS student;
DROP TABLE IF EXISTS course;
DROP TABLE IF EXISTS class;
DROP TABLE IF EXISTS selection;

CREATE TABLE student (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE course (
  id INTEGER PRIMARY KEY NOT NULL,
  name TEXT NOT NULL,
  teacher_name TEXT NOT NULL,
  description TEXT NOT NULL
);

INSERT INTO course (id, name, teacher_name, description) VALUES (0, '軟體工程開發實務', '陳錫民', '介紹軟體工程基本的原則與觀念。學生修習此課後可以學習到軟體工程紀律、專案管理、需求、設計、測試、版本管理及軟體維護等基本觀念。學生可以透過操作軟體工程工具的方式學習這些概念。');
INSERT INTO course (id, name, teacher_name, description) VALUES (1, '網路程式設計', '陳烈武', '介紹各種主從式架構下網路程式之設計實作技巧');

CREATE TABLE class (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  course_id INTEGER NOT NULL,
  timeOfDay INTEGER NOT NULL,
  dayOfWeek INTEGER NOT NULL,
  FOREIGN KEY (course_id) REFERENCES course (id)
);

INSERT INTO class (course_id, timeOfDay, dayOfWeek) VALUES (0, 3, 1);
INSERT INTO class (course_id, timeOfDay, dayOfWeek) VALUES (0, 4, 1);
INSERT INTO class (course_id, timeOfDay, dayOfWeek) VALUES (1, 6, 2);
INSERT INTO class (course_id, timeOfDay, dayOfWeek) VALUES (1, 7, 2);

CREATE TABLE selection (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  course_id INTEGER NOT NULL,
  student_id INTEGER NOT NULL,
  FOREIGN KEY (course_id) REFERENCES course (id)
  FOREIGN KEY (student_id) REFERENCES student (id)
);

INSERT INTO selection (course_id, student_id) VALUES (0, 1);
INSERT INTO selection (course_id, student_id) VALUES (1, 1);
