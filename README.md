Ant Roaming Algorithm (ARA)

This repository contains the simulation-based modelling framework for the Ant Roaming Algorithm (ARA), a biologically inspired approach to optimizing adaptive security patrols in resource-constrained environments. Drawing inspiration from ant colony optimization, ARA formalizes pheromone dynamics, probabilistic routing, and adaptive updates to guide patrol agents.

The framework integrates multiple AI modules to enhance patrol effectiveness:

Reinforcement Learning (PPO): enables agents to learn optimal patrol routes and responses.

Anomaly Detection (Isolation Forest): identifies unusual patterns and emerging hotspots.

Computer Vision (YOLO): provides real-time object recognition for threat perception.

Token-Based Incentive Model: motivates personnel and ensures patrol compliance.

Agent-based simulations conducted on a graph representation of the University of Calabar campus demonstrated that ARA achieves:

85.6% average coverage of critical nodes

1.32-unit average response time to incidents

78.4% patrol compliance, outperforming random and static patrol strategies

The repository includes:

Mathematical models for pheromone dynamics, routing, and global boosting

Simulation scripts for agent-based experiments

Documentation of performance metrics and comparative results

Guidelines for integrating ARA with edge-computing devices and mobile patrol interfaces

Key Contributions:

A rigorous mathematical formalization of ARA for adaptive patrol optimization.

Integration of AI modules within a biologically inspired simulation framework.

Empirical validation through agent-based experiments in a real-world campus setting.

ARA provides a scalable, cost-effective solution for smart campus security and urban safety systems, particularly in developing nations where resources are limited. By combining swarm intelligence with AI-driven perception and decision-making, this framework advances both theoretical research and practical deployment of adaptive patrol systems.
