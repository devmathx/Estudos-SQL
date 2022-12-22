/* Mostrar todos os dados de todas as mulheres que nasceram no Brasil
e tem seu nome iniciado com a letra "J" */

select * from pessoas 
where sexo = 'F' and nacionalidade = 'Brasil' and nome like 'J%';