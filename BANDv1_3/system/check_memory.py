import gc

# Function to print memory information
def print_memory_info():
    print("Memory Information:")
    print("Heap free:", gc.mem_free())
    print("Heap allocated:", gc.mem_alloc())
    print("Heap total:", gc.mem_free() + gc.mem_alloc())
    print()

# Example usage
def check_memory():
    print("Starting program...")
    
    # Print initial memory information
    print_memory_info()
    
    # Your code here...
    # Example: allocating some memory
    my_list = []
    for i in range(1000):
        my_list.append(i)
    
    # Print memory information after allocation
    print("After allocating memory:")
    print_memory_info()
    
    # Simulating some processing
    for i in range(10000):
        pass
    
    # Print memory information after processing
    print("After processing:")
    print_memory_info()

check_memory()