--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: applications; Type: TABLE; Schema: public; Owner: Zipfian; Tablespace: 
--

CREATE TABLE applications (
    comp_id integer,
    stud_id integer,
    date character varying
);


ALTER TABLE public.applications OWNER TO "Zipfian";

--
-- Name: companies; Type: TABLE; Schema: public; Owner: Zipfian; Tablespace: 
--

CREATE TABLE companies (
    id integer,
    name character varying
);


ALTER TABLE public.companies OWNER TO "Zipfian";

--
-- Name: students; Type: TABLE; Schema: public; Owner: Zipfian; Tablespace: 
--

CREATE TABLE students (
    id integer,
    name character varying
);


ALTER TABLE public.students OWNER TO "Zipfian";

--
-- Data for Name: applications; Type: TABLE DATA; Schema: public; Owner: Zipfian
--

COPY applications (comp_id, stud_id, date) FROM stdin;
9	14	2014-06-24
7	2	2014-05-26
5	12	2014-06-06
10	13	2014-05-18
3	13	2014-06-08
9	10	2014-05-28
2	11	2014-05-16
9	1	2014-05-20
1	1	2014-06-21
6	4	2014-06-02
10	12	2014-05-31
1	10	2014-06-06
7	1	2014-05-19
4	9	2014-06-12
3	3	2014-06-06
2	9	2014-06-23
5	2	2014-05-17
2	1	2014-06-18
6	6	2014-06-09
3	1	2014-06-18
10	15	2014-05-22
5	10	2014-05-17
7	13	2014-06-06
1	11	2014-06-20
10	14	2014-05-26
5	6	2014-06-10
3	12	2014-06-22
2	12	2014-05-20
4	1	2014-06-10
10	7	2014-06-22
2	6	2014-06-16
7	7	2014-05-20
2	13	2014-06-10
2	7	2014-05-17
10	11	2014-06-07
4	4	2014-05-26
2	10	2014-05-23
2	15	2014-06-09
2	8	2014-06-21
7	5	2014-06-10
\.


--
-- Data for Name: companies; Type: TABLE DATA; Schema: public; Owner: Zipfian
--

COPY companies (id, name) FROM stdin;
1	tesla
2	lumiata
3	stripe
4	radius
5	facebook
6	heroku
7	looker
8	tagged
9	keen io
10	khan academy
\.


--
-- Data for Name: students; Type: TABLE DATA; Schema: public; Owner: Zipfian
--

COPY students (id, name) FROM stdin;
1	wini
2	jonny
3	dan
4	erin
5	eric
6	sri
7	ethan
8	tripti
9	prasad
10	stephen
11	bruno
12	jana
13	ajay
14	adam
15	michael
\.


--
-- Name: public; Type: ACL; Schema: -; Owner: Zipfian
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM "Zipfian";
GRANT ALL ON SCHEMA public TO "Zipfian";
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

