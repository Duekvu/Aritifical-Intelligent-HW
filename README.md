Programming assignments for my Artificial Intelligent course. 

##### 1.  Implement the corresponding Backtracking Algorithm in Python to solve the n-queen problem.
##### 2.  Implement the corresponding Genetic Algorithmin Python to solve the simple Knapsackproblem.
       - Psudocode from AI book:
       function GENETIC-ALGORITHM(population,FITNESS-FN) returns an individual
            inputs: population, a set of individuals
            FITNESS-FN, a function that measures the fitness of an individual

             repeat
               new_population ← empty set
               for i = 1 to SIZE(population) do
                 x ← RANDOM-SELECTION(population,FITNESS-FN)
                 y ← RANDOM-SELECTION(population,FITNESS-FN)
                 child ← REPRODUCE(x,y)
                 if (small random probability) then child ← MUTATE(child)
                 add child to new_population
               population ← new_population
             until some individual is fit enough, or enough time has elapsed
             return the best individual in population, according to FITNESS-FN
             
             
##### 3.  Sudoku solver in Python using use backtracking with forward checking and "degree" and "MRV" heuristics. 
    How to run the code:
   
     python sudoku.py [filename] > [solution]
     filename: file contains sudoku puzzle set up
     solution: output to solution file.

     i/e: python sudoku.py puzzle1.txt > solution.doc

    Puzzle set up example: refer to puzzle#.txt files.
 

