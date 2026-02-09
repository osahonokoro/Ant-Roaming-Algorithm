def calculate_reward(agent, coverage, incidents, compliance,
                     K1=1.0, K2=2.0, K3=0.5):
    """
    Reward function based on Eq. 7 in the paper.
    
    Parameters:
    - agent: agent ID or object
    - coverage: number of nodes visited (coverage quality)
    - incidents: list of incident events where agent was first responder
    - compliance: measure of policy adherence (0–1 scale)
    - K1, K2, K3: coefficients balancing coverage, responsiveness, compliance
    
    Returns:
    - reward (float)
    """
    coverage_reward = K1 * coverage
    response_reward = K2 * len(incidents)
    compliance_penalty = K3 * (1 - compliance)

    total_reward = coverage_reward + response_reward - compliance_penalty
    return total_reward
