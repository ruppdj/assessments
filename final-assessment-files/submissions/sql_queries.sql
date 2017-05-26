1)   SELECT applications.stud_id, students.name FROM applications JOIN students ON applications.stud_id = students.id WHERE date > '2014-06-01' GROUP BY applications.stud_id,students.name;



2)  SELECT companies.id, companies.name, COUNT(stud_id) FROM  companies LEFT JOIN applications ON applications.comp_id = companies.id GROUP BY companies.id,companies.name;
