/* Exibir o menor peso entre as mulheres que nasceram fora do Brasil 
e entre 01/Jan/1990 e 31/Dez/2000 */

select min(peso) from pessoas 
where sexo = 'F' and nacionalidade != 'Brasil' and nascimento between '1990/01/01' and '2000/12/31';