from vm.Memory import Memory

class Context:
    def __init__(self, Memory):
        self.saved_memory = Memory
        self.saved_IP = 0
        
    def save_IP(self, IP):
        self.saved_IP = IP
        
    def get_Memory(self):
        return self.saved_memory
    
    def get_IP(self):
        return self.saved_IP