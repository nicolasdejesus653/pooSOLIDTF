# Princípios SOLID - Aulas UniFAAT

Este repositório contém exemplos de código em Python para cada um dos cinco princípios SOLID de design de software orientado a objetos. O material foi criado para as aulas de Engenharia de Software da UniFAAT.

## O que é SOLID?

SOLID é um acrônimo para cinco princípios de design que visam tornar os sistemas de software mais compreensíveis, flexíveis e fáceis de manter.

1.  **[S]ingle Responsibility Principle (Princípio da Responsabilidade Única):** Uma classe deve ter apenas um motivo para mudar.
2.  **[O]pen/Closed Principle (Princípio Aberto/Fechado):** Entidades de software (classes, módulos, funções, etc.) devem estar abertas para extensão, mas fechadas para modificação.
3.  **[L]iskov Substitution Principle (Princípio da Substituição de Liskov):** Objetos de uma superclasse devem ser substituíveis por objetos de uma subclasse sem afetar a correção do programa.
4.  **[I]nterface Segregation Principle (Princípio da Segregação de Interface):** Nenhuma classe deve ser forçada a depender de métodos que não utiliza. É melhor ter várias interfaces específicas do que uma única interface geral.
5.  **[D]ependency Inversion Principle (Princípio da Inversão de Dependência):** Módulos de alto nível não devem depender de módulos de baixo nível. Ambos devem depender de abstrações. Abstrações não devem depender de detalhes; detalhes devem depender de abstrações.

## Exemplos

Cada princípio tem seu próprio Jupyter Notebook com exemplos de código comentados:

-   [`001 - single_responsibility_principle.ipynb`](001 - single_responsibility_principle.ipynb)
-   [`002 - open_closed_principle.ipynb`](002 - open_closed_principle.ipynb)
-   [`003 - liskov_substitution_principle.ipynb`](003 - liskov_substitution_principle.ipynb)
-   [`004 - interface_segregation_principle.ipynb`](004 - interface_segregation_principle.ipynb)
-   [`005 - dependency_inversion_principle.ipynb`](005 - dependency_inversion_principle.ipynb)

---

## Exercício Prático: Refatorando com SOLID

Para aplicar os conceitos aprendidos, veja o exercício prático de refatoração no arquivo [`exercicio.md`](exercicio.md).
