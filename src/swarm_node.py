import random

class SwarmNode:
    def __init__(self, node_id):
        self.node_id = node_id
        self.neighbors = []
        self.state = 'IDLE'
        self.consensus_value = None

    def join_swarm(self, neighbor_nodes):
        self.neighbors = neighbor_nodes
        self.state = 'ACTIVE'

    def propose_value(self, value):
        self.consensus_value = value
        self.broadcast_proposal()

    def broadcast_proposal(self):
        for neighbor in self.neighbors:
            neighbor.receive_proposal(self.node_id, self.consensus_value)

    def receive_proposal(self, proposer_id, value):
        if self.state == 'ACTIVE':
            self.evaluate_proposal(proposer_id, value)

    def evaluate_proposal(self, proposer_id, value):
        # Implement swarm consensus protocol logic here
        # e.g., majority voting, byzantine fault tolerance, etc.
        if random.random() < 0.5:
            self.accept_proposal(proposer_id, value)
        else:
            self.reject_proposal(proposer_id)

    def accept_proposal(self, proposer_id, value):
        self.consensus_value = value
        self.broadcast_acceptance(proposer_id)

    def reject_proposal(self, proposer_id):
        self.broadcast_rejection(proposer_id)

    def broadcast_acceptance(self, proposer_id):
        for neighbor in self.neighbors:
            neighbor.receive_acceptance(self.node_id, proposer_id)

    def broadcast_rejection(self, proposer_id):
        for neighbor in self.neighbors:
            neighbor.receive_rejection(self.node_id, proposer_id)

    def receive_acceptance(self, acceptor_id, proposer_id):
        # Handle acceptance from other nodes
        pass

    def receive_rejection(self, rejector_id, proposer_id):
        # Handle rejection from other nodes
        pass
