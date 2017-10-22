clear all; close all; clc;

dbfile = fullfile(pwd,'lotofacil.db');
conn = sqlite(dbfile);
tic;
combinacoes = nchoosek(1:25,15);
toc;
tic;
insert(conn,'todas_combinacoes',...
    {'n1','n2','n3','n4','n5','n6','n7','n8','n9','n10','n11','n12','n13','n14','n15'},combinacoes)
toc;

clear all;

dbfile = fullfile(pwd,'quina.db');
conn = sqlite(dbfile);
tic;
combinacoes = nchoosek(1:5,80);
toc;
tic;
insert(conn,'todas_combinacoes',...
    {'n1','n2','n3','n4','n5'},combinacoes)
toc;


clear all;

dbfile = fullfile(pwd,'megasena.db');
conn = sqlite(dbfile);
tic;
combinacoes = nchoosek(1:6,60);
toc;
tic;
insert(conn,'todas_combinacoes',...
    {'n1','n2','n3','n4','n5','n6'},combinacoes)
toc;