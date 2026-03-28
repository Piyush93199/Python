import numpy as np

class SGD:
    """
    Stochastic Gradient Descent Optimizer.
    
    Think of this as a "Stepping-Down-the-Mountain" algorithm. 
    It helps us find the lowest point (the minimum) of a function 
    by taking small steps downhill at every step.
    """
    def __init__(self, learning_rate=0.01, epochs=100, batch_size=1, tolerance=1e-6):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.batch_size = batch_size
        self.tolerance = tolerance
        self.history = []

    def minimize(self, objective_func, gradient_func, x_start, data=None):
        """
        How to find the lowest point of a landscape:
        
        1. Start somewhere (x_start).
        2. Look around and feel which direction is downhill (the gradient).
        3. Take a tiny step that way (the learning rate).
        4. Do this until you reach the bottom (the tolerance) or run out of energy (epochs).
        
        Args:
            objective_func: The shape of the hill we're walking down.
            gradient_func: The direction that points uphill (so we go the opposite way!).
            x_start: Our first guess on where the bottom is.
            data: If we're using real data, it makes the slope "wobbly" and stochastic!
        
        Returns:
            x_found: Our best guess of where the valley is.
        """
        x = np.array(x_start, dtype=float)
        self.history = [x.copy()]
        
        for epoch in range(self.epochs):
            if data is not None:
                # 1. Shuffle our map so we don't follow the same path every time.
                np.random.shuffle(data)
                
                # 2. Break our search into small pieces (mini-batches).
                for i in range(0, len(data), self.batch_size):
                    batch = data[i:i+self.batch_size]
                    
                    # 3. Feel the local slope here.
                    grad = gradient_func(x, batch)
                    
                    # 4. Take a small step downhill.
                    x -= self.learning_rate * grad
            else:
                # If there's no data, we're just walking down a smooth hill.
                grad = gradient_func(x)
                x -= self.learning_rate * grad
            
            self.history.append(x.copy())
            
            # Check for convergence
            if np.linalg.norm(self.history[-1] - self.history[-2]) < self.tolerance:
                print(f"Converged at epoch {epoch}")
                break
                
        return x

    def get_history(self):
        return np.array(self.history)
