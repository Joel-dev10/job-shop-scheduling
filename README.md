# job-shop-scheduling
This repository is built to find ways to optimize the solutions for the NP-hard problem Job Shop Scheduling and subsequently Flexible Job Shop Scheduling Problem.

The Job Shop Scheduling Problem (JSSP) is a combinatorial optimization problem where the objective is to schedule a set of jobs on a set of machines. Each job consists of a sequence of operations, and each operation requires a specific machine for a certain duration. The operations of each job must be processed in a predetermined order, and no two operations can use the same machine at the same time.

The Flexible Job Shop Scheduling Problem (FJSSP) is a generalization of the Job Shop Scheduling Problem (JSSP), where each operation in a job can be processed on one of several available machines, rather than a single specific machine. Each machine may have different processing times for the same operation, adding flexibility to the scheduling.

Problem Statement:
A set of J jobs, a set of R machines/resources, and a set of O operations are given. Each job j consists of a sequence of nj consecutive operations in O, and each operation i belongs to O can be processed on any machine among a subset R(i) belongs to R of compatible machines. The processing time of operation i on machine k is given by pki. According to the technological processing order of jobs (routing), each operation i has one direct predecessor pr(i) and one direct successor fr(i). The jobs should be scheduled in such a way that it follows all the predefined parameters.

These types of scheduling problems (JSSP and FJSSP) are solved with various optimization algorithms such as the Genetic Algorithm, Ant Colony Optimization Algorithm, Particle Swarm Optimization, Tabu Search, Linear Programming Models, Reinforcement Learning, or other Neural Network models which are some of the meta-heuristic approaches. 

JSS_ORTools.py provides a solution using the optimization tools google ortools. It uses the cp_model as the base model to schedule tasks.

Among these various algorithms, using a hybrid algorithm of Genetic Algorithm (GA) and Reinforcement Learning (RL) is expected to be very promising. The advantages of using this hybrid combination are:
1.	GA’s role in exploration and RL’s role in exploitation leads to a perfect balance in exploration and exploitation.
2.	Using GA for global search and RL for local search ensures that the most optimum solution can be found and not get stuck at a local optimum.
3.	GA’s strength in multi-objective problems and RL’s focused optimization could provide solutions that balance multiple objectives effectively.
4.	RL’s feedback loop can negate GA’s lack of feedback mechanism.
5.	RL’s faster adaptation can also negate GA’s slower convergence rate.
The potential challenges of the above algorithm are:
•	Training Time for RL: RL models typically require extensive training, especially when learning optimal policies in complex environments. If the job shop environment is too large or if there are too many decision variables, RL could take a long time to learn an effective policy.
•	Reward Function Design: For RL to be effective, a well-designed reward function is crucial. In job shop scheduling, defining the right balance between competing objectives (e.g., minimizing makespan, maximizing machine utilization) can be complex, and poor reward design can lead to suboptimal schedules.
•	Parameter Tuning Complexity: Hybrid systems often require careful tuning of parameters from both methods (mutation rates, crossover rates in GA, learning rates, discount factors in RL). The interaction between these parameters can complicate the design and implementation.

![image](https://github.com/user-attachments/assets/d40f6096-37f3-4dd9-9fa8-9886bf52bb5c)

(Image can be seen in light mode)
