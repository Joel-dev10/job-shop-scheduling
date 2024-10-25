# job-shop-scheduling
This repository is built to find ways to optimize the solutions for the NP-hard problem Job Shop Scheduling and subsequently Flexible Job Shop Scheduling Problem.

The Job Shop Scheduling Problem (JSSP) is a combinatorial optimization problem where the objective is to schedule a set of jobs on a set of machines. Each job consists of a sequence of operations, and each operation requires a specific machine for a certain duration. The operations of each job must be processed in a predetermined order, and no two operations can use the same machine at the same time.

The Flexible Job Shop Scheduling Problem (FJSSP) is a generalization of the Job Shop Scheduling Problem (JSSP), where each operation in a job can be processed on one of several available machines, rather than a single specific machine. Each machine may have different processing times for the same operation, adding flexibility to the scheduling.

Problem Statement:
A set of J jobs, a set of R machines/resources, and a set of O operations are given. Each job j consists of a sequence of nj consecutive operations in O, and each operation i belongs to O can be processed on any machine among a subset R(i) belongs to R of compatible machines. The processing time of operation i on machine k is given by pki. According to the technological processing order of jobs (routing), each operation i has one direct predecessor pr(i) and one direct successor fr(i). The jobs should be scheduled in such a way that it follows all the predefined parameters.

JSS_ORTools.py provides a solution using the optimization tools google ortools. It uses the cp_model as the base model to schedule tasks.