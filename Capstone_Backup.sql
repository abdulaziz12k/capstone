PGDMP         9                {            capstone    15.3    15.3                0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    41517    capstone    DATABASE     �   CREATE DATABASE capstone WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Arabic_Saudi Arabia.1252';
    DROP DATABASE capstone;
                student    false            �            1259    41528    actors    TABLE     �   CREATE TABLE public.actors (
    id integer NOT NULL,
    name character varying NOT NULL,
    age integer,
    gender character varying
);
    DROP TABLE public.actors;
       public         heap    student    false            �            1259    41527    actors_id_seq    SEQUENCE     �   CREATE SEQUENCE public.actors_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 $   DROP SEQUENCE public.actors_id_seq;
       public          student    false    217                       0    0    actors_id_seq    SEQUENCE OWNED BY     ?   ALTER SEQUENCE public.actors_id_seq OWNED BY public.actors.id;
          public          student    false    216            �            1259    41537    alembic_version    TABLE     X   CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);
 #   DROP TABLE public.alembic_version;
       public         heap    student    false            �            1259    41519    movies    TABLE     u   CREATE TABLE public.movies (
    id integer NOT NULL,
    title character varying NOT NULL,
    release_date date
);
    DROP TABLE public.movies;
       public         heap    student    false            �            1259    41518    movies_id_seq    SEQUENCE     �   CREATE SEQUENCE public.movies_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 $   DROP SEQUENCE public.movies_id_seq;
       public          student    false    215                       0    0    movies_id_seq    SEQUENCE OWNED BY     ?   ALTER SEQUENCE public.movies_id_seq OWNED BY public.movies.id;
          public          student    false    214            o           2604    41531 	   actors id    DEFAULT     f   ALTER TABLE ONLY public.actors ALTER COLUMN id SET DEFAULT nextval('public.actors_id_seq'::regclass);
 8   ALTER TABLE public.actors ALTER COLUMN id DROP DEFAULT;
       public          student    false    216    217    217            n           2604    41522 	   movies id    DEFAULT     f   ALTER TABLE ONLY public.movies ALTER COLUMN id SET DEFAULT nextval('public.movies_id_seq'::regclass);
 8   ALTER TABLE public.movies ALTER COLUMN id DROP DEFAULT;
       public          student    false    214    215    215                      0    41528    actors 
   TABLE DATA           7   COPY public.actors (id, name, age, gender) FROM stdin;
    public          student    false    217   �                 0    41537    alembic_version 
   TABLE DATA           6   COPY public.alembic_version (version_num) FROM stdin;
    public          student    false    218                     0    41519    movies 
   TABLE DATA           9   COPY public.movies (id, title, release_date) FROM stdin;
    public          student    false    215   *                  0    0    actors_id_seq    SEQUENCE SET     <   SELECT pg_catalog.setval('public.actors_id_seq', 22, true);
          public          student    false    216                       0    0    movies_id_seq    SEQUENCE SET     <   SELECT pg_catalog.setval('public.movies_id_seq', 16, true);
          public          student    false    214            s           2606    41535    actors actors_pkey 
   CONSTRAINT     P   ALTER TABLE ONLY public.actors
    ADD CONSTRAINT actors_pkey PRIMARY KEY (id);
 <   ALTER TABLE ONLY public.actors DROP CONSTRAINT actors_pkey;
       public            student    false    217            u           2606    41541 #   alembic_version alembic_version_pkc 
   CONSTRAINT     j   ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);
 M   ALTER TABLE ONLY public.alembic_version DROP CONSTRAINT alembic_version_pkc;
       public            student    false    218            q           2606    41526    movies movies_pkey 
   CONSTRAINT     P   ALTER TABLE ONLY public.movies
    ADD CONSTRAINT movies_pkey PRIMARY KEY (id);
 <   ALTER TABLE ONLY public.movies DROP CONSTRAINT movies_pkey;
       public            student    false    215               X   x�3�����46��M�I�2��\S��5qM�\s��η ���\Kΐ�����"NcN_���VQC��FXE�����qqq ��66            x�370�0J1M�06L����� 'y�         U   x�3�LJ,�M��4200�!.Sΐ������T����������qs�8�-q���0�%a�C��-#c��%W� �%;     