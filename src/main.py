import os
import sys
import time
import random
import multiprocessing as mp

from agents.swarm import SwarmAgent
from agents.scraper import ScrapingAgent
from governance.protocol import GovernanceProtocol

def main():
    # Initialize the governance protocol
    protocol = GovernanceProtocol()

    # Spawn the swarm of agents
    swarm_size = 50
    swarm = [SwarmAgent(protocol) for _ in range(swarm_size)]

    # Spawn the scraping agents
    scraper_size = 10
    scrapers = [ScrapingAgent(protocol) for _ in range(scraper_size)]

    # Run the agents in parallel
    processes = []
    for agent in swarm + scrapers:
        p = mp.Process(target=agent.run)
        p.start()
        processes.append(p)

    # Wait for the agents to finish
    for p in processes:
        p.join()

    print("Distributed Autonomous Governance System has completed its execution.")

if __name__ == "__main__":
    main()