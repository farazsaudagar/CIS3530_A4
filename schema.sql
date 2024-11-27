drop table if exists department, dependent, dept_location, employee, project, works_on;

CREATE TABLE Employee(
      Fname VARCHAR(10) NOT NULL,
      Minit CHAR NOT NULL,
      Lname VARCHAR(10) NOT NULL,
      SSN CHAR(9) NOT NULL,
      Address VARCHAR(15) NOT NULL,
      Sex CHAR NOT NULL,
      Salary INT NOT NULL,
      Super_ssn CHAR(9) NOT NULL,
      Dno INT NOT NULL,
      BDate DATE,
      EmpDate DATE,
      PRIMARY KEY(Ssn),
      UNIQUE(Fname, Lname)
        );


INSERT INTO EMPLOYEE VALUES 
('Mary', 'J', 'Hind', '100040001', 'Dundas, ON', 'F', 333000, '333445555', 5,  '1997-01-19',  '2018-05-25'),
('Harry', 'O', 'Potter', '105947378', 'London,, On', 'M', 43000, '460836586', 1,  '1993-06-10',  '2014-07-01'),
('Sebastian', 'T', 'Kuras', '111111111', 'Houston, TX', 'M', 90000, '999999999', 5,  '1965-05-19',  '1985-09-14'),
('Alex', 'E', 'Vermeulen', '111222333', 'Dundas, ON', 'F', 150000, '888665555', 5,  '1992-04-01',  '2014-09-29'),
('John', 'B', 'Smith', '123456789', 'Houston, TX', 'M', 60000, '333445555', 5,  '1980-09-01',  '2004-11-06'),
('Victoria', 'J', 'Smith', '198782427', 'Guelph, ON', 'F', 127000, '444555777', 2,  '1987-06-14',  '2007-08-30'),
('Tamara', 'E', 'Walters', '198928552', 'Hamilton, ON', 'F', 980000, '888665555', 4,  '1967-11-17',  '1989-07-20'),
('Jessica', 'A', 'Jonesboro', '199098293', 'Guelph, ON', 'F', 164000, '460836586', 11,  '1969-06-12',  '1993-09-10'),
('Keane', 'W', 'Saunders', '199171129', 'London, ON', 'F', 180000, '333445555', 5,  '1993-07-09',  '2016-09-24'),
('Samuel', 'C', 'Anderson', '199196331', 'Paris, ON', 'M', 240000, '925468826', 24,  '1999-12-19',  '2020-08-29'),
('Andrea', 'R', 'Austin', '199302835', 'Hamilton, ON', 'M', 160000, '333445555', 5,  '1963-08-30',  '1983-12-03'),
('Fahad', 'Y', 'Selles', '199305628', 'Guelph, ON', 'M', 40000, '999999999', 5,  '1974-01-11',  '1996-04-11'),
('Jack', 'U', 'Nicholson', '199489442', 'Guelph, ON', 'M', 80000, '888665555', 5,  '1994-05-31',  '2019-02-25'),
('Robert', 'I', 'De Niro', '199608611', 'Hamilton, ON', 'M', 100000, '987654321', 4,  '1976-08-26',  '2000-07-10'),
('Jennifer', 'X', 'Armstrong', '199685000', 'Guelph, ON', 'F', 130000, '888665555', 7,  '1993-08-06',  '2017-10-14'),
('Rajan', 'C', 'Patel', '199705791', 'Paris, ON', 'M', 164000, '888665555', 11,  '1982-12-02',  '2006-12-17'),
('Emily', 'V', 'Asher', '199923690', 'London, ON', 'F', 10000, '999999999', 5,  '1985-04-22',  '2006-01-30'),
('Elizabeth', 'N', 'Asling', '200002511', 'Hamilton, ON', 'F', 227000, '444555777', 2,  '1975-08-02',  '1997-03-14'),
('Claire', 'D', 'Atkins', '200178650', 'Guelph, ON', 'M', 27000, '444555777', 2,  '1997-08-21',  '2022-07-03'),
('Al', 'F', 'Pacino', '200243095', 'Hamilton, ON', 'M', 150000, '333445555', 5,  '1989-04-15',  '2010-03-18'),
('Tom', 'E', 'Hanks', '200352295', 'Paris, ON', 'M', 197000, '807844760', 4,  '1977-10-29',  '1998-11-07'),
('Dustin', 'Y', 'Hoffman', '200369792', 'Guelph, ON', 'M', 50000, '333445555', 5,  '1987-03-03',  '2010-12-14'),
('Brad', 'A', 'Pitt', '200493155', 'London, ON', 'M', 97000, '444555777', 2,  '1982-01-19',  '2002-11-06'),
('Anthony', 'S', 'Hopkins', '200587814', 'Hamilton, ON', 'M', 170000, '444555777', 2,  '1977-07-20',  '2000-04-20'),
('Marlon', 'X', 'Brando', '200626576', 'Guelph, ON', 'F', 56000, '359624751', 11,  '1970-11-26',  '1992-09-20'),
('Jessica', 'C', 'Austin', '200757441', 'Guelph, ON', 'F', 123000, '444555777', 2,  '1998-03-09',  '2019-08-21'),
('Matthew', 'V', 'Austin', '200802224', 'Hamilton, ON', 'M', 200000, '333445555', 5,  '1985-08-05',  '2007-07-06'),
('Lauren', 'J', 'Baldwin', '201052043', 'Paris, ON', 'F', 890000, '359624751', 11,  '1992-07-07',  '2014-10-01'),
('Angelika', 'H', 'Ayers', '201073976', 'Guelph, ON', 'F', 56000, '202058568', 11,  '1971-01-26',  '1995-10-09'),
('Jared', 'K', 'Aziz', '201165466', 'London, ON', 'M', 50000, '987654321', 4,  '1990-12-15',  '2011-05-20'),
('Emma', 'L', 'Azizi', '201272287', 'Hamilton, ON', 'F', 40000, '123456789', 24,  '1988-10-03',  '2013-05-11'),
('Kelly', 'W', 'Barham', '201443758', 'Hamilton, ON', 'F', 140000, '843025296', 24,  '1989-03-06',  '2009-07-15'),
('Charlotte', 'Q', 'Balahura', '201450220', 'Guelph, ON', 'F', 65000, '629575266', 24,  '1990-12-03',  '2012-05-26'),
('Colin', 'R', 'Baroey', '201654020', 'Guelph, ON', 'M', 70000, '444555777', 2,  '1988-03-09',  '2013-03-02'),
('Ashley', 'V', 'Barta', '201739519', 'London, ON', 'F', 72000, '333445555', 1,  '1967-02-08',  '1988-05-02'),
('MacKenzie', 'A', 'Barsky', '201774583', 'Paris, ON', 'M', 99000, '987654321', 4,  '1986-06-29',  '2008-01-01'),
('Catherine', 'B', 'Bartlett', '201941078', 'Hamilton, ON', 'F', 80000, '315565726', 24,  '1990-10-15',  '2012-07-05'),
('Catherine', 'I', 'Bartley', '201959328', 'Guelph, ON', 'F', 150000, '315565726', 24,  '1990-04-07',  '2014-07-04'),
('Richard', 'T', 'Ramla', '202058568', 'Houston,, TX', 'M', 90000, '296045397', 5,  '1993-04-24',  '2016-07-10'),
('Sarah', 'A', 'Walters', '202176619', 'Hamilton, ON', 'F', 132000, '296045397', 11,  '1989-12-14',  '2011-08-16'),
('Denzel', 'O', 'Washington', '202185616', 'Guelph, ON', 'M', 150000, '202058568', 11,  '1965-05-06',  '1986-01-31'),
('Cassandra', 'D', 'Jonesboro', '202247633', 'Guelph, ON', 'F', 80000, '987654321', 4,  '1983-04-06',  '2006-06-25'),
('Kaitlyn', 'G', 'Anderson', '202428993', 'Paris, ON', 'F', 84000, '888665555', 1,  '1996-05-16',  '2016-11-15'),
('Aaron', 'Z', 'Austin', '202561262', 'Guelph, ON', 'M', 86000, '888665555', 24,  '1988-07-22',  '2011-07-08'),
('Tony', 'W', 'Saunders', '202561319', 'Hamilton, ON', 'M', 86000, '333445555', 4,  '1993-10-05',  '2017-01-24'),
('Emily', 'S', 'Nicholson', '202744742', 'London, ON', 'F', 50000, '987654321', 4,  '1971-03-10',  '1995-08-14'),
('Karly', 'A', 'Selles', '202785848', 'Paris, ON', 'F', 100000, '987654321', 4,  '1974-09-22',  '1998-04-21'),
('Laurence', 'C', 'De Niro', '202860324', 'Hamilton, ON', 'M', 40000, '999999999', 5,  '1977-10-20',  '1999-11-15'),
('Valentine', 'X', 'Muravyov', '218167890', 'Waldorf, MD', 'M', 80000, '444555777', 2,  '1997-09-07',  '2020-06-15'),
('Tushar', 'L', 'Dobhal', '222222222', 'Houston, TX', 'M', 70000, '999999999', 5,  '1999-12-03',  '2022-03-06'),
('James', 'O', 'Bond', '231456456', 'London, On', 'M', 25000, '888665555', 1,  '1993-11-04',  '2013-11-11'),
('William', 'M', 'Rawson', '232171234', 'Herndon, WV', 'M', 60000, '444555777', 2,  '1989-10-30',  '2010-05-24'),
('Michael', 'M', 'Monroe', '268268702', 'Toronto, On', 'M', 54000, '359624751', 11,  '1993-12-15',  '2016-03-04'),
('Leonard', 'K', 'Carnes', '295501234', 'Convoy, OH', 'M', 127000, '444555777', 2,  '1973-08-06',  '1996-02-13'),
('Shuchi', 'A', 'Pandit', '296045397', 'Guelph,, ON', 'F', 980000, '888665555', 4,  '1985-05-06',  '2007-10-29'),
('Melissa', 'K', 'Iv', '306737594', 'Toronto,, On', 'F', 164000, '460836586', 11,  '1994-06-03',  '2017-02-11'),
('Heidi', 'N', 'Klum', '315565726', 'Guelph, ON', 'F', 240000, '925468826', 24,  '1974-08-23',  '1998-06-27'),
('Karen', 'T', 'Winters', '321400789', 'Houston, TX', 'F', 180000, '333445555', 5,  '1973-07-03',  '1993-09-09'),
('Jean', 'C', 'Taylor', '321456789', 'Houston, TX', 'M', 160000, '333445555', 5,  '1997-03-06',  '2020-07-30'),
('Alex', 'Q', 'Gaijic', '333333333', 'Houston, TX', 'M', 40000, '999999999', 5,  '1964-06-21',  '1987-04-25'),
('Frank', 'T', 'Wong', '333445555', 'Houston, TX', 'M', 80000, '888665555', 5,  '1997-06-26',  '2020-10-28'),
('Trevor', 'T', 'Davis', '338888555', 'Almonte, ON', 'M', 100000, '987654321', 4,  '1996-03-24',  '2020-11-28'),
('Josiah', 'H', 'Timmins', '353467409', 'Guelph, ON', 'M', 130000, '888665555', 7,  '1983-09-21',  '2008-05-18'),
('Cindy', 'H', 'Crawford', '359624751', 'Toronto, On', 'F', 164000, '888665555', 11,  '1986-02-21',  '2009-12-25'),
('Mohammad', 'P', 'Ali', '444444444', 'Houston, TX', 'M', 10000, '999999999', 5,  '1995-10-03',  '2019-05-15'),
('Jean', 'J', 'Lansing', '444555777', 'Milwaukee, WI', 'F', 227000, 'null', 2,  '1982-01-27',  '2002-04-29'),
('Bonnie', 'Z', 'Baker', '449721234', 'Richardson, TX', 'F', 27000, '444555777', 2,  '1998-08-12',  '2022-07-16'),
('Joyce', 'A', 'Roberts', '453422453', 'Houston, TX', 'F', 150000, '333445555', 5,  '1996-03-16',  '2018-07-28'),
('Joyce', 'A', 'English', '453453453', 'Houston, TX', 'F', 50000, '333445555', 5,  '1963-06-28',  '1987-10-15'),
('Carmel', 'D', 'Schembri', '460836586', 'Guelph,, On', 'M', 197000, '807844760', 4,  '1992-05-29',  '2012-07-05'),
('Paula', 'J', 'Krach', '515821234', 'Elk City, KS', 'F', 67000, '444555777', 2,  '1972-04-19',  '1992-08-26'),
('Shannon', 'C', 'Page', '546031234', 'Redmond, WA', 'M', 170000, '444555777', 2,  '1992-01-05',  '2015-05-02'),
('Pamela', 'A', 'English', '546546877', 'Guelph, On', 'F', 56000, '359624751', 11,  '1984-08-02',  '2005-11-01'),
('Khadijah', 'L', 'Sabbagh', '550561234', 'Arroyo, CA', 'F', 123000, '444555777', 2,  '1972-03-02',  '1993-06-08'),
('Scott', 'A', 'Dougan', '558181999', 'Midland, ON', 'M', 200000, '333445555', 5,  '1987-09-08',  '2010-07-24'),
('Rachel', 'A', 'Castillo', '560123563', 'Guelph,, On', 'F', 56000, '202058568', 11,  '1964-01-22',  '1986-05-24'),
('Donald', 'F', 'Regan', '566879301', 'Toronto, On', 'M', 890000, '359624751', 11,  '1998-10-08',  '2022-06-28'),
('Delores', 'E', 'Patterson', '606088000', 'Orangeville, ON', 'F', 50000, '987654321', 4,  '1988-04-04',  '2008-06-12'),
('Rosie', 'N', 'Jones', '607465254', 'Fredericton, NB', 'F', 40000, '123456789', 24,  '1966-01-08',  '1988-02-07'),
('Daniela', 'N', 'Pestova', '629568526', 'St. Johns, NF', 'F', 65000, '629575266', 24,  '1990-11-28',  '2013-01-30'),
('Brooklyn', 'N', 'Decker', '629575266', 'Guelph, ON', 'F', 140000, '843025296', 24,  '1965-11-27',  '1985-11-30'),
('Carolyn', 'D', 'Dattilo', '631541234', 'Redmond, WA', 'F', 70000, '444555777', 2,  '1991-12-10',  '2015-01-10'),
('Imran', 'Z', 'Kanji', '666258951', 'Guelph, On', 'M', 99000, '987654321', 4,  '1966-12-08',  '1991-01-31');


CREATE TABLE Dependent(
  Essn CHAR(9),
  Dependent_name VARCHAR(12) NOT NULL,
  Sex CHAR NOT NULL,
  Bdate DATE NOT NULL,
  Relationship VARCHAR(10) NOT NULL,
  PRIMARY KEY(Essn, Dependent_name)
);

INSERT INTO Dependent VALUES
('123456789', 'Alice', 'F', '2008-12-31', 'Daughter'),
('123456789', 'Elizabeth', 'F', '1987-05-05', 'Spouse'),
('123456789', 'Michael', 'M', '2008-01-01', 'Son'),
('231456456', 'Delilah', 'F', '1968-05-13', 'Spouse'),
('268268702', 'Minnie', 'F', '1978-08-11', 'Spouse'),
('268268702', 'Pluto', 'M', '1988-07-31', 'Son'),
('321400789', 'Julia', 'F', '1973-05-05', 'Spouse'),
('321456789', 'Angus', 'M', '1995-01-08', 'Son'),
('321456789', 'Francine', 'F', '1968-05-07', 'Spouse'),
('321456789', 'Tracey', 'F', '1998-12-12', 'Daughter'),
('333445555', 'Alice', 'F', '2006-04-05', 'Daughter'),
('333445555', 'Joy', 'F', '1985-05-03', 'Spouse'),
('333445555', 'Theodore', 'M', '2003-10-25', 'Son'),
('444555777', 'Emily', 'F', '1978-05-26', 'Spouse'),
('453422453', 'Emma', 'F', '2005-04-06', 'Daughter'),
('453422453', 'Thomas', 'M', '2003-10-03', 'Son'),
('515821234', 'James', 'M', '1992-04-14', 'Son'),
('550561234', 'Yuri', 'M', '1993-12-25', 'Spouse'),
('666258951', 'Halle', 'F', '1999-11-05', 'Daughter'),
('666258951', 'Maximus', 'M', '2007-01-09', 'Son'),
('666258951', 'Megan', 'F', '1987-01-21', 'Spouse'),
('987654001', 'Charlotte', 'F', '1963-02-25', 'Spouse'),
('987654321', 'Abner', 'M', '1992-02-29', 'Spouse'),
('100040001', 'Harry', 'M', '2020-12-31', 'Son'),
('111111111', 'Richard', 'M', '2020-05-05', 'Son'),
('111222333', 'William', 'M', '2008-01-01', 'Son'),
('198782427', 'Leonard', 'M', '2020-05-13', 'Son'),
('199098293', 'Shuchi', 'F', '2020-08-11', 'Daughter'),
('199171129', 'Melissa', 'F', '2020-07-31', 'Daughter'),
('199196331', 'Josiah', 'M', '2018-05-05', 'Son'),
('199302835', 'Mohammad', 'M', '2018-01-08', 'Son'),
('199489442', 'Bonnie', 'F', '2018-05-07', 'Daughter'),
('199608611', 'Carmel', 'F', '2018-12-12', 'Daughter'),
('199685000', 'Khadijah', 'F', '2016-04-05', 'Daughter'),
('199705791', 'Rachel', 'F', '2016-05-03', 'Daughter'),
('200002511', 'Daniela', 'F', '2016-10-25', 'Daughter'),
('200178650', 'Leonard', 'M', '2016-05-26', 'Son'),
('200243095', 'Shuchi', 'F', '2016-04-06', 'Daughter'),
('200352295', 'Melissa', 'M', '2014-10-03', 'Son'),
('200493155', 'Josiah', 'F', '2014-04-14', 'Daughter'),
('200587814', 'Mohammad', 'M', '2014-12-25', 'Son'),
('200626576', 'Bonnie', 'F', '2014-11-05', 'Daughter'),
('200757441', 'Carmel', 'F', '2012-01-09', 'Daughter'),
('201052043', 'Khadijah', 'F', '2012-01-21', 'Daughter'),
('201073976', 'Rachel', 'F', '2012-02-25', 'Daughter'),
('201165466', 'Daniela', 'F', '2012-02-29', 'Daughter'),
('201443758', 'Leonard', 'M', '2020-12-31', 'Son'),
('201450220', 'Anne', 'F', '2020-05-05', 'Daughter'),
('201739519', 'Melissa', 'M', '2008-01-01', 'Son'),
('444444444', 'Josiah', 'F', '2020-05-13', 'Daughter'),
('449721234', 'Mohammad', 'M', '2020-08-11', 'Son'),
('453453453', 'Bonnie', 'F', '2020-07-31', 'Daughter'),
('460836586', 'Carmel', 'F', '2018-05-05', 'Daughter'),
('546031234', 'Khadijah', 'F', '2018-01-08', 'Daughter'),
('546546877', 'Rachel', 'F', '2018-05-07', 'Daughter'),
('560123563', 'Daniela', 'F', '2018-12-12', 'Daughter'),
('566879301', 'Carmel', 'F', '2016-04-05', 'Daughter'),
('607465254', 'Khadijah', 'F', '2016-05-03', 'Daughter'),
('629568526', 'Rachel', 'F', '2016-10-25', 'Daughter'),
('629575266', 'Daniela', 'F', '2016-05-26', 'Daughter');
 


CREATE TABLE Department(
  Dname VARCHAR(15) NOT NULL,
  Dnumber INT NOT NULL,
  Mgr_ssn CHAR(9) NOT NULL,
  PRIMARY KEY(Dnumber),
  UNIQUE(Dname)
);

CREATE TABLE Dept_Location(
  Dnumber INT NOT NULL,
  Dlocation VARCHAR(15) NOT NULL,
  PRIMARY KEY(Dnumber, Dlocation)
);

CREATE TABLE Project(
  Pname VARCHAR(15) NOT NULL,
  Pnumber INT NOT NULL,
  Plocation VARCHAR(15) NOT NULL,
  Dnum INT NOT NULL,
  PRIMARY KEY(Pnumber),
  UNIQUE(Pname)
);


CREATE TABLE Works_On(
  Essn CHAR(9) NOT NULL,
  Pno INT NOT NULL,
  Hours DEC(4,1) NOT NULL,
  PRIMARY KEY(Essn, Pno)
);

INSERT INTO Department  VALUES
('Headquarters', 1, '888665555'),
('Marketing', 2, '444555777'),
('Administration', 4, '987654321'),
('Research', 5, '333445555'),
('Finance', 7, '353467409'),
('Engineering', 11, '359624751'),
('Model', 24, '123456789');

INSERT INTO Dept_Location VALUES
(1, 'Houston'),
(2, 'Redmond'),
(4, 'Stafford'),
(5, 'Bellaire'),
(7, 'Guelph'),
(5, 'Houston'),
(11, 'Houston'),
(24, 'Guelph'),
(5, 'Sugarland');

INSERT INTO PROJECT VALUES
('ProductX', 1, 'Bellaire', 5),
('ProductY', 2, 'Sugarland', 5),
('ProductZ', 3, 'Houston', 5),
('Tesseract', 4, 'Redmond', 2),
('Computerization', 10, 'Stafford', 4),
('MancalaGame', 15, 'Sugarland', 5),
('Reorganization', 20, 'Houston', 1),
('VSecret', 24, 'Guelph', 24),
('Newbenefits', 30, 'Stafford', 4),
('Construction', 44, 'Sugarland', 5),
('Innovation', 117, 'Guelph', 11),
('Fraud', 118, 'Toronto', 11);

INSERT INTO Works_On VALUES
('100040001', 2, 6),
('111111111', 3, 20),
('111111111', 20, 20),
('111222333', 1, 6),
('111222333', 3, 15),
('123456789', 1, 33),
('123456789', 2, 8),
('198782427', 4, 40),
('198928552', 10, 20),
('198928552', 30, 20),
('199098293', 117, 40),
('199171129', 15, 20),
('199171129', 44, 20),
('199196331', 24, 35),
('199196331', 118, 5),
('199302835', 15, 25),
('199302835', 44, 15),
('199305628', 3, 23),
('199305628', 15, 15),
('199489442', 3, 5),
('199489442', 15, 15),
('199489442', 44, 20),
('199608611', 10, 18),
('199608611', 30, 22),
('199685000', 44, 40),
('199705791', 117, 40),
('199923690', 44, 35),
('200002511', 4, 37),
('200178650', 4, 40),
('200243095', 44, 39),
('200352295', 30, 40),
('200369792', 44, 40),
('200493155', 4, 35),
('200587814', 4, 37),
('200626576', 117, 40),
('200757441', 4, 39),
('200802224', 44, 40),
('201052043', 117, 35),
('201073976', 117, 40),
('201165466', 30, 37),
('201272287', 24, 40),
('201443758', 24, 40),
('201450220', 24, 39),
('201654020', 4, 40),
('201739519', 44, 37),
('201774583', 30, 35),
('201941078', 24, 40),
('201959328', 24, 39),
('202176619', 117, 40),
('202185616', 117, 40),
('202247633', 30, 35),
('202428993', 20, 37),
('202561262', 24, 39),
('202561319', 30, 40),
('202744742', 30, 40),
('202785848', 30, 40),
('202860324', 44, 35),
('218167890', 4, 20),
('222222222', 3, 35),
('222222222', 20, 5),
('231456456', 20, 12),
('268268702', 117, 35),
('315565726', 24, 33),
('321400789', 15, 10),
('321400789', 20, 3),
('321400789', 30, 5),
('321400789', 117, 2),
('321456789', 2, 7),
('321456789', 44, 33),
('333333333', 20, 40),
('333445555', 1, 3),
('333445555', 2, 6),
('333445555', 3, 7),
('333445555', 10, 10),
('333445555', 15, 10),
('333445555', 20, 3),
('333445555', 30, 5),
('333445555', 117, 2),
('338888555', 10, 11),
('359624751', 117, 25),
('359624751', 118, 15),
('444555777', 4, 18),
('453422453', 2, 20),
('453422453', 44, 20),
('453453453', 1, 20),
('453453453', 2, 20),
('515821234', 4, 20),
('546031234', 4, 5),
('546546877', 118, 40),
('558181999', 3, 35),
('566879301', 118, 40),
('606088000', 20, 17),
('607465254', 24, 33),
('629575266', 24, 33),
('631541234', 4, 10),
('666258951', 10, 40),
('666884444', 3, 40),
('681525266', 24, 33),
('888445555', 20, 15),
('888445555', 30, 20),
('891029345', 2, 5),
('891029345', 3, 7),
('891029345', 10, 10),
('891029345', 44, 3),
('925468826', 24, 33),
('987654001', 3, 40),
('987654001', 20, 15),
('987654001', 30, 20),
('987654321', 20, 15),
('987654321', 30, 20),
('987789987', 10, 35),
('987789987', 30, 5),
('987987987', 10, 35),
('987987987', 30, 5),
('999117777', 10, 10),
('999117777', 30, 30),
('999887777', 10, 10),
('999887777', 30, 30),
('999999999', 3, 20),
('999999999', 20, 20),
('105947378', 118, 32),
('202058568', 118, 33),
('232171234', 118, 20),
('295501234', 118, 33),
('296045397', 118, 23),
('306737594', 118, 18),
('353467409', 118, 38),
('444444444', 118, 22),
('449721234', 118, 34),
('460836586', 118, 26),
('550561234', 118, 32);

DROP TABLE IF EXISTS user_roles;
DROP TABLE IF EXISTS roles;
DROP TABLE IF EXISTS users;


CREATE TABLE users ( user_id SERIAL PRIMARY KEY, 
    username VARCHAR(50) UNIQUE NOT NULL, 
    password VARCHAR(255) NOT NULL, 
    role VARCHAR(20) NOT NULL, 
    department_id int
);  

-- Create Roles table
CREATE TABLE roles (
    role_id SERIAL PRIMARY KEY,
    role_name VARCHAR(50) UNIQUE NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create User_Roles junction table for many-to-many relationship
CREATE TABLE user_roles (
    user_id INT NOT NULL,
    role_id INT NOT NULL,
    assigned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (user_id, role_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (role_id) REFERENCES roles(role_id) ON DELETE CASCADE
);

ALTER TABLE user_roles ADD CONSTRAINT user_role_unique UNIQUE (user_id);


INSERT INTO roles (role_name, description) VALUES
('super_admin', 'Has full access to all system features and data'),
('department_admin', 'Can manage employees and data within their assigned department'),
('normal_user', 'Can view data related to their department only');

-- Drop views if already exists
DROP VIEW IF EXISTS DepartmentEmployee;
DROP VIEW IF EXISTS DepartmentView;
DROP VIEW IF EXISTS DepartmentProject;
DROP VIEW IF EXISTS DepartmentJoinedData;

-- View for Employees per department
CREATE OR REPLACE VIEW DepartmentEmployee AS
SELECT DISTINCT e.SSN, e.Fname, e.Lname, e.Salary, e.Dno
FROM Employee e
JOIN users u ON e.Dno = u.department_id
WHERE u.role = 'normal_user' OR u.role = 'department_admin';

-- View for Departments
CREATE OR REPLACE VIEW DepartmentView AS
SELECT DISTINCT d.Dnumber, d.Dname, d.Mgr_ssn
FROM Department d
JOIN users u ON d.Dnumber = u.department_id
WHERE u.role = 'normal_user' OR u.role = 'department_admin';

-- View for Projects per department
CREATE OR REPLACE VIEW DepartmentProject AS
SELECT DISTINCT p.Pnumber, p.Pname, p.Plocation, p.Dnum
FROM Project p
JOIN users u ON p.Dnum = u.department_id
WHERE u.role = 'normal_user' OR u.role = 'department_admin';

-- View for Joined data per department
CREATE OR REPLACE VIEW DepartmentJoinedData AS
SELECT e.Fname, e.Lname, e.Salary, d.Dname, p.Pname, p.Plocation, d.Dnumber
FROM Employee e
JOIN Department d ON e.Dno = d.Dnumber
JOIN Project p ON d.Dnumber = p.Dnum;
