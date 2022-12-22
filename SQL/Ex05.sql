/*  Mostrar uma lista com nome e nacionalidade de todos os homens que 
tem "Silva" no nome, não nasceram no Brasil e pesam menos de 100 kg */

select nome, nacionalidade from pessoas 
where nome like '%silva%' and nacionalidade != 'Brasil' and peso < 100;